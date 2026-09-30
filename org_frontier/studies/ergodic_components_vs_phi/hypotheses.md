# ergodic_components_vs_phi — hypotheses (fixed before computing)

**Question (Ergodicity × Algorithmacy track, Strand B).** On matched Boolean
coordination panels, do triadic forms (Φ_MIP > 0) differ from dyadic forms
(Φ_MIP = 0) in (i) number of ergodic components (attractors with nonempty
basins), (ii) basin entropy, and (iii) party-level |time average − ensemble
average|?

**Already known (cited, not reopened).**
- `studies/genuine_bistability/` — GENUINE_COEXISTENCE: some forms host
  triadic and dyadic attractors at fixed coupling; sticky #109 is
  MULTI_SAME plus activity hysteresis.
- Probe #43 / #109 — sticky mediator encodings and activity hysteresis.
- Stoch–temporal arc closed on noise / delay / CT proxy; this cell does not
  reopen those verdicts.
- Connaughton, Jeroen, and Paillusson (2026 working notes): on finite maps,
  ergodic components are tied to invariant sets / attractors; operational
  hierarchy is Metric Indecomposability > Equality of Distributions >
  Equality of Averages.

**Definitions (fixed).**
- An **attractor** is a fixed point or limit cycle of the synchronous Boolean
  map.
- An **ergodic component** for this cell is an attractor together with its
  basin (the set of states that reach it). Component count = number of
  attractors with basin size ≥ 1.
- **Basin entropy** = −∑_a (b_a / 2^n) log (b_a / 2^n) over attractors a with
  basin size b_a.
- **Party time–ensemble divergence** for party i on attractor a: absolute
  difference between the occupancy time average of bit i along a and the
  uniform average of bit i over the states of a (primary); secondary contrast
  uses the uniform average over the full 2^n state space.
- **Triadic / dyadic** at an attractor: max Φ_MIP over attractor states >
  PHI_EPS vs ≤ PHI_EPS (exact binary IIT-4.0). Whole-form verdict = lab
  classifier on the form.

**Panel (designed; candid).** Primary n=3 labels (W, S, C). Include at
minimum: memoryless triad, sticky, xor_memory, or_commit, parity_hub, maj3,
plus at least two known corpus dyadic forms and two known corpus triadic
forms. Exact membership list is frozen in the commit that adds
`analyze_components.py`, before that script is run.

**Instrument gate.** Faithful memoryless triad whole-form triadic;
sticky whole-form dyadic (matches #43). Abort the comparison if either gate
fails.

## H1 — component count tracks verdict

Mean ergodic-component count is higher for whole-form triadic forms than for
whole-form dyadic forms on the panel, by a pre-registered margin δ_c ≥ 0.5
components (or a one-sided permutation test at α = 0.05 if the panel is large
enough for a test).

Null: mean counts differ by less than δ_c (or test non-significant).

## H2 — basin entropy tracks verdict

Mean basin entropy is higher for triadic forms than for dyadic forms by
δ_h ≥ 0.1 bits (same testing rule as H1).

Null: difference below δ_h / non-significant.

## H3 — party time–ensemble divergence tracks active mediation

The fraction of (form, party, attractor) cells with divergence > ε_div
(ε_div = 0.1 occupancy) is higher among attractors of whole-form triadic forms
than among attractors of whole-form dyadic forms.

Null: fractions equal within a pre-registered tolerance, or higher for dyadic.

## H4 — coexistence implies cross-basin competence split

On every form that hosts both a triadic and a dyadic attractor (the
`genuine_bistability` coexistence class), party time averages differ across
those two attractors for at least one party by ≥ ε_div.

Null: coexistence forms show cross-basin party-average agreement within ε_div
for all parties.

**Primary verdict word.**
- H1 and H3 → `COMPONENTS_TRACK_TRIAD`
- H1 only → `COUNT_ONLY`
- H3 only → `DIVERGENCE_ONLY`
- H4 with coexistence present → report `CROSS_BASIN_SPLIT` as a secondary
  witness
- else → `NO_ERGODIC_SIGNATURE`

When H2 agrees with H1, note it as a magnitude witness; H2 alone does not
carry the primary word.

**Scope.** Exact binary IIT-4.0; designed Boolean forms; in-silico. Evidence
about models, not about real organizations. No numbers until
`analyze_components.py` exists, is committed after this file, and is run.
