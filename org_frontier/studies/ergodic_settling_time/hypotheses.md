# ergodic_settling_time — hypotheses (fixed before computing)

**Question (Strand G / T8 residual).** Once multistability is conditioned
out, binary basin-mode Equality-of-Averages is all-AGREEING on the frozen
42-form panel, yet the continuous residual gap under the `basin` reference
still ranks triadic above dyadic (AUC 0.729, Spearman ρ with Φ 0.330,
p 0.025; `studies/ergodic_eoa_basin/`). Residual gaps are tiny
(≈0.005–0.02) and plausibly finite-T burn-in. Do triadic forms settle more
slowly — longer transients / slower convergence of time averages to the
attractor measure — and does that, rather than ergodicity-breaking, drive
the residual EoA gap?

**Already known (cited, not reopened).**
- Instrument stress (`ergodic_eoa_instrument`): agreement 17/42; verdict
  `EOA_TRACKS_MI_NOT_PHI`.
- Basin fix (`ergodic_eoa_basin`): H1/H2 SUPPORTED (miss classes cleared);
  binary H3 REFUTED (all-AGREEING, agree 25/42); continuous H4 SUPPORTED
  under basin; verdict `EOA_BASIN_INCONCLUSIVE`.
- Working hypothesis under test here: residual gap ↔ Φ association is a
  settling-time confound, not a remaining metric-indecomposability signal.

**Null stated plainly.** Settling time may not differ between triadic and
dyadic forms, or may track state-space size `n`, attractor period, or
number of attractors rather than Φ. Both are legitimate results.

