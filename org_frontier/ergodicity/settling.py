"""Settling-time measures for Boolean coordination forms (Strand G follow-on).

Reusable diagnostics that ask whether a form's residual Equality-of-Averages
gap under a basin-restricted reference is a finite-T burn-in effect rather
than ergodicity-breaking. No Φ computation lives here.

Measures (definitions frozen by studies that import them):

(a) **Transient length** — steps from a start until the trajectory first
    lands on its attractor cycle. Per-form summaries over an ensemble:
    mean, max, and basin-mass-weighted mean of per-basin means.

(b) **Time-average convergence T** — smallest horizon T at which the
    cumulative time average of a party observable lies within ε of the
    uniform mean on the attractor the start reaches. Reported as the
    mean / max over (start × party) cells.

(c) **Noisy-chain relaxation** — under flip noise ε_flip > 0, the
    spectral gap of the row-stochastic TPM and the implied relaxation
    time 1/gap (independent of the deterministic basin partition).

Covariates recorded alongside: attractor periods, number of attractors,
state-space size.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import Optional, Sequence, Union

import math

from org_frontier.ergodicity.eoa import (
    NextMap,
    Observable,
    Rules,
    State,
    attractor_partition,
    bit_observable,
    cycle_mean,
    noisy_transition_matrix,
    rules_to_next_map,
    uniform_ensemble,
)

# Frozen defaults for studies; override only under pre-registration.
DEFAULT_EPS_CONV = 0.01
DEFAULT_T_MAX = 256
DEFAULT_EPS_FLIP = 0.05
DEFAULT_TV_DELTA = 0.25


@dataclass(frozen=True)
class TransientSummary:
    """Per-form transient-length summary over an ensemble of starts."""

    mean: float
    max: float
    basin_weighted_mean: float
    n_starts: int
    n_attractors: int
    mean_period: float
    max_period: int
    state_space_size: int
    # Optional per-start lengths (omitted from CSV dumps when empty).
    lengths: tuple = field(default=(), repr=False)

    def to_dict(self) -> dict:
        d = asdict(self)
        d.pop("lengths", None)
        return d


@dataclass(frozen=True)
class ConvergenceSummary:
    """Per-form time-average convergence summary over (start × party) cells."""

    mean_T: float
    max_T: float
    median_T: float
    n_cells: int
    n_unresolved: int  # cells that never entered the ε-ball by T_max
    eps_conv: float
    t_max: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class MixingSummary:
    """Spectral gap / relaxation time of the flip-noise chain."""

    spectral_gap: float
    relaxation_time: float
    tv_mixing_bound: float  # ceil(log(1/δ) / gap); inf if gap=0
    eps_flip: float
    tv_delta: float
    n_states: int

    def to_dict(self) -> dict:
        return asdict(self)


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


def transient_length(nxt: NextMap, start: State) -> int:
    """Steps from ``start`` until the trajectory first enters its cycle.

    Walks the deterministic map, recording first-visit times. When a
    previously seen state reappears, the cycle begins at that visit; the
    transient length is the index of the first cycle state (0 if ``start``
    already lies on the cycle). Caps at ``len(nxt)`` (finite maps always
    enter a cycle by then).
    """
    cur = start
    seen: dict[State, int] = {}
    t = 0
    limit = len(nxt)
    while cur not in seen and t <= limit:
        seen[cur] = t
        cur = nxt[cur]
        t += 1
    if cur not in seen:
        # Should not happen on a total finite map; treat path as all transient.
        return t
    return seen[cur]


def summarize_transients(
    form: Union[NextMap, Rules],
    *,
    ensemble: Optional[Sequence[State]] = None,
    n: Optional[int] = None,
) -> TransientSummary:
    """Mean / max / basin-weighted mean transient length over an ensemble.

    Basin-weighted mean: for each attractor basin, take the mean transient
    of ensemble starts that drain to it, then average those basin means
    weighted by the number of ensemble starts in the basin. On the full
    uniform state space this equals the ordinary mean; it remains well-
    defined for subsampled ensembles.
    """
    nxt, n = _resolve_form(form, n)
    ens = uniform_ensemble(n) if ensemble is None else list(ensemble)
    part = attractor_partition(nxt)
    lengths = [transient_length(nxt, s) for s in ens]
    if not lengths:
        return TransientSummary(
            mean=float("nan"),
            max=float("nan"),
            basin_weighted_mean=float("nan"),
            n_starts=0,
            n_attractors=len(part["cycles"]),
            mean_period=float("nan"),
            max_period=0,
            state_space_size=len(nxt),
            lengths=(),
        )
    mean = sum(lengths) / float(len(lengths))
    mx = float(max(lengths))
    # Basin-weighted mean of per-basin means.
    buckets: dict[int, list[int]] = {}
    for s, L in zip(ens, lengths):
        buckets.setdefault(part["basin_of"][s], []).append(L)
    weighted = 0.0
    for vs in buckets.values():
        weighted += (sum(vs) / float(len(vs))) * len(vs)
    basin_w = weighted / float(len(ens))
    periods = [len(c) for c in part["cycles"]]
    # Basin-mass-weighted mean period over the ensemble.
    period_sum = 0.0
    for s in ens:
        period_sum += len(part["cycle_of_state"][s])
    mean_period = period_sum / float(len(ens))
    return TransientSummary(
        mean=mean,
        max=mx,
        basin_weighted_mean=basin_w,
        n_starts=len(ens),
        n_attractors=len(part["cycles"]),
        mean_period=mean_period,
        max_period=max(periods) if periods else 0,
        state_space_size=len(nxt),
        lengths=tuple(lengths),
    )


def time_avg_prefix(
    nxt: NextMap,
    start: State,
    observable: Observable,
    horizon: int,
) -> list[float]:
    """Cumulative time averages of ``observable`` for T = 1..horizon.

    Index 0 is the average after 1 sample (the start); index k−1 is the
    average of the first k states on the deterministic trajectory
    (transient then cycling). Trajectories longer than the state space
    wrap on the attracting cycle.
    """
    if horizon < 1:
        return []
    # Build a long enough series: transient + enough cycle repeats.
    cur = start
    seen: dict[State, int] = {}
    path: list[State] = []
    t = 0
    limit = max(horizon, len(nxt) + 1)
    while cur not in seen and t < limit:
        seen[cur] = t
        path.append(cur)
        cur = nxt[cur]
        t += 1
    if cur in seen and path:
        cycle = path[seen[cur] :]
        series = list(path)
        while len(series) < horizon:
            series.extend(cycle)
        series = series[:horizon]
    else:
        series = path[:horizon]
        if not series:
            return []
        while len(series) < horizon:
            series.append(series[-1])
    out: list[float] = []
    total = 0.0
    for i, st in enumerate(series):
        total += observable(st)
        out.append(total / float(i + 1))
    return out


def convergence_time(
    nxt: NextMap,
    start: State,
    observable: Observable,
    *,
    eps_conv: float = DEFAULT_EPS_CONV,
    t_max: int = DEFAULT_T_MAX,
    attractor_mean: Optional[float] = None,
) -> int:
    """Smallest T ∈ {1..t_max} with |Ā_T − μ| < ε_conv; else t_max + 1.

    μ is the uniform mean of ``observable`` on the attractor cycle that
    ``start`` reaches, unless ``attractor_mean`` is supplied. Returning
    ``t_max + 1`` marks unresolved cells (never entered the ε-ball).
    """
    if attractor_mean is None:
        part = attractor_partition(nxt)
        attractor_mean = cycle_mean(observable, part["cycle_of_state"][start])
    avgs = time_avg_prefix(nxt, start, observable, t_max)
    for t, a in enumerate(avgs, start=1):
        if abs(a - attractor_mean) < eps_conv:
            return t
    return t_max + 1


def summarize_convergence(
    form: Union[NextMap, Rules],
    party_indices: Sequence[int],
    *,
    ensemble: Optional[Sequence[State]] = None,
    n: Optional[int] = None,
    eps_conv: float = DEFAULT_EPS_CONV,
    t_max: int = DEFAULT_T_MAX,
) -> ConvergenceSummary:
    """Mean / max / median convergence T over (start × party) cells."""
    nxt, n = _resolve_form(form, n)
    ens = uniform_ensemble(n) if ensemble is None else list(ensemble)
    part = attractor_partition(nxt)
    times: list[int] = []
    for idx in party_indices:
        obs = bit_observable(idx)
        # Cache cycle means per attractor index.
        cyc_means = {
            i: cycle_mean(obs, cyc) for i, cyc in enumerate(part["cycles"])
        }
        for start in ens:
            bid = part["basin_of"][start]
            T = convergence_time(
                nxt,
                start,
                obs,
                eps_conv=eps_conv,
                t_max=t_max,
                attractor_mean=cyc_means[bid],
            )
            times.append(T)
    if not times:
        return ConvergenceSummary(
            mean_T=float("nan"),
            max_T=float("nan"),
            median_T=float("nan"),
            n_cells=0,
            n_unresolved=0,
            eps_conv=eps_conv,
            t_max=t_max,
        )
    n_unresolved = sum(1 for T in times if T > t_max)
    srt = sorted(times)
    m = len(srt)
    if m % 2 == 1:
        med = float(srt[m // 2])
    else:
        med = 0.5 * (srt[m // 2 - 1] + srt[m // 2])
    return ConvergenceSummary(
        mean_T=sum(times) / float(len(times)),
        max_T=float(max(times)),
        median_T=med,
        n_cells=len(times),
        n_unresolved=n_unresolved,
        eps_conv=eps_conv,
        t_max=t_max,
    )


def spectral_gap(P: Sequence[Sequence[float]]) -> float:
    """1 − |λ₂| for a row-stochastic matrix (numpy eigvals).

    Returns 0.0 when the chain is not uniquely mixing (gap numerically
    ≤ 0) or when the state space is empty / singleton (trivial gap = 1
    for a 1×1 matrix — returned as 1.0).
    """
    import numpy as np

    m = len(P)
    if m == 0:
        return float("nan")
    if m == 1:
        return 1.0
    A = np.asarray(P, dtype=float)
    # Right eigenvalues of row-stochastic P; λ₁ = 1.
    w = np.linalg.eigvals(A)
    # Sort by descending magnitude.
    mags = sorted((abs(complex(z)) for z in w), reverse=True)
    lam2 = mags[1] if len(mags) > 1 else 0.0
    gap = 1.0 - float(lam2)
    # Numerical floor: gaps below 1e-10 are treated as 0 (reducible /
    # non-mixing under float64 eigendecomposition of small Boolean TPMs).
    if gap < 1e-10:
        gap = 0.0
    return gap


def relaxation_time_from_gap(gap: float) -> float:
    """1 / spectral_gap; +inf when gap is 0."""
    if gap <= 0.0 or math.isnan(gap):
        return float("inf")
    return 1.0 / gap


def tv_mixing_bound(gap: float, delta: float = DEFAULT_TV_DELTA) -> float:
    """Crude spectral mixing bound ⌈ln(1/δ) / gap⌉; +inf when gap=0."""
    if gap <= 0.0 or math.isnan(gap):
        return float("inf")
    if delta <= 0.0 or delta >= 1.0:
        raise ValueError("delta must lie in (0, 1)")
    return math.ceil(math.log(1.0 / delta) / gap)


def summarize_mixing(
    form: Union[NextMap, Rules],
    *,
    eps_flip: float = DEFAULT_EPS_FLIP,
    tv_delta: float = DEFAULT_TV_DELTA,
    n: Optional[int] = None,
) -> MixingSummary:
    """Spectral gap and relaxation time of the flip-noise chain."""
    if eps_flip <= 0.0:
        raise ValueError("eps_flip must be > 0 for a mixing chain")
    nxt, _ = _resolve_form(form, n)
    P = noisy_transition_matrix(nxt, eps_flip)
    gap = spectral_gap(P)
    rel = relaxation_time_from_gap(gap)
    bound = tv_mixing_bound(gap, tv_delta)
    return MixingSummary(
        spectral_gap=gap,
        relaxation_time=rel,
        tv_mixing_bound=bound,
        eps_flip=eps_flip,
        tv_delta=tv_delta,
        n_states=len(nxt),
    )


# ---------------------------------------------------------------------------
# Known-answer control maps (no Φ; unit-test fixtures)
# ---------------------------------------------------------------------------

def control_chain_to_fixed() -> NextMap:
    """3-bit map: Gray-like drain into the fixed point 000.

    Explicit next-map (not maj3): every nonzero state flips its lowest
    set bit off, so the unique attractor is {(0,0,0)} and transient
    lengths are exactly the Hamming weights::

        000 → 000  (transient 0)
        100 → 000  (1)
        010 → 000  (1)
        001 → 000  (1)
        110 → 010 → 000  (2)
        101 → 001 → 000  (2)
        011 → 001 → 000  (2)
        111 → 011 → 001 → 000  (3)

    Mean transient over the uniform ensemble = (0+1+1+1+2+2+2+3)/8 = 1.5.
    """
    nxt: NextMap = {}
    for s in range(8):
        cur = tuple((s >> i) & 1 for i in range(3))
        bits = list(cur)
        for i in range(3):
            if bits[i] == 1:
                bits[i] = 0
                break
        nxt[cur] = tuple(bits)
    return nxt


def control_two_step_cycle() -> NextMap:
    """Unique 2-cycle (000 ↔ 100); all other states drain in one step.

    Transient lengths: 0 on the cycle, 1 elsewhere. Period = 2.
    """
    nxt: NextMap = {
        (0, 0, 0): (1, 0, 0),
        (1, 0, 0): (0, 0, 0),
    }
    for s in range(8):
        cur = tuple((s >> i) & 1 for i in range(3))
        if cur in nxt:
            continue
        # Drain toward 000.
        nxt[cur] = (0, 0, 0)
    return nxt
