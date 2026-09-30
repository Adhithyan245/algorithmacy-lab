# ergodic_gap_decomposition — hypotheses (fixed before computing)

**Question (Strand G / T8 residual).** Once multistability is conditioned
out and settling time has been ruled out as a confound, the continuous
basin-mode Equality-of-Averages residual gap still ranks whole-form
triadic above dyadic on the frozen 42-form panel (AUC 0.729, Spearman ρ
with Φ 0.330, p 0.025; standardized logistic β 1.139, p 0.012;
`studies/ergodic_eoa_basin/`, `studies/ergodic_settling_time/`). Residual
gaps are tiny (≈0.005–0.02 at T=64). What drives that residual link?

**Already known (cited, not reopened).**
- Instrument stress (`ergodic_eoa_instrument`): agreement 17/42; verdict
  `EOA_TRACKS_MI_NOT_PHI`.
- Basin fix (`ergodic_eoa_basin`): binary all-AGREEING under basin /
  stationary; continuous H4 SUPPORTED under basin; verdict
  `EOA_BASIN_INCONCLUSIVE`.
- Settling residual (`ergodic_settling_time`): mean transient does not
  separate triadic from dyadic; controlling for it leaves the gap–Φ
  association unchanged or slightly stronger; verdict `SETTLING_NULL`.

**Null stated plainly.** None of the four mechanisms below may explain
the association. The original AUC may also be a small-panel fluke: the
bootstrap CI on AUC may cover chance (0.5), or a label-permutation test
may fail to reject at α=0.05. Both are legitimate results.