**Instrument (committed before this study's numbers).** Module:
`org_frontier/ergodicity/settling.py`, unit-tested in
`org_frontier/ergodicity/test_settling.py`. Measures:

- **(a) Transient length** — steps from a start until the trajectory first
  enters its attractor cycle. Per form over the uniform start ensemble:
  mean, max, and basin-mass-weighted mean of per-basin means. Covariates:
  `n_attractors`, mean / max attractor period, state-space size.
- **(b) Time-average convergence T** — smallest `T ∈ {1..T_max}` such that
  `|Ā_T(f) − μ_a(f)| < ε_conv` for party-bit observables `f`, where `μ_a`
  is the uniform mean of `f` on the attractor the start reaches. Unresolved
  cells (never enter the ε-ball by `T_max`) are coded `T_max + 1`. Per form:
  mean / max / median T over (start × party) cells.
- **(c) Noisy-chain relaxation** — under flip noise `ε_flip > 0`, spectral
  gap of the row-stochastic TPM and relaxation time `1/gap` (independent of
  the deterministic basin partition). Forms with gap 0 (reducible noisy
  chain) receive `relaxation_time = +inf` and are ranked above all finite
  values for AUC / Spearman.

Frozen thresholds: `ε_conv = 0.01`, `T_max = 256`, `ε_flip = 0.05`,
TV-mixing δ = 0.25 (reported covariate only). Primary observables: same
non-mediator party bits as the basin study (n=3: `{W,C}`; n=4: non-`S`).

**Panel (identical freeze to `ergodic_eoa_instrument` / `ergodic_eoa_basin`).**
1. G2 core (9), classifier library (5), absorbing/ejection (2).
2. Seeded random n=3 (20): seed `20260930`, same 8-gate palette and
   input-pair draw, reject duplicates of named members.
3. n=4 tractable (6): and_pool, or_pool, maj_homog, chain_ws_c1c2,
   hub_s, dual_latch.

Total **42** forms. CI subset: G2 core + classifier + ejection via
`--ci` (no random n=3, no n=4); H3 (needs committed basin gaps on the full
panel) and H5 confound checks are `NOT_TESTABLE` under `--ci`.

**Instrument gate.** memoryless triadic Φ=2; sticky dyadic Φ=0. Abort if
fail. Unit-test controls (known answers, no Φ): (a) Hamming-drain map mean
transient = 1.5; (b) identity / full-cycle mean transient = 0; (c) identity
mean convergence T = 1; (d) maj3 under `ε_flip=0.05` has spectral gap 0.

**Residual gap source.** Basin-mode `gap_mean` per form is read from the
committed CSV
`studies/ergodic_eoa_basin/results/forms.csv` (`mode=basin`, noise=0).
This study does not recompute EoA.

**Statistics (frozen).**
- One-sided Mann–Whitney: triadic scores stochastically larger than dyadic;
  report rank-AUC and a one-sided permutation p (2000 shuffles, seed
  `20260930`). Chance AUC = 0.5.
- Spearman rank correlation with Φ magnitude; two-sided permutation p
  (same seed / shuffle count). Chance ρ = 0.
- Infinite relaxation times: for rank statistics, replace `+inf` by
  `1 + max(finite relaxation times on the panel)` (one step above the
  worst finite mixer).

## H1 — triadic forms have longer mean transient than dyadic

On the 42-form panel, mean transient length is larger for whole-form
triadic than for dyadic by a one-sided Mann–Whitney test at α = 0.05
(report AUC). Pass if AUC ≥ **0.65** **or** one-sided permutation p < 0.05.

Null: AUC < 0.65 and p ≥ 0.05.

## H2 — transient length correlates with Φ magnitude

Spearman ρ of mean transient vs whole-form Φ on the 42-form panel:
|ρ| ≥ **0.30** with two-sided permutation p < 0.05.

Null: |ρ| < 0.30 or p ≥ 0.05.

## H3 — residual basin-mode EoA gap is explained by settling time

Primary settling covariate: mean transient length. Exact test: logistic
regression of whole-form triadic status on basin `gap_mean` alone
(univariate), then on `gap_mean` + mean transient (partial). H3 passes if
either:

1. `|β_gap_partial| / |β_gap_uni| ≤ 0.50` (the gap coefficient drops by
   half or more toward zero after controlling for transient), **or**
2. the univariate gap coefficient has two-sided p < 0.05 and the partial
   gap coefficient has two-sided p ≥ 0.05 (gap loses significance once
   transient is controlled),

**and** the partial Spearman of basin `gap_mean` vs Φ controlling for mean
transient satisfies |ρ_partial| < |ρ_uni| (magnitude drops).

Secondary report (not a pass criterion): the same battery with mean
convergence T in place of mean transient.

Null: gap's association with triadic / Φ does not shrink under either
rule after controlling for transient.

## H4 — noisy-chain relaxation separates triadic from dyadic

On the 42-form panel at `ε_flip = 0.05`, rank-AUC of relaxation time
(with the inf-replacement rule above) vs whole-form triadic ≥ **0.65**,
**or** one-sided Mann–Whitney permutation p < 0.05 (triadic larger).

Null: AUC < 0.65 and p ≥ 0.05.

## H5 — effect survives confounds (n, period, n_attractors)

Restricted to the primary H1 measure (mean transient):

1. Within n=3 forms alone, H1's AUC / p criterion still holds.
2. Partial Spearman of mean transient vs Φ controlling for mean attractor
   period and `n_attractors` still satisfies |ρ| ≥ **0.30** with
   permutation p < 0.05, **or** the residualized Mann–Whitney AUC of mean
   transient vs triadic (after linear residualization on period and
   `n_attractors`) still meets H1's pass rule.

Null: the n=3 stratum fails H1's rule **or** the partial / residualized
association fails both alternatives in (2). (If the panel has no
variation in a confound, that arm is reported `NOT_TESTABLE` and does
not block the other arm.)

**Primary verdict word.**
- H1 and H3 both hold → `SETTLING_EXPLAINS_RESIDUAL_GAP`
- H1 holds, H3 fails → `SETTLING_TRACKS_PHI_NOT_GAP`
- H1 fails, H4 holds → `MIXING_NOT_TRANSIENT`
- H1 fails and H4 fails → `SETTLING_NULL`
- else → `SETTLING_INCONCLUSIVE`

**Scope.** In-silico Boolean forms only. Evidence about settling on the
models and about the residual basin-mode gap; not about real
organizations or platforms. If triadic forms do settle more slowly, the
literacy / algorithmacy reading is only that a participant observing a
triadic coordination form sees non-representative behaviour for longer
during burn-in — still an in-silico claim about the Boolean models, not
a field finding. No panel numbers until `analyze_settling.py` runs after
this commit.
