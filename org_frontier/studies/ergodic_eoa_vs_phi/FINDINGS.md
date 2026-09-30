# ergodic_eoa_vs_phi — findings

**Verdict: EOA_AGREES_PHI.** Operational EoA on synthetic trajectory
logs agrees with whole-form Φ on **7/9** forms (agree rate **0.778**;
one-sided binomial P(X≥7 | n=9, p=0.5)=**0.0898**). H1 passes the
pre-registered ≥7/9 rule. Multi-attractor mean fail rate **0.797** vs
single-attractor **0.500** (Δ=**0.297** ≥ 0.15; **H2 SUPPORTED**).
Sticky is operational FAIL and whole-form dyadic — the named
disagreement witness (**H3 SUPPORTED**): MI/EoA can fire without
triadic Φ.

In-silico synthetic logs only. Hypotheses fixed in `hypotheses.md`.

## Forms

| form | whole | n_a | fail_rate | op | agree |
|---|---|---:|---:|---|---|
| memoryless | triadic | 3 | 0.500 | FAIL | yes |
| sticky | dyadic | 2 | 1.000 | FAIL | **no** |
| xor_memory | triadic | 2 | 0.875 | FAIL | yes |
| or_commit | triadic | 3 | 0.500 | FAIL | yes |
| sticky_or | triadic | 2 | 0.875 | FAIL | yes |
| sticky_parity | triadic | 2 | 0.875 | FAIL | yes |
| parity_hub | triadic | 1 | 0.500 | FAIL | yes |
| maj3 | dyadic | 2 | 1.000 | FAIL | **no** |
| w_follows_c | triadic | 2 | 0.750 | FAIL | yes |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 EoA agrees with Φ (≥7/9) | **SUPPORTED** |
| H2 multi-attractor fail rate higher | **SUPPORTED** |
| H3 sticky FAIL×dyadic witness | **SUPPORTED** |

## Reading

T8 is **supported** at the pre-registered agreement threshold, with an
important limit: both dyadic forms on the panel (sticky, maj3) are
multi-attractor EoA failures. Operational EoA tracks multistability
(MI) more tightly than Φ; agreement with Φ on this panel is driven by
triadic forms also being multistable Failures. EoA alone is not a Φ
proxy when dyadic multistability is present.

## Limits

Uniform-on-X ensemble; ε_div=0.1; fail-rate threshold 0.25; designed
n=3 panel. No real platform logs (G1 still open).

## Reproduce

```
python org_frontier/studies/ergodic_eoa_vs_phi/analyze_eoa.py
```