**Instrument (committed before this study's numbers).** Reuses
`org_frontier.ergodicity.eoa` (basin reference) and
`org_frontier.ergodicity.settling` (attractor partition / cycle means).
Backward-compatible extensions (unit-tested) add attractor-oscillation
and within-basin path-diversity summaries; prior call sites unchanged.

**Panel (identical freeze).** G2 core (9) + classifier (5) + ejection (2)
+ random n=3 seed `20260930` (20) + n=4 tractable (6) = **42** forms
(17 triadic, 25 dyadic). CI subset: G2 + classifier + ejection via
`--ci` (no random n=3, no n=4); full-panel hypotheses that need n=42 are
`NOT_TESTABLE` under `--ci`.

**Primary residual gap.** Basin-mode pooled party-bit `gap_mean` at
`T=64`, `noise=0`, matching `ergodic_eoa_basin` (read from the committed
CSV and verified by recomputation; abort if any form differs by >
1e-6). Decomposition also reports per-observable gaps (each party bit
separately, mediator `S`, parity `W⊕C` / first-two non-S bits on n=4),
per-basin mean gaps, and per-start gaps.

**Statistics (frozen).**
- Logistic of triadic on standardized predictors; report β and two-sided
  normal p. Shrink rule: `|β_partial| / |β_uni| ≤ 0.50`.
- Spearman ρ of gap vs Φ; partial Spearman controlling for a covariate;
  two-sided permutation p (2000 shuffles, seed `20260930`).
- Rank-AUC of a score vs triadic; one-sided / two-sided permutation as
  named per hypothesis.
- Bootstrap CI on AUC: 2000 stratified resamples of the 42 forms
  (seed `20260930`); report 2.5th / 97.5th percentiles.
- T-grid: `T ∈ {16, 32, 64, 128, 256, 512}` under basin / noise=0 /
  pooled party bits. Per form, fit OLS of `log(gap_mean + 1e-12)` on
  `log(T)`; report the panel mean slope. Also report the Spearman of
  `(gap_mean × T)` across T with a constant (phase-artifact signature:
  `gap·T` roughly flat ⇒ mean |CV| of `gap·T` across T small).

**Primary ranking rule.** Among mechanisms that pass their shrink /
mediation criterion, the winner is the covariate with the **smallest**
`|β_partial| / |β_uni|` on the full panel (most absorption). If none
pass, the ranking reports the covariate with the smallest ratio anyway
as a descriptive note, and the overall verdict is the null word. Tie:
prefer the mechanism with the larger drop in |Spearman|.

---

## Covariates (one measurable per mechanism)

| id | mechanism | covariate (per form) |
|---|---|---|
| (a) | Finite-T phase artifact | `party_osc_frac` — fraction of party-bit × attractor cells where the bit is non-constant on the cycle; also `mean_cycle_var` (mean Bernoulli variance of party bits over cycles, basin-mass weighted) and `mean_period` |
| (b) | Within-basin heterogeneity | `pre_cycle_div` — mean over starts of the number of distinct party-bit tuples visited strictly before cycle entry (0 if start is on-cycle), divided by `2^{n_parties}` so the scale is in [0,1] |
| (c) | Observable choice | `party_gap` vs `mediator_gap` — basin `gap_mean` for pooled party bits vs for `S` alone; oscillation restricted to parties (`party_osc_frac`) is the mediation covariate for the claim that triadic forms keep parties moving |
| (d) | Panel composition | leave-one-group-out AUC of basin `gap_mean` vs triadic |

---

## H0 — original association is not a small-panel fluke

On the full 42-form panel, basin `gap_mean` (T=64) vs triadic:

1. Bootstrap 95% CI for AUC excludes 0.5 (lower bound > 0.5), **and**
2. Label-permutation two-sided p for AUC (2000 shuffles, seed
   `20260930`) < 0.05.

Null: CI covers 0.5 **or** permutation p ≥ 0.05. (Fluke / fragile.)

## H1 — finite-T phase artifact (mechanism a)

Pass if **both**:

1. Panel-mean OLS slope of `log(gap+ε)` on `log(T)` lies in
   **[−1.25, −0.75]** (near −1 ⇒ gap ∼ 1/T), **and**
2. Logistic shrink: `|β_gap | party_osc_frac| / |β_gap uni| ≤ 0.50`
   **or** partial Spearman |ρ(gap, Φ | osc)| < |ρ_uni| **and**
   `|β_ratio| ≤ 0.75`.

Null: slope outside the band, **or** oscillation does not absorb the
gap–triadic link under the shrink / partial rule.

Secondary report (not a pass gate): mean coefficient of variation of
`gap·T` across the T-grid (small CV supports a pure phase artifact).

## H2 — within-basin heterogeneity (mechanism b)

Pass if `|β_gap | pre_cycle_div| / |β_gap uni| ≤ 0.50`, **or** the
univariate gap β has p < 0.05 and the partial has p ≥ 0.05, **and**
partial Spearman |ρ(gap, Φ | div)| < |ρ_uni|.

Null: controlling for pre-cycle diversity does not shrink the
association under either rule.

## H3 — observable choice / party oscillation (mechanism c)

Pass if **both**:

1. Party-pooled basin gap separates triadic better than mediator gap:
   `AUC(party_gap) − AUC(mediator_gap) ≥ 0.10`, **or** party gap has
   Spearman |ρ| vs Φ at least 0.10 larger than mediator gap's |ρ|, **and**
2. Mediation through `party_osc_frac`: same shrink / partial-Spearman
   rule as H1(2).

Null: party and mediator gaps carry similar association, **or**
party oscillation does not absorb the link.

If H3 passes: the in-silico reading is only that, on these Boolean
forms, triadic coordination keeps party bits non-constant on attractors
more often than dyadic forms do, and that oscillation accounts for the
tiny residual EoA gap. No claim about real organizations, literacy, or
algorithmacy in the field.

## H4 — one panel group carries the association (mechanism d)

Leave-one-group-out: for each group in
`{g2_core, classifier, ejection, random_n3, n4}`, recompute AUC of
basin `gap_mean` vs triadic on the remaining forms. H4 passes if
**some** leave-out drops AUC below **0.65** **and** drops Spearman |ρ|
below **0.30** (that group's removal kills the pre-registered H4 band
from the basin study). Report every leave-out AUC / ρ.

Null: every leave-out still has AUC ≥ 0.65 **or** |ρ| ≥ 0.30 (no single
group is necessary for the band).

## H5 — recomputed basin gaps match the committed CSV

For every form on the panel (CI subset under `--ci`),
`|recomputed_gap_mean − committed_gap_mean| ≤ 1e-6` at T=64 /
basin / noise=0 / pooled parties. Abort the study (do not score H0–H4)
if any form exceeds the tolerance.

Null: any mismatch → study `NOT_TESTABLE` / gate fail.

**Primary verdict word.**
- H0 fails → `GAP_ASSOC_FLUKE`
- H0 holds and H1 passes and H1 wins the ranking → `GAP_PHASE_ARTIFACT`
- H0 holds and H2 passes and H2 wins → `GAP_WITHIN_BASIN_HETERO`
- H0 holds and H3 passes and H3 wins → `GAP_PARTY_OSCILLATION`
- H0 holds and H4 passes and no mechanism among H1–H3 passes →
  `GAP_PANEL_COMPOSITION`
- H0 holds and none of H1–H4 pass → `GAP_UNEXPLAINED`
- else (mixed pattern, e.g. H0 holds, a mechanism passes but loses the
  ranking to a non-passing competitor's descriptive ratio) →
  `GAP_DECOMPOSITION_INCONCLUSIVE`

**Scope.** In-silico Boolean forms only. Evidence about the residual
basin-mode gap on the models; not about real organizations or
platforms. No panel numbers until `analyze_decomposition.py` runs after
this commit.
