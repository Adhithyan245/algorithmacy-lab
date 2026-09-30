# Ergodic components vs Φ (track first cell)

Does attractor / basin structure — the ergodic components of a finite Boolean
map — differ systematically between triadic forms (Φ_MIP > 0) and dyadic forms
(Φ_MIP = 0)?

Track home: [`../../ergodicity/`](../../ergodicity/). Sibling:
[`../genuine_bistability/`](../genuine_bistability/) (agenda #13,
GENUINE_COEXISTENCE).

## Status

**RUN.** Results in `results/` and [`FINDINGS.md`](FINDINGS.md). Verdict
`NO_ERGODIC_SIGNATURE` with secondary `CROSS_BASIN_SPLIT` |
`BASIN_DETERMINATION_SPLIT`. Hypotheses fixed before computing.

## Question (one line)

On matched Boolean coordination panels, do triadic forms show more ergodic
components (attractors / basins) and larger party-level time–ensemble
divergence than dyadic forms?

## Run

```
python org_frontier/studies/ergodic_components_vs_phi/analyze_components.py
```
