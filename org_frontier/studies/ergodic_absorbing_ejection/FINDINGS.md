# ergodic_absorbing_ejection — findings

**Verdict: ABSORBING_EJECTION.** The ejected_latch encoding hosts an
absorbing inactive attractor (cycle `000`, basin **7**, exit rate **0**,
dyadic Φmax=**0**) and a triadic active attractor (cycle `111`, basin
**1**, Φmax=**2.000**). Memoryless contrast remains whole-form triadic
Φ=**2.000**. Sticky retains an active dyadic attractor (`111`) alongside
inactive `000` — not a one-way extractive absorption (**H3 SUPPORTED**).

In-silico; exact IIT-4.0; n=3. Hypotheses fixed in `hypotheses.md`.

## Attractors (witnesses)

| form | cycle | basin | exit | S=0 | verdict | Φmax |
|---|---|---:|---:|---|---|---:|
| ejected_latch | 000 | 7 | 0 | yes | dyadic | 0 |
| ejected_latch | 111 | 1 | 0 | no | triadic | 2.000 |
| memoryless | 111 | 1 | 0 | no | triadic | 2.000 |
| sticky | 000 | 3 | 0 | yes | dyadic | 0 |
| sticky | 111 | 5 | 0 | no | dyadic | 0 |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 absorbing inactive on ejected_latch | **SUPPORTED** |
| H2 ejected dyadic / pre-ejection triadic | **SUPPORTED** |
| H3 sticky ≠ absorbing-ejection witness | **SUPPORTED** |

## Reading

T5's Boolean clause holds on this encoding: ruin-as-absorption is
representable as an ergodic component with a dyadic/null inactive
attractor while a triadic pre-ejection attractor remains. Sticky
multistability is a different phenomenon (activity latch, both dyadic).

## Limits

Single designed latch family; ejected_latch_or collapses to all-dyadic
(whole Φ=0) — encoding-local. No organization measured.

## Reproduce

```
python org_frontier/studies/ergodic_absorbing_ejection/analyze_absorb.py
```
