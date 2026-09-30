# ergodic_sticky_returns — findings

**Verdict: HYSTERESIS_ONLY.** The #109 activity-hysteresis gap
sticky−memoryless = **0.0661** (≥ 0.05) remains (**H2 SUPPORTED**).
Sticky does **not** enlarge inactive-{000} basin mass or lengthen mean
return time to {000} on any matched pair (**H1 REFUTED**). Masses:
memoryless/sticky both **0.375**; or_commit/sticky_or both **0.125**
(neither ever returns to 000 from some starts — mean return ∞);
parity_hub mass **1.000** → sticky_parity **0.250** (sticky
*shrinks* inactive mass). H3 (parity_hub not sticky-like on returns)
**REFUTED**: parity_hub/memoryless return ratio = **2.4286** ≥ 1.2
(parity_hub's sole attractor is 000 with Φ=0.5, so return statistics
are dominated by that global sink).

In-silico; finite Boolean caricature only. Hypotheses fixed in
`hypotheses.md`.

## Pairs

| convey → sticky | mass | return | ratio | H1 pair |
|---|---|---|---:|---|
| memoryless → sticky | 0.375 → 0.375 | 1.000 → 1.000 | 1.000 | no |
| or_commit → sticky_or | 0.125 → 0.125 | ∞ → ∞ | — | no |
| parity_hub → sticky_parity | 1.000 → 0.250 | 2.429 → 1.000 | 0.412 | no |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 sticky enlarges mass or return | **REFUTED** |
| H2 #109 hysteresis gap | **SUPPORTED** |
| H3 parity_hub not sticky-like | **REFUTED** |

## Reading

T7's return-time / inactive-basin clause is **refuted** on this panel.
Sticky's finite signature here is activity hysteresis (#109), not a
larger inactive trap. The infinite-ergodicity analogy needs a different
finite observable than {000}-return on these encodings.

## Limits

n=3; inactive set = {000} only; no session-log heavy tails (F1–F3).

## Reproduce

```
python org_frontier/studies/ergodic_sticky_returns/analyze_returns.py
```
