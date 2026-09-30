# ergodic_eoa_instrument — findings

**Verdict: EOA_TRACKS_MI_NOT_PHI.** On the pre-registered 42-form stress
panel the EoA instrument agrees with whole-form Φ on **17/42** forms
(agree rate **0.405**; one-sided binomial P(X≥17 | n=42, p=0.5)=**0.918**).
H1 (agreement ≥0.65) is **REFUTED**. Every form is operational
`BREAKING` (confusion TP=17, FP=25, TN=0, FN=0): the agreement rate
collapses to the panel's triadic base rate. Among the 25 disagreements,
**20/25 (0.800)** are dyadic multi-attractor forms (**H2 SUPPORTED**).
Both G2 misses — sticky and maj3 — remain `BREAKING` × dyadic ×
multi-attractor (**H3 SUPPORTED**). EoA wall-clock on the G2 core is
~0.007× exact Φ (**H4 SUPPORTED**). Horizon / noise / S-only contrasts
on the G2 core stay inside the pre-registered bands (**H5a–c
SUPPORTED**).

In-silico Boolean forms only. Hypotheses fixed in `hypotheses.md` before
`analyze_stress.py`.

## G2 misses — mechanism

G2 disagreed on exactly two of nine forms: **sticky** and **maj3**. Both
are whole-form dyadic (Φ_MIP = 0) with two attractors and polarized
party occupancy:

| form | Φ | attractors | party occupancy on attractors | EoA |
|---|---|---|---|---|
| sticky | 0 | 000, 111 | W=C=0 on 000; W=C=1 on 111 | BREAKING |
| maj3 | 0 | 000, 111 | same polarization | BREAKING |

Under a uniform-on-X ensemble the reference mean for each party bit is
0.5. A trajectory that absorbs into 000 (or 111) has time average ≈0
(or ≈1). The gap exceeds ε_div=0.1 from every mixed start, so the form
fail rate is 1.0. The failure is **basin polarization under a mixed
ensemble**, not triadic irreducibility. Sticky is the latch
(S' = (W∧C)∨S) that creates the two poles without binding W–S–C into a
non-factorable MIP; maj3 is homogeneous majority, which factors along
every party cut while still splitting the state space into two
absorbing poles. Horizon T and small flip noise do not remove the
disagreement on the G2 core (H5). The informative reading from G2
therefore generalizes: operational EoA tracks multistability / metric
indecomposability more tightly than Φ.

## Stress panel

| group | n | agree | note |
|---|---:|---:|---|
| g2_core | 9 | 7 | same cells as G2; sticky, maj3 miss |
| classifier | 5 | 2 | dyadic library forms all BREAKING |
| ejection | 2 | 1 | ejected_latch_or dyadic×multi miss |
| random_n3 (seed 20260930) | 20 | 4 | triadic base rate low |
| n4 designed | 6 | 3 | maj_homog / dual_latch / chain miss |
| **total** | **42** | **17** | |

Confusion (BREAKING as positive for triadic): TP=17, TN=0, FP=25, FN=0.

Disagreement class: 20/25 misses are dyadic with n_attractors ≥ 2. The
other five are dyadic single-attractor forms whose cycle (or burn-in)
party mean differs from the uniform 0.5 reference (ensemble-measure
mismatch, not multi-basin polarization).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 agreement ≥0.65 on 42-form panel | **REFUTED** |
| H2 disagreements in dyadic×multi ≥0.75 | **SUPPORTED** |
| H3 sticky & maj3 are that class | **SUPPORTED** |
| H4 EoA ≤0.1× Φ wall-clock | **SUPPORTED** |
| H5a T∈{16,64,256} within ±0.10 | **SUPPORTED** |
| H5b noise 0.05 drift ≤0.15 | **SUPPORTED** |
| H5c S-only contrast / miss stable | **SUPPORTED** |

## Reading

T8's operational claim — EoA calibrates to Φ above a useful threshold —
holds on the designed G2 nine-form panel (7/9) and **fails** once the
panel widens to classifier, ejection, seeded-random n=3, and n=4 forms.
The stress result does not demote Φ: exact Φ still supplies the
literacy / algorithmacy cut the lab needs. What fails is using EoA alone
as a Φ proxy. EoA remains a cheap, well-specified instrument for
**ensemble-vs-trajectory divergence**; its disagreements with Φ
concentrate in the characterizable class dyadic × multi-attractor
(plus a smaller single-attractor ensemble-mismatch residue). That is the
calibration limit T8 must carry.

## Limits

Uniform-on-X ensemble; ε_div=0.1; τ=0.25; primary observables {W,C}
(n=3) / non-S parties (n=4). Seeded random palette is a thin slice of
the n=3 rule space. No real platform logs (G1 still open). Wall-clock
ratio is machine-dependent but the order-of-magnitude gap is not.

## Reproduce

```
python -m org_frontier.ergodicity.test_eoa
python org_frontier/studies/ergodic_eoa_instrument/analyze_stress.py
```
