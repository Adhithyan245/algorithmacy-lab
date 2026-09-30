# ergodic_settling_time — findings

**Verdict: SETTLING_NULL.** On the frozen 42-form panel, mean transient
length does not separate whole-form triadic from dyadic (median **0.875**
either class; AUC **0.540**, one-sided permutation p **0.338**). Transient
length does not correlate with Φ (Spearman ρ **0.051**, p **0.754**).
Controlling for mean transient does not shrink the residual basin-mode EoA
gap's association with triadic status — the logistic |β_gap| ratio is
**1.197** (partial larger than univariate) and partial Spearman of gap vs Φ
rises from **0.333** to **0.353**. Noisy-chain relaxation time at
`ε_flip=0.05` ranks the wrong way (AUC **0.338**). The pre-registered null
holds: settling time does not differ by Φ class on this panel, and it does
not explain the residual basin-mode gap.

In-silico Boolean forms only. Hypotheses fixed in `hypotheses.md` before
`analyze_settling.py` produced numbers.

## Measures (one line each)

| measure | definition |
|---|---|
| transient length | steps from a start until the trajectory first enters its attractor cycle; per form: mean / max / basin-weighted mean over the uniform start ensemble |
| convergence T | smallest T with \|Ā_T(f) − μ_a(f)\| < ε_conv=0.01 for party bits; unresolved cells coded T_max+1=257 |
| noisy relaxation | 1 / spectral gap of the ε_flip=0.05 flip-noise TPM (inf when gap=0) |

Covariates: `n_attractors`, mean / max attractor period, state-space size.

## Headline contrasts (n=42; triadic 17, dyadic 25)

| measure | median triadic | median dyadic | AUC | p (one-sided) | Spearman vs Φ | p |
|---|---:|---:|---:|---:|---:|---:|
| transient_mean | 0.875 | 0.875 | 0.540 | 0.338 | 0.051 | 0.754 |
| conv_mean_T | 51.0 | 32.25 | 0.651 | 0.056 | 0.211 | 0.180 |
| relaxation_time | 20.12 | 30.0 | 0.338 | 0.959 | −0.160 | 0.302 |

Mean transient is slightly higher for triadic than dyadic in the raw mean
(1.118 vs 0.842) but the rank test does not clear the pre-registered bar.
Convergence T is the only measure that approaches separation (AUC 0.651,
p 0.056); it was not a primary H1 score and does not pass at α=0.05.

## H3 — mediation of the residual basin gap

Basin-mode `gap_mean` from the committed `ergodic_eoa_basin` CSV still
predicts triadic status univariately (standardized logistic β=1.139,
p=0.012). Adding mean transient raises β_gap to 1.363 (p=0.033); the
ratio |β_partial|/|β_uni| = 1.197 fails the ≤0.50 shrink rule, and gap
does not lose significance. Partial Spearman of gap vs Φ controlling for
transient is 0.353 against univariate 0.333 — magnitude does not drop.
Secondary battery with mean convergence T likewise fails
(|β_partial|/|β_uni|=1.259; partial ρ=0.266 < univariate 0.333 on the
Spearman arm alone, but the logistic shrink rule fails, so H3's joint
pass criterion is not met).

The residual continuous gap–Φ association reported under
`EOA_BASIN_INCONCLUSIVE` is therefore not a settling-time confound under
the pre-registered test.

## Confounds (H5)

Within n=3 (36 forms): transient AUC 0.615, p 0.127 — fails H1's rule.
Partial Spearman of transient vs Φ controlling for mean period and
`n_attractors`: ρ=0.065, p=0.702. Residualized Mann–Whitney AUC after
linear residualization on period and `n_attractors`: 0.655 (would pass
AUC alone) but the conjunction with the n=3 stratum fails. H5 REFUTED.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 triadic longer mean transient (AUC≥0.65 or p<0.05) | **REFUTED** (AUC=0.540, p=0.338) |
| H2 transient correlates with Φ (\|ρ\|≥0.30, p<0.05) | **REFUTED** (ρ=0.051, p=0.754) |
| H3 basin gap explained by settling (logistic shrink + Spearman drop) | **REFUTED** (ratio=1.197; partial ρ rises) |
| H4 noisy relaxation separates triadic | **REFUTED** (AUC=0.338, p=0.959) |
| H5 survives n / period / n_attractors | **REFUTED** |

## Reading

The working hypothesis that triadic forms settle more slowly, and that
slow settling drives the residual basin-mode EoA gap, is refuted on this
panel. Transient length and noisy-chain relaxation do not track the
literacy / algorithmacy cut; the residual gap's weak continuous
association with Φ survives controlling for settling and is not reduced
by it. Exact Φ remains the cut; neither fixed-threshold EoA nor
settling time replaces it. Any reading that "a participant sees
non-representative behaviour longer under triadic coordination" is not
supported by these Boolean models — the claim stays in-silico and, on
the pre-registered measures, is null.

## Limits

Same frozen panel (seed 20260930) and party observables as
`ergodic_eoa_instrument` / `ergodic_eoa_basin`. Convergence uses
ε_conv=0.01 and T_max=256; noisy mixing uses single-bit flip noise at
0.05 (reducible chains get gap 0 / relaxation +inf). Basin gaps are
read from the committed basin-study CSV, not recomputed. No real
platform logs. Scope: in-silico Boolean forms.

## Reproduce

```
python org_frontier/ergodicity/test_settling.py
python org_frontier/studies/ergodic_settling_time/analyze_settling.py
python org_frontier/studies/ergodic_settling_time/analyze_settling.py --ci
```
