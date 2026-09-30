# ergodic_settling_time (Strand G / T8 residual)

Settling-time measures vs exact Φ_MIP on the frozen 42-form panel from
`ergodic_eoa_instrument`, testing whether the residual basin-mode EoA gap
(`ergodic_eoa_basin`) is a finite-T burn-in effect.

Hypotheses fixed in [`hypotheses.md`](hypotheses.md) **before** computing.
Prior cells: [`../ergodic_eoa_basin/`](../ergodic_eoa_basin/),
[`../ergodic_eoa_instrument/`](../ergodic_eoa_instrument/).
Track: [`../../ergodicity/`](../../ergodicity/).

## Instrument

`org_frontier.ergodicity.settling` — transient length, time-average
convergence T, noisy-chain spectral gap / relaxation time.

```
python org_frontier/ergodicity/test_settling.py
```

## Run

```
python org_frontier/studies/ergodic_settling_time/analyze_settling.py
python org_frontier/studies/ergodic_settling_time/analyze_settling.py --ci
```
