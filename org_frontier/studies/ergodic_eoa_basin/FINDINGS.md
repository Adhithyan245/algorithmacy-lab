# ergodic_eoa_basin — findings

**Verdict: EOA_BASIN_INCONCLUSIVE.** The per-outcome fix clears the miss
classes that drove the prior `EOA_TRACKS_MI_NOT_PHI` result, but the
binary EoA↔Φ agreement test does not recover. Under both `basin` and
`stationary` at noise=0 every form on the frozen 42-form panel is
operational `AGREEING` (TP=0, TN=25, FP=0, FN=17; agree rate
**25/42 = 0.595**). That rate is the panel's dyadic base rate: the
binary instrument collapses and carries no Φ cut. The continuous
gap statistic still separates triadic from dyadic above chance under
`basin` (AUC **0.729**, Spearman ρ **0.330**, permutation p **0.025**),
so H4 passes while H3 fails — hence inconclusive rather than a clean
`EOA_FIX_NO_PHI_SIGNAL`. The pre-registered noise arm under `basin`
(`ε_flip=0.05`, G2 core) restores BREAKING on 4 forms and lifts G2
agreement from 0.222 to 0.667 (**H5 SUPPORTED**); that reintroduced
signal is not claimed to track Φ on the full panel.

In-silico Boolean forms only. Hypotheses fixed in `hypotheses.md` before
`analyze_basin.py`.

## What the fix does

| mode | reference | multi-attractor FPs | single-attractor mismatches | binary Φ agreement |
|---|---|---|---|---|
| `uniform` (prior) | mean of f on all starts | 20 false BREAKING | 5 false BREAKING | 17/42 |
| `basin` | mean of time averages within zero-noise basin | **20/20 rescued** | (also all AGREEING) | 25/42 |
| `stationary` | ∫f dμ_a on the attractor reached | (all AGREEING) | **5/5 rescued** | 25/42 |

Under deterministic dynamics, within-basin time averages coincide at long
T, and finite-T averages sit close to the cycle measure. The Equality-of-
Averages failure that the uniform instrument reported was almost entirely
cross-basin polarization (plus a smaller ensemble-measure mismatch). Once
those are removed, the binary BREAKING flag vanishes.

## Confusion and scores (noise=0, n=42)

| mode | TP | TN | FP | FN | agree | AUC(gap, triadic) | Spearman(gap, Φ) |
|---|---:|---:|---:|---:|---:|---:|---:|
| uniform | 17 | 0 | 25 | 0 | 0.405 | 0.493 | −0.014 (p=0.94) |
| basin | 0 | 25 | 0 | 17 | 0.595 | **0.729** | **0.330 (p=0.025)** |
| stationary | 0 | 25 | 0 | 17 | 0.595 | 0.707 | 0.273 (p=0.072) |

Residual gaps under the fix are small (typical gap_mean ≈ 0.005–0.02) and
reflect finite-T burn-in, not metric indecomposability. The basin-mode
AUC above 0.65 is a weak continuous association, not a usable binary
proxy for the literacy / algorithmacy cut.

## Noise arm (H5)

On the G2 core under `basin`, `ε_flip=0.05`, `T=64`: four forms flip
AGREEING→BREAKING (memoryless, xor_memory, or_commit, sticky_parity).
G2-core agreement moves from 0.222 to 0.667. Flip noise at finite T
reintroduces within-basin divergence of time averages; the arm confirms
the instrument can still emit BREAKING when trajectories mix across the
zero-noise partition. It does not restore a calibrated Φ proxy on the
42-form panel (noise arm was pre-registered on G2 core only).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 basin rescues ≥0.75 of prior dya×multi | **SUPPORTED** (20/20) |
| H2 stationary rescues ≥0.80 of prior dya×single | **SUPPORTED** (5/5) |
| H3 agreement ≥0.65 under basin or stationary | **REFUTED** (0.595 either mode) |
| H4 AUC≥0.65 or \|ρ\|≥0.30 under basin or stationary | **SUPPORTED** (basin AUC=0.729, ρ=0.330) |
| H5 basin noise arm restores a BREAKING signal | **SUPPORTED** (4 flips; Δagree=0.444) |

## Reading

T8's operational claim that EoA calibrates to Φ does not survive the
per-outcome correction. The uniform-ensemble instrument agreed with Φ
only insofar as it tracked multistability; once multistability is
conditioned out, binary EoA is all-AGREEING on this panel and the
agreement rate collapses to the dyadic base rate. Exact Φ still supplies
the literacy / algorithmacy cut. The residual continuous gap–Φ
association under `basin` is a secondary observation inside the
pre-registered H4 band; it does not license replacing Φ with fixed-
threshold EoA. The honest null named in the hypotheses — that the fix
may erase the Φ signal — holds for the binary verdict and fails only
for the continuous gap score.

## Limits

Same frozen panel, thresholds, and observables as
`ergodic_eoa_instrument`. Basin labels come from the zero-noise
partition even in the noise arm. Stationary-under-noise uses the unique
stationary of the flip-noise chain (global), which at finite T is a
harsh reference and was used only for the unit-test BREAKING control,
not for H1–H4. No real platform logs. Scope: in-silico Boolean forms.

## Reproduce

```
python -m org_frontier.ergodicity.test_eoa
python org_frontier/studies/ergodic_eoa_basin/analyze_basin.py
python org_frontier/studies/ergodic_eoa_basin/analyze_basin.py --ci
```
