# Ergodic components vs Φ (track first cell)

Does attractor / basin structure — the ergodic components of a finite Boolean
map — differ systematically between triadic forms (Φ_MIP > 0) and dyadic forms
(Φ_MIP = 0)? Spec only. No results. Hypotheses are fixed in
[`hypotheses.md`](hypotheses.md) before any analysis script lands.

Track home: [`../../ergodicity/`](../../ergodicity/). Sibling: 
[`../genuine_bistability/`](../genuine_bistability/) (agenda #13,
GENUINE_COEXISTENCE).

## Status

**SPEC — not run.** No `analyze_*.py`, no `results/`, no FINDINGS. Numbers that
appear in future commits must come from a registered script and must not be
invented in prose first.

## Question (one line)

On matched Boolean coordination panels, do triadic forms show more ergodic
components (attractors / basins) and larger party-level time–ensemble
divergence than dyadic forms?

## Why it matters

Finite deterministic maps carry invariant measures on attractors; the ergodic
components are those attractors and their basins (Connaughton, Jeroen, and
Paillusson 2026 working notes §2). If triadic mediation is associated with
richer component structure or with party time averages that fail to match the
ensemble, non-ergodicity of party trajectories becomes a computable signature
of the competence the lab calls algorithmacy.

## Method (planned)

1. Validate the instrument on known controls (faithful memoryless triad
   triadic; a known dyadic form dyadic) before any comparison.
2. Build a designed panel of dyadic and triadic forms (reuse
   `genuine_bistability` encodings plus corpus landmarks; n=3 primary, n=4
   secondary if cheap).
3. Enumerate attractors (fixed points and limit cycles) and basin sizes under
   the synchronous Boolean map.
4. Evaluate exact binary IIT-4.0 Φ_MIP at attractor states (per-attractor), and
   record the whole-form classifier verdict.
5. For each party bit, compare time-average occupancy inside each basin to the
   ensemble average over the invariant measure on that attractor (and to the
   uniform average over state space as a secondary contrast).
6. Pre-register the decision rules in `hypotheses.md`; implement analysis only
   after that commit.

## Out of scope for this cell

Operational tests on real logs (Strand G), multiplicative growth (Strand C),
recommender RL (Strand H). Those need other instruments. This cell uses only
existing lab Φ / attractor machinery.

## Run (when implemented)

```
python org_frontier/studies/ergodic_components_vs_phi/analyze_components.py
```

(Script does not exist yet. Do not invent output.)
