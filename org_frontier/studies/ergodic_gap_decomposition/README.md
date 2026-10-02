# ergodic_gap_decomposition (Strand G / T8 residual)

Decompose the residual basin-mode EoA gap's continuous association with
whole-form Φ_MIP on the frozen 42-form panel, after multistability was
conditioned out and settling time was ruled out as a confound.

Hypotheses fixed in [`hypotheses.md`](hypotheses.md) **before** computing.
Prior cells: [`../ergodic_settling_time/`](../ergodic_settling_time/),
[`../ergodic_eoa_basin/`](../ergodic_eoa_basin/),
[`../ergodic_eoa_instrument/`](../ergodic_eoa_instrument/).
Track: [`../../ergodicity/`](../../ergodicity/).

## Mechanisms under test

| id | claim | covariate |
|---|---|---|
| (a) | Finite-T phase artifact | party-bit attractor oscillation; gap ∼ 1/T |
| (b) | Within-basin path heterogeneity | pre-cycle party-tuple diversity |
| (c) | Observable choice | party vs mediator gaps; party oscillation mediation |
| (d) | Panel composition | leave-one-group-out AUC |

## Instrument

`org_frontier.ergodicity.eoa` (basin reference) and
`org_frontier.ergodicity.settling` (partition helpers), plus
backward-compatible oscillation / path-diversity summaries.

```
python org_frontier/ergodicity/test_eoa.py
python org_frontier/ergodicity/test_settling.py
```

## Run

```
python org_frontier/studies/ergodic_gap_decomposition/analyze_decomposition.py
python org_frontier/studies/ergodic_gap_decomposition/analyze_decomposition.py --ci
```

No numbers in this README. Results land only from the analysis script
after the hypotheses commit.
