# ergodic_eoa_vs_phi — hypotheses (fixed before computing)

**Question (Strand G2 / T8).** Does the operational Equality-of-Averages
verdict on synthetic trajectory "logs" agree with the lab's Φ_MIP verdict
on designed Boolean forms?

**Already known (cited, not reopened).**
- On finite maps with ≥2 attractors, EoA fails for generic observables when
  starts are mixed across basins (derived).
- First-cell panel and instrument gates from
  `studies/ergodic_components_vs_phi/`.

**Definitions (fixed).**
- **Synthetic log:** for each start state x∈{0,1}^n, the trajectory
  x, T(x), … until the attractor cycle is entered, then one full period
  (or N=64 steps max). Party observable f_i = bit i ∈ {W,C} (not S).
- **Ensemble mean:** uniform average of f_i over X (secondary: basin-weighted
  mixture of cycle means).
- **EoA fail** for a trajectory: |time avg − ensemble| > ε_div with
  ε_div = 0.1.
- **Form-level EoA fail rate:** fraction of (start, party) cells that fail.
- **Form operational verdict:** FAIL if fail rate ≥ 0.25; PASS otherwise.
- **Agreement:** operational FAIL ↔ whole-form triadic, or PASS ↔ dyadic.

**Panel (frozen).** Same nine forms as `ergodic_components_vs_phi`:
memoryless, sticky, xor_memory, or_commit, sticky_or, sticky_parity,
parity_hub, maj3, w_follows_c. Labels (W,S,C).

**Instrument gate.** memoryless triadic Φ=2; sticky dyadic Φ=0. Abort if fail.

## H1 — agreement above chance

Agreement rate across the nine forms ≥ 7/9 (≈0.778), or equivalently
strictly above 0.5 with a one-sided exact binomial test at α=0.05 favoring
agreement.

Null: agreement ≤ 5/9 (at or below chance-ish on this small N).

## H2 — multi-attractor forms fail EoA more often

Mean form-level fail rate among forms with n_attractors ≥ 2 exceeds mean
fail rate among SINGLE forms by ≥ 0.15.

Null: difference < 0.15.

## H3 — sticky (dyadic, multi) is the informative disagreement cell

If sticky is operational FAIL and whole-form dyadic, that disagreement is
reported as a named witness that MI/EoA can fire without triadic Φ — a
limit of using EoA alone as a Φ proxy.

Null: sticky PASS, or sticky triadic (gate would have aborted).

**Primary verdict word.**
- H1 → `EOA_AGREES_PHI`
- H1 false and H2 → `EOA_TRACKS_MI_NOT_PHI`
- else → `EOA_PHI_DISAGREE`

**Scope.** Synthetic logs from designed Boolean forms only. Calibrates the
operational instrument against exact Φ in-silico; does not measure real
platforms. No numbers until `analyze_eoa.py` runs after this commit.
