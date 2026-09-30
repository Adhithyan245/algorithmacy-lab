# ergodic_sticky_returns — hypotheses (fixed before computing)

**Question (Strand F4 / T7).** Can a Boolean sticky mediator be read as a
finite-state analogue of a neutral sticky point, and does its basin structure
predict engagement hysteresis (longer returns / larger inactive basins)?

**Already known (cited, not reopened).**
- Probe #109 / #43: sticky activity hysteresis gap ≥ 0.05 vs memoryless.
- `genuine_bistability`: sticky MULTI_SAME (both dyadic); memoryless COEXIST.

**Definitions (fixed).**
- **Inactive set:** states with all bits 0, or (secondary) states with S=0.
- **Return time** from state x to inactive set I: min t≥1 with T^t(x)∈I,
  or ∞ if never. Mean return time = average of finite return times over
  start states that eventually hit I (exclude states that never return).
- **Inactive basin mass:** basin size of attractors contained in I,
  divided by 2^n.

**Panel (frozen).** Pairs: memoryless vs sticky; or_commit vs sticky_or;
parity_hub vs sticky_parity. Labels (W,S,C).

**Instrument gate.** #109 hysteresis gap sticky−memoryless ≥ 0.05; memoryless
triadic Φ=2; sticky dyadic Φ=0. Abort if any fails.

## H1 — sticky enlarges inactive basin mass

For every matched pair, sticky inactive-basin mass (attractor in {000}) is
strictly greater than the convey twin's, OR sticky mean return time to {000}
is ≥ 1.2× the convey twin's (when both means are finite).

Null: sticky mass ≤ convey and return-time ratio < 1.2 on any pair.

## H2 — #109 gap remains the activity-hysteresis witness

sticky−memoryless hysteresis area gap ≥ 0.05 (reproduce #109 control).

Null: gap < 0.05.

## H3 — return-time signature is specific to sticky latch, not all multistable

parity_hub (SINGLE, triadic) does not show longer mean return to {000} than
memoryless by the 1.2× margin (control that multistability alone ≠ sticky
return signature).

Null: parity_hub ≥ 1.2× memoryless return time.

**Primary verdict word.**
- H1 and H2 → `STICKY_FINITE_TRAP`
- H1 only → `BASIN_ONLY`
- H2 only → `HYSTERESIS_ONLY`
- else → `NO_STICKY_TRAP`

**Scope.** Finite Boolean caricature only — not a claim of infinite
ergodicity. In-silico. No numbers until `analyze_returns.py` runs after this
commit.
