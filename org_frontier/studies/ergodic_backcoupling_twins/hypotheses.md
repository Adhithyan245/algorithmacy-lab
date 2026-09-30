# ergodic_backcoupling_twins — hypotheses (fixed before computing)

**Question (Strand A4 / T1).** Can two environments share the same interface
surface and differ only in whether the mediating state depends on the user's
past — and does that single difference flip the literacy / algorithmacy
demand (whole-form Φ_MIP verdict)?

**Already known (cited, not reopened).**
- Probe #43 / #109: sticky mediator is whole-form dyadic (Φ=0); memoryless
  triad is whole-form triadic (Φ=2).
- `studies/genuine_bistability/`: sticky is MULTI_SAME; memoryless is COEXIST.
- Connaughton, Jeroen, and Paillusson (2026): skew product vs coupled product.

**Definitions (fixed).**
- **Convey twin:** mediator update independent of retained S beyond the current
  party convey (e.g. S' = W∧C). Skew-like in the mediator bit.
- **Accumulating twin:** mediator update depends on retained S
  (e.g. S' = (W∧C)∨S). Coupled.
- **Skew-factor present:** the Boolean rule for S' does not read the previous
  S bit (coefficient of S in the mediator rule is identically unused).
- **Verdict flip:** whole-form structure differs across a matched twin pair.

**Panel (frozen).** Three pairs, n=3 labels (W,S,C):
1. memoryless (S'=W∧C) vs sticky (S'=(W∧C)∨S)
2. or_commit (S'=W∨C) vs sticky_or (S'=(W∨C)∨S)
3. parity_hub (S'=W⊕C) vs sticky_parity (S'=(W⊕C)∨S)
Party reads fixed: W'=S, C'=S on every form.

**Instrument gate.** memoryless whole-form triadic Φ=2; sticky whole-form
dyadic Φ=0. Abort if either fails.

## H1 — skew factor tracks the convey / accumulate split

Every convey twin has skew-factor present; every accumulating twin has
skew-factor absent.

Null: any convey twin reads S, or any accumulating twin ignores S.

## H2 — verdict flips with back-coupling

At least one twin pair shows a whole-form verdict flip (triadic ↔ dyadic).

Null: all three pairs share the same whole-form verdict on both sides.

## H3 — accumulating ⇒ triadic (strong competence reading)

Every accumulating twin is whole-form triadic and every convey twin is
whole-form dyadic.

Null: any accumulating twin dyadic, or any convey twin triadic.
(Note: #43 already makes H3 unlikely; H3 is the strong claim T1's naive
reading invites, and a refutation is informative.)

**Primary verdict word.**
- H1 and H2 → `BACKCOUPLING_SPLITS` (structural criterion holds; Φ may or
  may not track the strong H3 reading)
- H1 and H3 → `SKEW_AND_PHI_ALIGN`
- H1 only → `SKEW_ONLY`
- else → `NO_BACKCOUPLING_SIGNATURE`

**Scope.** Exact binary IIT-4.0; designed Boolean twins; in-silico. Evidence
about models, not organizations. No numbers until `analyze_twins.py` exists,
is committed after this file, and is run.
