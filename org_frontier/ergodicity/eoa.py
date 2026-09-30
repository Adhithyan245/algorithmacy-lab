"""Equality-of-Averages (EoA) instrument for Boolean coordination forms.

Reusable Strand-G tooling. Given a finite Boolean next-map (or per-party
rules), an observable, an initial-state ensemble, a horizon T, and an
optional flip-noise level, returns a time-vs-ensemble gap statistic with
an uncertainty estimate and a binary verdict:

    AGREEING  — fail rate < τ  (ergodic-agreeing under the reference measure)
    BREAKING  — fail rate ≥ τ  (EoA-breaking)

Reference modes (``reference_mode``):

    uniform     — one global ensemble mean of f on starts (legacy default;
                  matches G2 / ``ergodic_eoa_instrument``).
    basin       — each trajectory compared to the mean of time averages
                  among ensemble starts in the same zero-noise basin
                  (clears cross-basin polarization false positives).
    stationary  — each trajectory compared to ∫f dμ on the attractor it
                  reaches (uniform on the deterministic cycle; unique
                  stationary of the flip-noise chain when noise > 0).

Decision thresholds ``ε_div`` and ``τ`` are arguments; studies that use this
instrument must freeze them in a hypotheses file *before* the stress run.
Default values match G2 / ``ergodic_eoa_instrument``: ε_div=0.1, τ=0.25.

No Φ computation lives here. Pair with ``classify_rules`` / ``whole_verdict``
when comparing to the literacy / algorithmacy cut.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Callable, Optional, Sequence, Union

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

REFERENCE_UNIFORM = "uniform"
REFERENCE_BASIN = "basin"
REFERENCE_STATIONARY = "stationary"
REFERENCE_MODES = (REFERENCE_UNIFORM, REFERENCE_BASIN, REFERENCE_STATIONARY)


@dataclass(frozen=True)
class EoAResult:
    """Instrument output for one (form, observable, ensemble, T, noise) cell."""

    verdict: str                 # "AGREEING" | "BREAKING"
    fail_rate: float
    gap_mean: float              # mean |time_avg − reference|
    gap_std: float               # sample std of per-trajectory gaps
    gap_se: float                # gap_std / sqrt(n)
    ensemble_mean: float         # reported reference (mode-dependent)
    n_trajectories: int
    n_fail: int
    eps_div: float
    fail_rate_thresh: float
    horizon: int
    noise: float
    observable_name: str
    reference_mode: str = REFERENCE_UNIFORM

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


# ---------------------------------------------------------------------------
# Basin / attractor reference helpers (no Φ)
# ---------------------------------------------------------------------------

def attractor_partition(nxt: NextMap) -> dict:
    """Zero-noise attractor partition of a finite deterministic next-map.

    Returns dict with:
      cycles: list of cycle tuples (canonical rotation)
      basin_of: state → cycle index
      basin_states: cycle index → frozenset of states draining to that cycle
      cycle_of_state: state → the cycle tuple it reaches
    """
    cycle_key_of: dict[State, frozenset] = {}
    cycles_by_key: dict[frozenset, tuple] = {}
    states = list(nxt.keys())
    for start_state in states:
        cur = start_state
        path: list[State] = []
        vis: dict[State, int] = {}
        while cur not in vis:
            if cur in cycle_key_of:
                break
            vis[cur] = len(path)
            path.append(cur)
            cur = nxt[cur]
        if cur in vis:
            cyc = tuple(path[vis[cur] :])
            key = frozenset(cyc)
            cyc_c = min(tuple(cyc[i:] + cyc[:i]) for i in range(len(cyc)))
            cycles_by_key[key] = cyc_c
            for st in cyc:
                cycle_key_of[st] = key

    # Map every state to its cycle key via forward walk.
    for start_state in states:
        if start_state in cycle_key_of:
            continue
        cur = start_state
        visited: set[State] = set()
        while cur not in visited:
            if cur in cycle_key_of:
                break
            visited.add(cur)
            cur = nxt[cur]
        key = cycle_key_of[cur]
        for st in visited:
            cycle_key_of[st] = key

    keys = list(cycles_by_key.keys())
    key_to_idx = {k: i for i, k in enumerate(keys)}
    cycles = [cycles_by_key[k] for k in keys]
    basin_of = {st: key_to_idx[cycle_key_of[st]] for st in states}
    basin_states: dict[int, set] = {i: set() for i in range(len(keys))}
    for st, idx in basin_of.items():
        basin_states[idx].add(st)
    cycle_of_state = {
        st: cycles[basin_of[st]] for st in states
    }
    return {
        "cycles": cycles,
        "basin_of": basin_of,
        "basin_states": {i: frozenset(s) for i, s in basin_states.items()},
        "cycle_of_state": cycle_of_state,
    }


def cycle_mean(observable: Observable, cycle: Sequence[State]) -> float:
    """Uniform mean of ``observable`` on a deterministic cycle."""
    if not cycle:
        return float("nan")
    return sum(observable(st) for st in cycle) / float(len(cycle))


def noisy_transition_matrix(nxt: NextMap, noise: float) -> list[list[float]]:
    """Row-stochastic matrix for one step of ``nxt`` with bit-flip noise.

    With prob 1−noise: follow the deterministic image. With prob noise:
    flip exactly one uniformly chosen bit of the image.
    """
    states = list(nxt.keys())
    n = len(states[0])
    index = {st: i for i, st in enumerate(states)}
    m = len(states)
    P = [[0.0] * m for _ in range(m)]
    for st in states:
        i = index[st]
        img = nxt[st]
        if noise <= 0.0:
            P[i][index[img]] = 1.0
            continue
        P[i][index[img]] += 1.0 - noise
        for bit in range(n):
            flipped = list(img)
            flipped[bit] = 1 - flipped[bit]
            j = index[tuple(flipped)]
            P[i][j] += noise / float(n)
    return P


def stationary_distribution(P: Sequence[Sequence[float]], tol: float = 1e-12) -> list[float]:
    """Unique stationary distribution of a finite irreducible chain (power iter).

    Falls back to the normalized left-eigenvector via iterative multiply
    starting from uniform; adequate for small Boolean state spaces.
    """
    m = len(P)
    if m == 0:
        return []
    pi = [1.0 / m] * m
    for _ in range(10000):
        nxt = [0.0] * m
        for i in range(m):
            pi_i = pi[i]
            row = P[i]
            for j in range(m):
                nxt[j] += pi_i * row[j]
        diff = sum(abs(nxt[j] - pi[j]) for j in range(m))
        pi = nxt
        s = sum(pi)
        if s <= 0:
            return [1.0 / m] * m
        pi = [x / s for x in pi]
        if diff < tol:
            break
    return pi


def stationary_mean(
    observable: Observable,
    nxt: NextMap,
    noise: float = 0.0,
) -> float:
    """Mean of ``observable`` under the chain's stationary distribution."""
    states = list(nxt.keys())
    if noise <= 0.0:
        # Mixture of attractor measures weighted by basin mass (not used as
        # per-trajectory reference; callers prefer per-attractor cycle means).
        part = attractor_partition(nxt)
        total = 0.0
        for idx, cyc in enumerate(part["cycles"]):
            mass = len(part["basin_states"][idx]) / float(len(states))
            total += mass * cycle_mean(observable, cyc)
        return total
    P = noisy_transition_matrix(nxt, noise)
    pi = stationary_distribution(P)
    return sum(pi[i] * observable(states[i]) for i in range(len(states)))


