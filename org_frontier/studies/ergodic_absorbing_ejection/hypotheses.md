# ergodic_absorbing_ejection — hypotheses (fixed before computing)

**Question (Strand D4 / T5).** Can a Boolean coordination form with an
absorbing "ejected" mediator state reproduce extractive ejection as an
ergodic absorbing component?

**Already known (cited, not reopened).**
- `studies/ejection_order/` CO_EJECT_TO_OWNER; #110 path {W,S,C}→null→{S,P}.
- Absorbing sets on finite maps are ergodic components with exit rate 0
  (derived; Connaughton et al. 2026 working notes §2).

**Definitions (fixed).**
- **Ejected latch form (n=3):** W'=S, C'=S, S' = 0 if S=0 else (W∧C). Once
  the mediator is off, it stays off (absorbing inactive).
- **Pre-ejection contrast:** memoryless triad S'=W∧C (no latch).
- **Absorbing attractor:** exit rate from the attractor's state set under T
  is zero (every successor stays in the set) and the basin is nonempty.
- **Null-core / dyadic ejected:** max Φ_MIP on the ejected attractor ≤ PHI_EPS
  or major complex empty.

**Panel (frozen).** n=3: memoryless (contrast), ejected_latch (primary),
sticky (non-absorbing multistable control), ejected_latch_or
(S' = 0 if S=0 else W∨C). Labels (W,S,C).

**Instrument gate.** memoryless whole-form triadic Φ=2. Abort if fail.

## H1 — ejected latch hosts an absorbing inactive attractor

ejected_latch has an attractor contained in {states with S=0} that is
absorbing (exit rate 0) with basin size ≥ 1.

Null: no such attractor, or exit rate > 0.

## H2 — ejected attractor is dyadic / null-core; pre-ejection path triadic

On ejected_latch, the absorbing inactive attractor is dyadic (Φ_MIP ≤ EPS);
the memoryless contrast remains whole-form triadic. If ejected_latch also
hosts a non-ejected attractor, that attractor is triadic (Φ_MIP > EPS).

Null: ejected attractor triadic, or memoryless not triadic, or all
attractors of ejected_latch dyadic with no triadic witness on the contrast.

## H3 — sticky is not an absorbing-ejection witness

sticky (#43) does not satisfy H1's absorbing inactive pattern as a
sole absorbing component that erases all triadic attractors — it remains
MULTI_SAME / activity hysteresis, not extractive absorption.

Null: sticky matches the ejected_latch absorbing Φ pattern.

**Primary verdict word.**
- H1 and H2 → `ABSORBING_EJECTION`
- H1 only → `ABSORB_NO_PHI_SPLIT`
- else → `NO_ABSORBING_EJECTION`

**Scope.** Exact binary IIT-4.0; designed Boolean forms; in-silico. No
organization measured. No numbers until `analyze_absorb.py` runs after this
commit.
