# ergodic_gap_decomposition — findings

**Verdict: GAP_UNEXPLAINED.** On the frozen 42-form panel the residual
basin-mode EoA gap's continuous association with whole-form triadic status
is not a small-panel fluke (H0 SUPPORTED: AUC **0.729**, bootstrap 95% CI
**[0.560, 0.862]**, label-permutation p **0.0075**). None of the four
pre-registered mechanisms absorbs that association. Finite-T scaling of
the gap magnitude is consistent with a phase artifact (mean log-log slope
**−0.976**, mean CV of `gap·T` **0.0049**), but party-bit attractor
oscillation does not shrink the logistic link (β ratio **0.985**).
Pre-cycle path diversity does not shrink it either (β ratio **1.163**).
The signal lives in party bits rather than the mediator (AUC party
**0.729** vs mediator **0.498**), yet oscillation mediation still fails,
so H3 is REFUTED. No single panel group is necessary for the basin-study
H4 band (H4 REFUTED). Recomputed basin gaps match the committed CSV on
all 42 forms (H5 SUPPORTED). Ranking among a–c finds no passing
mechanism; the overall verdict is the stated null.

In-silico Boolean forms only. Hypotheses fixed in `hypotheses.md` before
`analyze_decomposition.py` produced numbers.

## Per-mechanism results

| mechanism | covariate | β ratio | partial ρ | T-scaling slope | passes |
|---|---|---:|---:|---:|---|
| (a) phase artifact | `party_osc_frac` | 0.985 | 0.325 | −0.976 | no |
| (b) within-basin | `pre_cycle_div` | 1.163 | 0.346 | — | no |
| (c) party oscillation | `party_osc_frac` | 0.985 | 0.325 | — | no |
| (d) panel composition | leave-one-group | — | — | — | no |

Primary ranking rule: no mechanism passes, so there is no winner.
Descriptive lowest β ratio among a–c is (a) at 0.985.

## H0 — association not a fluke

| statistic | value |
|---|---:|
| AUC(gap, triadic) | 0.729 |
| bootstrap 95% CI | [0.560, 0.862] |
| permutation p (two-sided vs chance) | 0.0075 |
| Spearman ρ(gap, Φ) | 0.330 (p 0.025) |
| standardized logistic β_gap | 1.125 (p 0.012) |

CI lower bound > 0.5 and p < 0.05 → **H0 SUPPORTED**.

## H1 — finite-T phase artifact

Mean OLS slope of `log(gap+ε)` on `log(T)` over
`T ∈ {16,32,64,128,256,512}` is **−0.976** (inside [−1.25, −0.75]).
Mean CV of `gap·T` across the grid is **0.0049** (nearly flat). The
gap *magnitude* therefore scales as ∼1/T. Controlling for
`party_osc_frac` leaves β_gap almost unchanged (1.125 → 1.108; ratio
0.985) and partial Spearman 0.325 vs univariate 0.330. Mediation fails
→ **H1 REFUTED**. A gap that shrinks as 1/T is still compatible with a
phase remainder; what fails is the claim that attractor oscillation of
party bits carries the triadic association.

## H2 — within-basin heterogeneity

`pre_cycle_div` raises rather than shrinks β_gap (ratio 1.163); partial
Spearman rises to 0.346. **H2 REFUTED**.

## H3 — observable choice / party oscillation

Party-pooled basin gap AUC **0.729** vs mediator-only AUC **0.498**
(Δ = 0.232); Spearman |ρ| likewise larger for parties (0.330 vs 0.046).
Observable separation clears the pre-registered 0.10 bar. Mediation
through `party_osc_frac` does not (same β ratio 0.985 as H1). Joint
pass requires both → **H3 REFUTED**. In-silico only: the residual score
ranks forms through party-bit gaps, not mediator gaps; that does not
by itself show that triadic coordination “keeps parties moving,” because
the oscillation covariate does not absorb the Φ link.

## H4 — leave-one-group-out

| left out | n left | AUC | Spearman ρ | kills band |
|---|---:|---:|---:|---|
| g2_core | 33 | 0.759 | 0.386 | no |
| classifier | 37 | 0.709 | 0.287 | no |
| ejection | 40 | 0.750 | 0.367 | no |
| random_n3 | 22 | 0.705 | 0.194 | no |
| n4 | 36 | 0.735 | 0.353 | no |

Killing the band requires AUC < 0.65 **and** |ρ| < 0.30. Dropping
`random_n3` softens ρ but leaves AUC at 0.705; no leave-out meets both
→ **H4 REFUTED**.

## Hypotheses

| hypothesis | result |
|---|---|
| H0 association not a fluke | **SUPPORTED** |
| H1 finite-T phase artifact | **REFUTED** |
| H2 within-basin heterogeneity | **REFUTED** |
| H3 observable choice / party oscillation | **REFUTED** |
| H4 one panel group carries the association | **REFUTED** |
| H5 recomputed gaps match committed CSV | **SUPPORTED** |

## Reading

The residual continuous gap–Φ association reported under
`EOA_BASIN_INCONCLUSIVE` survives the fluke check and survives every
pre-registered mechanism test on this panel. Exact Φ remains the
literacy / algorithmacy cut. The gap's *size* is a finite-T remainder
(∼1/T; typical 0.005–0.02 at T=64), and the score that ranks forms is
the party-bit gap rather than the mediator gap, but neither fact
explains *why* that tiny remainder still tracks Φ after multistability
and settling time are conditioned out. No claim about real organizations
follows.

## Limits

Same frozen panel (seed 20260930) and basin reference as
`ergodic_eoa_basin`. Φ / structure labels are read from the committed
basin CSV; gaps are recomputed and matched (H5). Oscillation and
pre-cycle diversity are deterministic summaries of the zero-noise
partition. Bootstrap and permutation use 2000 draws at seed 20260930.
No real platform logs. Scope: in-silico Boolean forms.

## Reproduce

```
python org_frontier/ergodicity/test_settling.py
python org_frontier/studies/ergodic_gap_decomposition/analyze_decomposition.py
python org_frontier/studies/ergodic_gap_decomposition/analyze_decomposition.py --ci
```
