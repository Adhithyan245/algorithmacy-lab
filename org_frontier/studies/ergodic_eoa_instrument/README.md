# ergodic_eoa_instrument (Strand G / T8 stress)

Reusable Equality-of-Averages instrument, diagnosed G2 misses, and a
wider stress panel against exact Φ_MIP.

Hypotheses fixed in [`hypotheses.md`](hypotheses.md) **before** computing
(commit precedes `analyze_stress.py`). Track:
[`../../ergodicity/`](../../ergodicity/). Prior cell:
[`../ergodic_eoa_vs_phi/`](../ergodic_eoa_vs_phi/) (G2).

## Instrument

`org_frontier.ergodicity.eoa` — `run_eoa` / `run_eoa_parties`. Unit tests:

```
python -m org_frontier.ergodicity.test_eoa
```

## Run

```
python org_frontier/studies/ergodic_eoa_instrument/analyze_stress.py
python org_frontier/studies/ergodic_eoa_instrument/analyze_stress.py --ci
```
