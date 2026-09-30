# ergodic_eoa_basin — hypotheses (fixed before computing)

**Question (Strand G / T8 follow-on).** Once Equality-of-Averages stops
conflating multistability with irreducibility — by comparing each
trajectory to a basin-restricted or attractor-stationary reference
instead of the uniform-on-X ensemble — does the residual BREAKING signal
track whole-form Φ_MIP at all?

**Already known (cited, not reopened).**
- G2 (`studies/ergodic_eoa_vs_phi/`): operational EoA agreed with Φ on 7/9
  forms; both misses dyadic multi-attractor (sticky, maj3).
- Instrument stress (`studies/ergodic_eoa_instrument/`): on the frozen
  42-form panel, agreement 17/42; every form BREAKING (TP=17, FP=25,
  TN=0, FN=0); verdict `EOA_TRACKS_MI_NOT_PHI`. Of 25 misses, 20 were
  dyadic multi-attractor (basin polarization under a uniform ensemble);
  5 were dyadic single-attractor forms whose cycle mean differs from the
  uniform 0.5 reference (ensemble-measure mismatch).
- Derived: on a finite map with ≥2 attractors, EoA vs a mixed ensemble
  fails for generic observables (THEORIES.md T8; Connaughton et al.
  hierarchy). The per-outcome fix asks whether that failure was the
  whole of the Φ association.

**Null stated plainly.** After the fix, EoA may collapse to all-AGREEING
and carry no information about Φ. That is a legitimate result.

**Instrument extension (backward compatible; implemented after this
commit).** Module: `org_frontier/ergodicity/eoa.py`. Keep the prior
`uniform` reference mode unchanged. Add:

- **`basin`** — for each trajectory start, the reference is the mean of
  per-trajectory time averages among ensemble starts that share the same
  (zero-noise) basin of attraction. Equality is tested *within* basin;
  cross-basin polarization is no longer counted as breaking.
- **`stationary`** — for each trajectory, the reference is the mean of
  the observable under the invariant measure on the attractor the start
  reaches (uniform over cycle states when deterministic; the unique
  stationary distribution of the flip-noise chain when `noise > 0`).

Decision thresholds stay frozen from the prior study: `ε_div = 0.1`,
`τ = 0.25`. Primary observables: non-mediator party bits (n=3: `{W,C}`;
n=4: non-`S`). Default horizon `T = 64`. Default noise `ε_flip = 0`.

**Panel (identical freeze to `ergodic_eoa_instrument`).**
1. G2 core (9), classifier library (5), absorbing/ejection (2).
2. Seeded random n=3 (20): seed `20260930`, same 8-gate palette and
   input-pair draw, reject duplicates of named members.
3. n=4 tractable (6): and_pool, or_pool, maj_homog, chain_ws_c1c2,
   hub_s, dual_latch.

Total **42** forms. CI subset: G2 core + classifier + ejection via
`--ci` (no random n=3, no n=4); noise arm deferred under `--ci`.

**Instrument gate.** memoryless triadic Φ=2; sticky dyadic Φ=0. Abort if
fail. Unit-test controls (known answers, no Φ): (a) two absorbing poles
→ AGREEING under `basin`; (b) single full-cycle → AGREEING under
`basin` and under `stationary`; (c) two absorbing poles with flip noise
at finite T → BREAKING under `stationary` (finite-T averages have not
reached the noisy chain's stationary mean).

**Score-based checks (frozen).** Treat EoA gap_mean as a score for
Φ>0: report ROC-AUC of gap_mean vs whole-form triadic, and Spearman rank
correlation of gap_mean with Φ magnitude. Chance AUC = 0.5; chance
Spearman = 0.

## H1 — basin mode removes most dyadic multi-attractor false positives

On the 42-form panel under `reference_mode=basin`, among the forms that
were BREAKING×dyadic×multi-attractor under the prior uniform instrument
(the 20-miss class), the share that become AGREEING is ≥ **0.75**.

Null: that rescue share < 0.75.

## H2 — stationary mode removes the five single-attractor mismatches

On the same panel under `reference_mode=stationary`, among the forms
that were BREAKING×dyadic×single-attractor under the prior uniform
instrument (the 5-miss residue), the share that become AGREEING is
≥ **0.80** (i.e. at least 4 of 5).

Null: rescue share < 0.80.

## H3 — residual BREAKING separates triadic from dyadic (agreement)

Under each of `basin` and `stationary` at noise=0, EoA↔Φ agreement rate
on the 42-form panel is ≥ **0.65**, or a one-sided exact binomial test
of agreement vs p=0.5 at α=0.05.

Null: agreement < 0.65 and binomial p ≥ 0.05. (All-AGREEING collapses
agreement to the dyadic base rate and fails this test — that is the
stated null outcome.)

## H4 — residual gap score carries Φ information

Under each of `basin` and `stationary` at noise=0: ROC-AUC of
`gap_mean` vs whole-form triadic ≥ **0.65**, **or** |Spearman ρ| of
`gap_mean` vs Φ magnitude ≥ **0.30** with a two-sided permutation (or
exact-rank) p < 0.05.

Null: AUC < 0.65 and |ρ| < 0.30 (or p ≥ 0.05). Collapse of every gap
to ~0 fails this test.

## H5 — noise arm can restore a within-basin BREAKING signal

Under `reference_mode=basin`, `ε_flip = 0.05`, `T = 64`, on the G2 core
nine forms: either (a) at least one form that was AGREEING under
basin/noise=0 becomes BREAKING, **or** (b) the G2-core agreement rate
moves by ≥ **0.10** absolute relative to basin/noise=0. This arm asks
whether noise-induced hopping reintroduces a signal; it does not claim
that signal tracks Φ.

Null: no AGREEING→BREAKING flip on the G2 core and |Δ agree| < 0.10.

**Primary verdict word (evaluated on noise=0 basin and stationary).**
- H3 and H4 both hold for at least one of {basin, stationary} →
  `EOA_BASIN_TRACKS_PHI`
- H1 and H2 hold, but neither mode passes H3 or H4 →
  `EOA_FIX_NO_PHI_SIGNAL`
- H1 or H2 fails (fix does not clear its named miss class) →
  `EOA_FIX_INCOMPLETE`
- else → `EOA_BASIN_INCONCLUSIVE`

**Scope.** In-silico Boolean forms only. Evidence about the instrument
and the models; not about real organizations or platforms. No numbers
until `analyze_basin.py` runs after this commit.
