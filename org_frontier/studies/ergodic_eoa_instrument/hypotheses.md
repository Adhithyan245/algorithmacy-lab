# ergodic_eoa_instrument — hypotheses (fixed before computing)

**Question (Strand G / T8 follow-on).** Can Equality-of-Averages be packaged
as a reusable instrument with a pre-registered decision rule, and does that
instrument agree with exact Φ_MIP on a wider stress panel than G2's nine
forms — with disagreements concentrated in a characterizable class?

**Already known (cited, not reopened).**
- G2 (`studies/ergodic_eoa_vs_phi/`): operational EoA agreed with Φ on 7/9
  forms; both misses were dyadic multi-attractor forms (sticky, maj3).
- Derived: on a finite map with ≥2 attractors, EoA fails for generic
  observables when starts mix across basins (THEORIES.md T8 sketch;
  Connaughton et al. hierarchy cited there).
- First-cell panel and instrument gates from
  `studies/ergodic_components_vs_phi/` and `ergodicity/_boolean_ergo.py`.

**Instrument (fixed interface; implemented after this commit).**
Module: `org_frontier/ergodicity/eoa.py`. Inputs: Boolean next-map (or rules),
observable `f`, initial-state ensemble, horizon `T`, noise level `ε_flip`.
Outputs: mean |time − ensemble| gap, gap SE, fail rate, and a binary verdict
`AGREEING` (ergodic-agreeing) vs `BREAKING` (EoA-breaking).

**Decision rule (frozen; not to be tuned after the stress run).**
- Per-trajectory fail: `|time_avg(f) − ensemble_mean(f)| > ε_div` with
  `ε_div = 0.1`.
- Form verdict: `BREAKING` if fail rate ≥ `τ = 0.25`; else `AGREEING`.
- Φ agreement: `BREAKING` ↔ whole-form triadic, or `AGREEING` ↔ dyadic.
- Primary observable set: party bits `{W, C}` (exclude mediator `S`), matching
  G2. Secondary sensitivity: `{S}` alone; all bits; parity `W⊕C`.
- Default ensemble: uniform on the state space. Secondary: basin-restricted
  (one start per attractor cycle only — expect AGREEING on deterministic
  cycles).
- Default horizon `T = 64`; noise `ε_flip = 0` (deterministic). Sensitivity
  grid: `T ∈ {16, 64, 256}`, `ε_flip ∈ {0, 0.01, 0.05}`.

**Panel (frozen; seeded where random).**
1. **G2 core (9):** memoryless, sticky, xor_memory, or_commit, sticky_or,
   sticky_parity, parity_hub, maj3, w_follows_c.
2. **Classifier library (5):** chat_dyad, gig_dyadic_model, ats_triad_mediator,
   ats_feedback_factors, gig_false_dyad.
3. **Absorbing / ejection (2):** ejected_latch, ejected_latch_or.
4. **Seeded random n=3 (20):** seed `20260930`; each node independently
   draws a 2-input Boolean from a fixed 8-gate palette
   `{AND, OR, XOR, NAND, NOR, XNOR, COPY0, COPY1}` with input pair drawn
   from `{(0,1),(0,2),(1,2)}`; reject forms identical to a named panel
   member.
5. **n=4 tractable (6):** and_pool, or_pool, maj_homog, chain_ws_c1c2,
   hub_s, dual_latch — exact Φ within seconds each (labels W,S,C1,C2).

Total designed+seeded: **42** forms. CI subset: G2 core + classifier +
ejection + unit-test controls (no random n=3, no n=4) via `--ci`.

**Instrument gate.** memoryless triadic Φ=2; sticky dyadic Φ=0. Abort if fail.
Unit-test controls (known answers, no Φ): (a) single full-cycle XOR ring —
expect AGREEING for bit-0 under uniform; (b) two absorbing fixed points with
polarized observable — expect BREAKING under mixed starts.

## H1 — agreement holds on the wider panel

On the full 42-form panel under the frozen primary settings, EoA↔Φ agreement
rate ≥ **0.65**, or equivalently a one-sided exact binomial test of
agreement vs p=0.5 at α=0.05.

Null: agreement rate < 0.65 and binomial p ≥ 0.05.

## H2 — disagreements concentrate in dyadic multi-attractor forms

Among forms where EoA and Φ disagree, the share with
`(whole_structure == dyadic) AND (n_attractors ≥ 2)` is ≥ **0.75**.

Null: that share < 0.75 (disagreements are scattered).

## H3 — G2 misses are the named witnesses of that class

Both sticky and maj3 are BREAKING × dyadic × multi-attractor under the
instrument; the FINDINGS name the mechanism (basin-polarized party
occupancy under a uniform ensemble).

Null: either form AGREEING, or either form triadic (gate abort).

## H4 — EoA is cheaper than exact Φ

Mean wall-clock of the EoA instrument (primary settings, excluding Φ) over
the G2 core nine forms is ≤ **0.1×** the mean wall-clock of
`classify_rules` / whole-form Φ on the same nine.

Null: EoA_time / Φ_time > 0.1.

## H5 — robustness / sensitivity (pre-registered contrasts)

(a) Agreement rate under `T ∈ {16, 64, 256}` at `ε_flip=0` stays within
**±0.10** of the primary (`T=64`) rate on the G2 core.
(b) Raising `ε_flip` to 0.05 changes the G2-core agreement rate by
**≤ 0.15** absolute.
(c) Switching the observable to mediator bit `S` alone drops agreement on
the G2 core by **≥ 0.10** relative to primary `{W,C}` OR leaves sticky/maj3
still BREAKING (observable choice matters or the miss class is stable).

Null for (a)/(b): drift exceeds the stated band. Null for (c): S-only
agreement within 0.10 of primary and sticky or maj3 flips to AGREEING.

**Primary verdict word.**
- H1 and H2 → `EOA_INSTRUMENT_AGREES_CLASS`
- H1 and not H2 → `EOA_AGREES_UNCLASSIFIED`
- not H1 and H2 → `EOA_TRACKS_MI_NOT_PHI`
- else → `EOA_PHI_STRESS_FAIL`

**Scope.** In-silico Boolean forms only. Evidence about the instrument and
the models; not about real organizations or platforms. No numbers until
`analyze_stress.py` runs after this commit.
