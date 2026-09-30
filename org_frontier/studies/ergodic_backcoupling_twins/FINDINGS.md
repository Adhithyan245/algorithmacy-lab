# ergodic_backcoupling_twins — findings

**Verdict: BACKCOUPLING_SPLITS.** Skew-factor presence tracks the convey
vs accumulating split on all three twin pairs (**H1 SUPPORTED**). At
least one pair flips whole-form Φ verdict (**H2 SUPPORTED**: memoryless
triadic Φ=2.000 ↔ sticky dyadic Φ=0.000). The strong reading
accumulating⇒triadic and convey⇒dyadic is **REFUTED** (**H3**): the
primary twin flips the opposite way, and sticky_or / sticky_parity remain
triadic with their convey twins.

In-silico; exact IIT-4.0; n=3. Hypotheses fixed in `hypotheses.md`.

## Twins

| convey | skew | Φ | accum | skew | Φ | flip |
|---|---|---|---|---|---|---|
| memoryless | yes | tri 2.000 | sticky | no | dya 0.000 | yes |
| or_commit | yes | tri 2.000 | sticky_or | no | tri 2.000 | no |
| parity_hub | yes | tri 0.500 | sticky_parity | no | tri 0.500 | no |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 skew tracks convey/accumulate | **SUPPORTED** |
| H2 some verdict flip | **SUPPORTED** |
| H3 accum⇒triadic & convey⇒dyadic | **REFUTED** |

## Reading

T1's structural skew-product criterion holds as a decidable Boolean
test. Mapping skew→literacy and coupled→algorithmacy via whole-form Φ
does **not** hold in the strong H3 direction: the #43 sticky latch is
coupled and dyadic. Back-coupling is necessary to break skew-product
structure; it is not sufficient for a triadic Φ verdict.

## Limits

Three designed twins only; party reads fixed W'=C'=S. No continuous
recommender dynamics.

## Reproduce

```
python org_frontier/studies/ergodic_backcoupling_twins/analyze_twins.py
```
