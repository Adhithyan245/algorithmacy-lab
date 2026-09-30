"""Equality-of-Averages (EoA) instrument for Boolean coordination forms.

Reusable Strand-G tooling. Given a finite Boolean next-map (or per-party
rules), an observable, an initial-state ensemble, a horizon T, and an
optional flip-noise level, returns a time-vs-ensemble gap statistic with
an uncertainty estimate and a binary verdict:

    AGREEING  — fail rate < τ  (ergodic-agreeing under the reference measure)
    BREAKING  — fail rate ≥ τ  (EoA-breaking)

Decision thresholds ``ε_div`` and ``τ`` are arguments; studies that use this
instrument must freeze them in a hypotheses file *before* the stress run.
Default values match G2 / ``ergodic_eoa_instrument``: ε_div=0.1, τ=0.25.

No Φ computation lives here. Pair with ``classify_rules`` / ``whole_verdict``
when comparing to the literacy / algorithmacy cut.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Callable, Iterable, Optional, Sequence, Union

import math
import random

State = tuple[int, ...]
Observable = Callable[[State], float]
NextMap = dict[State, State]
Rules = Sequence[Callable[[State], int]]


# Frozen defaults (studies may override only if pre-registered).
DEFAULT_EPS_DIV = 0.1
DEFAULT_FAIL_RATE_THRESH = 0.25
DEFAULT_HORIZON = 64


@dataclass(frozen=True)
class EoAResult:
    """Instrument output for one (form, observable, ensemble, T, noise) cell."""

    verdict: str                 # "AGREEING" | "BREAKING"
    fail_rate: float
    gap_mean: float              # mean |time_avg − ens_avg|
    gap_std: float               # sample std of per-trajectory gaps
    gap_se: float                # gap_std / sqrt(n)
    ensemble_mean: float
    n_trajectories: int
    n_fail: int
    eps_div: float
    fail_rate_thresh: float
    horizon: int
    noise: float
    observable_name: str

    def to_dict(self) -> dict:
        return asdict(self)


def rules_to_next_map(rules: Rules, n: Optional[int] = None) -> NextMap:
    """Deterministic next-state map from per-party Boolean rules."""
    n = len(rules) if n is None else n
    nxt: NextMap = {}
    for s in range(2**n):
        cur = tuple((s >> i) & 1 for i in range(n))
        nxt[cur] = tuple(int(rules[j](cur)) for j in range(n))
    return nxt


def next_map_from_tpm(tpm) -> NextMap:
    """Build a next-map from a deterministic state-by-node TPM (2^n × n)."""
    import numpy as np

    tpm = np.asarray(tpm)
    n_states, n = tpm.shape
    assert n_states == 2**n
    nxt: NextMap = {}
    for s in range(n_states):
        cur = tuple((s >> i) & 1 for i in range(n))
        nxt[cur] = tuple(int(round(float(tpm[s, j]))) for j in range(n))
    return nxt


def bit_observable(idx: int) -> Observable:
    """Observable = state bit at index ``idx``."""

    def f(st: State) -> float:
        return float(st[idx])

    return f


def parity_observable(idxs: Sequence[int]) -> Observable:
    """Observable = XOR of the named bits."""

    def f(st: State) -> float:
        v = 0
        for i in idxs:
            v ^= int(st[i])
        return float(v)

    return f


def uniform_ensemble(n: int) -> list[State]:
    """Every state in {0,1}^n once (uniform discrete measure)."""
    return [tuple((s >> i) & 1 for i in range(n)) for s in range(2**n)]


def sample_ensemble(n: int, k: int, rng: random.Random) -> list[State]:
    """``k`` i.i.d. uniform starts (with replacement)."""
    out = []
    for _ in range(k):
        s = rng.randrange(2**n)
        out.append(tuple((s >> i) & 1 for i in range(n)))
    return out


def ensemble_mean(observable: Observable, ensemble: Sequence[State]) -> float:
    if not ensemble:
        return float("nan")
    return sum(observable(st) for st in ensemble) / float(len(ensemble))


def _step(nxt: NextMap, state: State, noise: float, rng: random.Random) -> State:
    """One map step; with probability ``noise``, flip a random bit of the image."""
    nxt_st = nxt[state]
    if noise <= 0.0 or rng.random() >= noise:
        return nxt_st
    n = len(nxt_st)
    bit = rng.randrange(n)
    flipped = list(nxt_st)
    flipped[bit] = 1 - flipped[bit]
    return tuple(flipped)


def trajectory_time_average(
    nxt: NextMap,
    start: State,
    observable: Observable,
    horizon: int = DEFAULT_HORIZON,
    noise: float = 0.0,
    rng: Optional[random.Random] = None,
) -> float:
    """Time average of ``observable`` along a length-``horizon`` trajectory.

    Deterministic (noise=0) path: walk until a previously seen state (cycle
    entry), then append one full period, then truncate/pad to ``horizon``
    samples so finite-T comparisons are honest across forms. Noisy path:
    always take exactly ``horizon`` steps under flip noise.
    """
    rng = rng or random.Random(0)
    if noise > 0.0:
        cur = start
        total = observable(cur)
        for _ in range(horizon - 1):
            cur = _step(nxt, cur, noise, rng)
            total += observable(cur)
        return total / float(horizon)

    # Deterministic: burn-in + one cycle, then clip to horizon.
    cur = start
    seen: dict[State, int] = {}
    path: list[State] = []
    t = 0
    while cur not in seen and t < horizon:
        seen[cur] = t
        path.append(cur)
        cur = nxt[cur]
        t += 1
    if cur in seen:
        cycle = path[seen[cur] :]
        series = path + cycle
    else:
        series = path
    if not series:
        return 0.0
    if len(series) > horizon:
        series = series[:horizon]
    elif len(series) < horizon:
        # Pad by repeating the attracting cycle (or last state) so T is fixed.
        if cur in seen and path:
            cyc = path[seen[cur] :]
            while len(series) < horizon:
                series = series + cyc
            series = series[:horizon]
        else:
            last = series[-1]
            series = series + [last] * (horizon - len(series))
    return sum(observable(st) for st in series) / float(len(series))


def run_eoa(
    form: Union[NextMap, Rules],
    observable: Observable,
    *,
    ensemble: Optional[Sequence[State]] = None,
    horizon: int = DEFAULT_HORIZON,
    noise: float = 0.0,
    eps_div: float = DEFAULT_EPS_DIV,
    fail_rate_thresh: float = DEFAULT_FAIL_RATE_THRESH,
    n: Optional[int] = None,
    seed: int = 0,
    observable_name: str = "f",
    ensemble_mean_value: Optional[float] = None,
) -> EoAResult:
    """Run the EoA instrument.

    ``form`` may be a next-map ``dict[state→state]`` or a list of Boolean
    rules. ``ensemble`` defaults to the full uniform state space. When
    ``ensemble_mean_value`` is supplied it overrides the empirical ensemble
    mean (use for a theoretically fixed reference measure).
    """
    if isinstance(form, dict):
        nxt = form
        if n is None:
            n = len(next(iter(nxt.keys())))
    else:
        nxt = rules_to_next_map(form, n=n)
        n = len(form) if n is None else n

    if ensemble is None:
        ens = uniform_ensemble(n)
    else:
        ens = list(ensemble)

    ens_mean = (
        float(ensemble_mean_value)
        if ensemble_mean_value is not None
        else ensemble_mean(observable, ens)
    )

    rng = random.Random(seed)
    gaps: list[float] = []
    n_fail = 0
    for start in ens:
        # Independent RNG stream per start for noisy runs; deterministic ignores it.
        local = random.Random(rng.randrange(2**31 - 1))
        t_avg = trajectory_time_average(
            nxt, start, observable, horizon=horizon, noise=noise, rng=local
        )
        gap = abs(t_avg - ens_mean)
        gaps.append(gap)
        if gap > eps_div:
            n_fail += 1

    n_traj = len(gaps)
    fail_rate = n_fail / float(n_traj) if n_traj else float("nan")
    gap_mean = sum(gaps) / float(n_traj) if n_traj else float("nan")
    if n_traj > 1:
        var = sum((g - gap_mean) ** 2 for g in gaps) / float(n_traj - 1)
        gap_std = math.sqrt(var)
        gap_se = gap_std / math.sqrt(n_traj)
    else:
        gap_std = 0.0
        gap_se = 0.0

    verdict = "BREAKING" if fail_rate >= fail_rate_thresh else "AGREEING"
    return EoAResult(
        verdict=verdict,
        fail_rate=fail_rate,
        gap_mean=gap_mean,
        gap_std=gap_std,
        gap_se=gap_se,
        ensemble_mean=ens_mean,
        n_trajectories=n_traj,
        n_fail=n_fail,
        eps_div=eps_div,
        fail_rate_thresh=fail_rate_thresh,
        horizon=horizon,
        noise=noise,
        observable_name=observable_name,
    )


def run_eoa_parties(
    form: Union[NextMap, Rules],
    party_indices: Sequence[int],
    *,
    labels: Optional[Sequence[str]] = None,
    ensemble: Optional[Sequence[State]] = None,
    horizon: int = DEFAULT_HORIZON,
    noise: float = 0.0,
    eps_div: float = DEFAULT_EPS_DIV,
    fail_rate_thresh: float = DEFAULT_FAIL_RATE_THRESH,
    n: Optional[int] = None,
    seed: int = 0,
) -> EoAResult:
    """EoA pooled over several party-bit observables (G2-style).

    Each (start, party) cell is one trajectory cell. Fail rate is the
    fraction of cells with |gap| > ε_div. Verdict uses the same τ.
    """
    if isinstance(form, dict):
        nxt = form
        if n is None:
            n = len(next(iter(nxt.keys())))
    else:
        nxt = rules_to_next_map(form, n=n)
        n = len(form) if n is None else n

    if ensemble is None:
        ens = uniform_ensemble(n)
    else:
        ens = list(ensemble)

    rng = random.Random(seed)
    gaps: list[float] = []
    n_fail = 0
    for start in ens:
        for idx in party_indices:
            name = labels[idx] if labels else str(idx)
            obs = bit_observable(idx)
            # Ensemble mean of a bit under uniform-on-X is 0.5; under a
            # restricted ensemble, compute empirically.
            ens_mean = ensemble_mean(obs, ens)
            local = random.Random(rng.randrange(2**31 - 1))
            t_avg = trajectory_time_average(
                nxt, start, obs, horizon=horizon, noise=noise, rng=local
            )
            gap = abs(t_avg - ens_mean)
            gaps.append(gap)
            if gap > eps_div:
                n_fail += 1

    n_traj = len(gaps)
    fail_rate = n_fail / float(n_traj) if n_traj else float("nan")
    gap_mean = sum(gaps) / float(n_traj) if n_traj else float("nan")
    if n_traj > 1:
        var = sum((g - gap_mean) ** 2 for g in gaps) / float(n_traj - 1)
        gap_std = math.sqrt(var)
        gap_se = gap_std / math.sqrt(n_traj)
    else:
        gap_std = 0.0
        gap_se = 0.0

    obs_name = (
        "{" + ",".join(labels[i] if labels else str(i) for i in party_indices) + "}"
    )
    verdict = "BREAKING" if fail_rate >= fail_rate_thresh else "AGREEING"
    # Ensemble mean is not a single scalar when pooling bits; report 0.5 when
    # the ensemble is the full uniform space (standard G2 reference).
    ens_mean_report = 0.5 if len(ens) == 2**n else float("nan")
    return EoAResult(
        verdict=verdict,
        fail_rate=fail_rate,
        gap_mean=gap_mean,
        gap_std=gap_std,
        gap_se=gap_se,
        ensemble_mean=ens_mean_report,
        n_trajectories=n_traj,
        n_fail=n_fail,
        eps_div=eps_div,
        fail_rate_thresh=fail_rate_thresh,
        horizon=horizon,
        noise=noise,
        observable_name=obs_name,
    )


def agrees_with_phi(eoa_verdict: str, phi_structure: str) -> bool:
    """Agreement rule: BREAKING ↔ triadic; AGREEING ↔ dyadic."""
    return (eoa_verdict == "BREAKING" and phi_structure == "triadic") or (
        eoa_verdict == "AGREEING" and phi_structure == "dyadic"
    )


# ---------------------------------------------------------------------------
# Known-answer control forms (no Φ; unit-test fixtures)
# ---------------------------------------------------------------------------

def control_full_cycle_n3() -> NextMap:
    """Single 8-cycle through every 3-bit state (fully mixing on X).

    Gray-like Hamiltonian cycle. Every trajectory eventually traverses the
    same cycle; bit-0 occupancy on the cycle is exactly 1/2, matching the
    uniform ensemble mean — so EoA AGREEING for bit 0 under uniform starts.
    """
    order = [
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (0, 1, 0),
        (0, 1, 1),
        (1, 1, 1),
        (1, 0, 1),
        (0, 0, 1),
    ]
    nxt: NextMap = {}
    for i, st in enumerate(order):
        nxt[st] = order[(i + 1) % len(order)]
    return nxt


def control_two_absorbing() -> Rules:
    """Two absorbing fixed points 000 and 111; everything else drains in.

    maj3 map — two absorbing states with polarized bit observables. Mixed
    uniform starts ⇒ EoA BREAKING for party bits.
    """

    def maj(x: State) -> int:
        return 1 if (x[0] + x[1] + x[2]) >= 2 else 0

    return [maj, maj, maj]


def control_identity_single() -> Rules:
    """Identity map: every state is a fixed point (2^n attractors).

    Singleton ensemble on one state ⇒ AGREEING for any bit; full mixed
    ensemble ⇒ BREAKING (time avg = start bit, ensemble = 0.5).
    """
    return [lambda x: x[0], lambda x: x[1], lambda x: x[2]]