def _summarize_gaps(
    gaps: list[float],
    *,
    eps_div: float,
    fail_rate_thresh: float,
    horizon: int,
    noise: float,
    observable_name: str,
    ensemble_mean: float,
    reference_mode: str,
) -> EoAResult:
    n_traj = len(gaps)
    n_fail = sum(1 for g in gaps if g > eps_div)
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
        ensemble_mean=ensemble_mean,
        n_trajectories=n_traj,
        n_fail=n_fail,
        eps_div=eps_div,
        fail_rate_thresh=fail_rate_thresh,
        horizon=horizon,
        noise=noise,
        observable_name=observable_name,
        reference_mode=reference_mode,
    )


def _resolve_form(
    form: Union[NextMap, Rules], n: Optional[int]
) -> tuple[NextMap, int]:
    if isinstance(form, dict):
        nxt = form
        if n is None:
            n = len(next(iter(nxt.keys())))
        return nxt, n
    nxt = rules_to_next_map(form, n=n)
    n_out = len(form) if n is None else n
    return nxt, n_out


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
    reference_mode: str = REFERENCE_UNIFORM,
) -> EoAResult:
    """Run the EoA instrument.

    ``form`` may be a next-map ``dict[state→state]`` or a list of Boolean
    rules. ``ensemble`` defaults to the full uniform state space. When
    ``ensemble_mean_value`` is supplied under ``reference_mode='uniform'``
    it overrides the empirical ensemble mean (theoretically fixed
    reference). ``reference_mode`` selects uniform / basin / stationary
    (see module docstring).
    """
    if reference_mode not in REFERENCE_MODES:
        raise ValueError(
            f"reference_mode must be one of {REFERENCE_MODES}, got {reference_mode!r}"
        )
    nxt, n = _resolve_form(form, n)
    ens = uniform_ensemble(n) if ensemble is None else list(ensemble)
    rng = random.Random(seed)

    # Per-start time averages (shared across modes).
    t_avgs: list[float] = []
    for start in ens:
        local = random.Random(rng.randrange(2**31 - 1))
        t_avgs.append(
            trajectory_time_average(
                nxt, start, observable, horizon=horizon, noise=noise, rng=local
            )
        )

    if reference_mode == REFERENCE_UNIFORM:
        ens_mean = (
            float(ensemble_mean_value)
            if ensemble_mean_value is not None
            else ensemble_mean(observable, ens)
        )
        gaps = [abs(t - ens_mean) for t in t_avgs]
        return _summarize_gaps(
            gaps,
            eps_div=eps_div,
            fail_rate_thresh=fail_rate_thresh,
            horizon=horizon,
            noise=noise,
            observable_name=observable_name,
            ensemble_mean=ens_mean,
            reference_mode=reference_mode,
        )

    part = attractor_partition(nxt)

    if reference_mode == REFERENCE_BASIN:
        # Reference = mean of time averages among starts in the same basin.
        basin_buckets: dict[int, list[float]] = {}
        basin_ids = [part["basin_of"][s] for s in ens]
        for bid, t in zip(basin_ids, t_avgs):
            basin_buckets.setdefault(bid, []).append(t)
        basin_ref = {bid: sum(vs) / len(vs) for bid, vs in basin_buckets.items()}
        gaps = [abs(t - basin_ref[bid]) for t, bid in zip(t_avgs, basin_ids)]
        # Report the mean absolute deviation from per-basin refs as the
        # scalar "ensemble_mean" stand-in is not a single number; use the
        # average of basin references weighted by basin start counts.
        report = sum(
            basin_ref[bid] * len(vs) for bid, vs in basin_buckets.items()
        ) / float(len(ens))
        return _summarize_gaps(
            gaps,
            eps_div=eps_div,
            fail_rate_thresh=fail_rate_thresh,
            horizon=horizon,
            noise=noise,
            observable_name=observable_name,
            ensemble_mean=report,
            reference_mode=reference_mode,
        )

    # stationary
    if noise > 0.0:
        ref = stationary_mean(observable, nxt, noise=noise)
        gaps = [abs(t - ref) for t in t_avgs]
        return _summarize_gaps(
            gaps,
            eps_div=eps_div,
            fail_rate_thresh=fail_rate_thresh,
            horizon=horizon,
            noise=noise,
            observable_name=observable_name,
            ensemble_mean=ref,
            reference_mode=reference_mode,
        )
    gaps = []
    refs = []
    for start, t in zip(ens, t_avgs):
        cyc = part["cycle_of_state"][start]
        ref = cycle_mean(observable, cyc)
        refs.append(ref)
        gaps.append(abs(t - ref))
    report = sum(refs) / float(len(refs)) if refs else float("nan")
    return _summarize_gaps(
        gaps,
        eps_div=eps_div,
        fail_rate_thresh=fail_rate_thresh,
        horizon=horizon,
        noise=noise,
        observable_name=observable_name,
        ensemble_mean=report,
        reference_mode=reference_mode,
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
    reference_mode: str = REFERENCE_UNIFORM,
) -> EoAResult:
    """EoA pooled over several party-bit observables (G2-style).

    Each (start, party) cell is one trajectory cell. Fail rate is the
    fraction of cells with |gap| > ε_div. Verdict uses the same τ.
    ``reference_mode`` is applied per party observable.
    """
    if reference_mode not in REFERENCE_MODES:
        raise ValueError(
            f"reference_mode must be one of {REFERENCE_MODES}, got {reference_mode!r}"
        )
    nxt, n = _resolve_form(form, n)
    ens = uniform_ensemble(n) if ensemble is None else list(ensemble)

    gaps: list[float] = []
    rng = random.Random(seed)
    part = (
        attractor_partition(nxt)
        if reference_mode in (REFERENCE_BASIN, REFERENCE_STATIONARY)
        else None
    )
    # Precompute per-party time averages and references.
    for idx in party_indices:
        obs = bit_observable(idx)
        t_avgs = []
        for start in ens:
            local = random.Random(rng.randrange(2**31 - 1))
            t_avgs.append(
                trajectory_time_average(
                    nxt, start, obs, horizon=horizon, noise=noise, rng=local
                )
            )
        if reference_mode == REFERENCE_UNIFORM:
            ens_mean = ensemble_mean(obs, ens)
            for t in t_avgs:
                gaps.append(abs(t - ens_mean))
        elif reference_mode == REFERENCE_BASIN:
            assert part is not None
            basin_ids = [part["basin_of"][s] for s in ens]
            buckets: dict[int, list[float]] = {}
            for bid, t in zip(basin_ids, t_avgs):
                buckets.setdefault(bid, []).append(t)
            refs = {bid: sum(vs) / len(vs) for bid, vs in buckets.items()}
            for t, bid in zip(t_avgs, basin_ids):
                gaps.append(abs(t - refs[bid]))
        else:  # stationary
            assert part is not None
            if noise > 0.0:
                ref = stationary_mean(obs, nxt, noise=noise)
                for t in t_avgs:
                    gaps.append(abs(t - ref))
            else:
                for start, t in zip(ens, t_avgs):
                    cyc = part["cycle_of_state"][start]
                    gaps.append(abs(t - cycle_mean(obs, cyc)))

    obs_name = (
        "{" + ",".join(labels[i] if labels else str(i) for i in party_indices) + "}"
    )
    # Ensemble mean is not a single scalar when pooling bits; report 0.5 when
    # the ensemble is the full uniform space under uniform mode (G2).
    if reference_mode == REFERENCE_UNIFORM and len(ens) == 2**n:
        ens_mean_report = 0.5
    else:
        ens_mean_report = float("nan")
    return _summarize_gaps(
        gaps,
        eps_div=eps_div,
        fail_rate_thresh=fail_rate_thresh,
        horizon=horizon,
        noise=noise,
        observable_name=obs_name,
        ensemble_mean=ens_mean_report,
        reference_mode=reference_mode,
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
