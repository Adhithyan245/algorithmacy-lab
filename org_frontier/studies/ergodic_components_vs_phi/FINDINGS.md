# ergodic_components_vs_phi — findings

**Verdict: NO_ERGODIC_SIGNATURE** (secondary witnesses
`CROSS_BASIN_SPLIT` | `BASIN_DETERMINATION_SPLIT`). Whole-form triadic
forms do **not** show higher mean ergodic-component count or higher
party time–ensemble divergence than dyadic forms on this panel. Mean
components: triadic **2.1429**, dyadic **2.0000** (Δ=**0.1429** <
δ_c=0.5). Mean basin entropy: triadic **0.8092**, dyadic **0.9772**
(dyadic higher; H2 reverse). Divergence fraction vs basin-weighted
mixture: triadic **0.9333**, dyadic **1.0000** (H3 reverse). Every
coexistence form shows cross-basin party occupancy gap ≥ 0.1 (**H4
SUPPORTED**). Every multistable form disagrees on core or occupancy
across basins (**E4 SUPPORTED**, 8/8).

In-silico; exact IIT-4.0 Φ_MIP on attractor states; n=3 panel of 9
forms. Hypotheses fixed in `hypotheses.md` before computing. Note:
uniform-on-attractor vs cycle time average is identically zero on
deterministic cycles (derived); H3 uses |cycle avg − basin-weighted
mixture| as the ensemble-over-starts contrast.

## Panel

| form | whole | n_c | H_b | tri_a | dya_a | div_frac |
|---|---|---:|---:|---:|---:|---:|
| memoryless | triadic | 3 | 1.406 | 1 | 2 | 1.000 |
| sticky | dyadic | 2 | 0.954 | 0 | 2 | 1.000 |
| xor_memory | triadic | 2 | 0.954 | 1 | 1 | 1.000 |
| or_commit | triadic | 3 | 1.406 | 1 | 2 | 1.000 |
| sticky_or | triadic | 2 | 0.544 | 1 | 1 | 1.000 |
| sticky_parity | triadic | 2 | 0.811 | 1 | 1 | 1.000 |
| parity_hub | triadic | 1 | 0.000 | 1 | 0 | 0.000 |
| maj3 | dyadic | 2 | 1.000 | 0 | 2 | 1.000 |
| w_follows_c | triadic | 2 | 0.544 | 1 | 1 | 1.000 |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 component count tracks triadic | **REFUTED** |
| H2 basin entropy tracks triadic | **REFUTED** |
| H3 divergence tracks triadic | **REFUTED** |
| H4 coexistence ⇒ cross-basin split | **SUPPORTED** |
| E4 basins disagree core/occ | **SUPPORTED** |

## Reading

T2 (component count / divergence track Φ_MIP) is **refuted** on this
designed panel: multistability and EoA failure are common to both
verdicts. T3 (cross-basin competence split under coexistence) is
**supported**. E4 / T6 Boolean clause (basins as distinct
who-determines-whom readings) is **supported**. Whole-form Φ is not a
proxy for ergodic-component richness here; attractor-level structure
still carries the coexistence and determination signatures.

## Limits

n=3 deterministic Boolean panel only; designed forms, not a random
ensemble (B5 still open). No organization measured.

## Reproduce

```
python org_frontier/studies/ergodic_components_vs_phi/analyze_components.py
```
