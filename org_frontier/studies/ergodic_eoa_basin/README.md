# ergodic_eoa_basin (Strand G / T8 per-outcome fix)

Basin-restricted and attractor-stationary Equality-of-Averages vs exact
Φ_MIP on the frozen 42-form panel from `ergodic_eoa_instrument`.

Hypotheses fixed in [`hypotheses.md`](hypotheses.md) **before** computing.
Prior cell: [`../ergodic_eoa_instrument/`](../ergodic_eoa_instrument/).
Track: [`../../ergodicity/`](../../ergodicity/).

## Instrument modes

`org_frontier.ergodicity.eoa` — `run_eoa` / `run_eoa_parties` with
`reference_mode ∈ {uniform, basin, stationary}`.

```
python -m org_frontier.ergodicity.test_eoa
```

## Run

```
python org_frontier/studies/ergodic_eoa_basin/analyze_basin.py
python org_frontier/studies/ergodic_eoa_basin/analyze_basin.py --ci
```
