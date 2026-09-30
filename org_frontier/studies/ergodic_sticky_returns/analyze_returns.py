"""Strand F4 — sticky return times / inactive basins.

Hypotheses fixed in hypotheses.md before computing.

Run:  python org_frontier/studies/ergodic_sticky_returns/analyze_returns.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.ergodicity._boolean_ergo import (
    find_attractors,
    inactive000_basin_mass,
    instrument_gates,
    mean_return_time_to_set,
    next_map,
    rules_memoryless,
    rules_or_commit,
    rules_parity_hub,
    rules_sticky,
    rules_sticky_or,
    rules_sticky_parity,
)
from org_frontier.probes import probe_hysteresis as hyst

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
HYST_GAP_MIN = 0.05
RATIO_MIN = 1.2

PAIRS = [
    ("memoryless", rules_memoryless, "sticky", rules_sticky),
    ("or_commit", rules_or_commit, "sticky_or", rules_sticky_or),
    ("parity_hub", rules_parity_hub, "sticky_parity", rules_sticky_parity),
]


def metrics(builder):
    rules = builder()
    nxt = next_map(rules)
    attrs = find_attractors(nxt)
    zero = {(0, 0, 0)}
    return {
        "inactive_mass": inactive000_basin_mass(attrs),
        "mean_return": mean_return_time_to_set(nxt, zero),
        "n_attr": len(attrs),
    }


def main():
    print("STRAND F4 — STICKY RETURN TIMES / INACTIVE BASINS")
    print("=" * 80)
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    t_all = time.time()
    gates = instrument_gates()
    print("INSTRUMENT CONTROL")
    print("-" * 80)
    print(
        f"  memoryless whole: {gates['memoryless'].structure} "
        f"Φ={gates['memoryless'].max_phi:.6f}  "
        f"{'PASS' if gates['ctrl_memoryless'] else 'FAIL'}"
    )
    print(
        f"  sticky whole:     {gates['sticky'].structure} "
        f"Φ={gates['sticky'].max_phi:.6f}  "
        f"{'PASS' if gates['ctrl_sticky'] else 'FAIL'}"
    )
    area_sticky, _, _ = hyst.loop_area(True)
    area_mem, _, _ = hyst.loop_area(False)
    hyst_gap = area_sticky - area_mem
    ctrl_hyst = hyst_gap >= HYST_GAP_MIN
    print(f"  #109 gap sticky−memoryless = {hyst_gap:.4f}  "
          f"{'PASS' if ctrl_hyst else 'FAIL'} (need ≥{HYST_GAP_MIN})")
    if not (gates["ok"] and ctrl_hyst):
        raise SystemExit("ABORT: instrument / #109 control failed")
    print()

    rows = []
    print("PAIRS")
    print("-" * 80)
    pair_ok = []
    for c_name, c_b, s_name, s_b in PAIRS:
        c_m = metrics(c_b)
        s_m = metrics(s_b)
        mass_gt = s_m["inactive_mass"] > c_m["inactive_mass"]
        if c_m["mean_return"] == float("inf") or s_m["mean_return"] == float("inf"):
            ratio = float("inf") if s_m["mean_return"] > c_m["mean_return"] else 0.0
            ratio_ok = s_m["mean_return"] >= RATIO_MIN * c_m["mean_return"] if c_m["mean_return"] != float("inf") else False
        else:
            ratio = s_m["mean_return"] / c_m["mean_return"] if c_m["mean_return"] > 0 else float("inf")
            ratio_ok = ratio >= RATIO_MIN
        ok = mass_gt or ratio_ok
        pair_ok.append(ok)
        row = {
            "convey": c_name,
            "sticky": s_name,
            "convey_mass": c_m["inactive_mass"],
            "sticky_mass": s_m["inactive_mass"],
            "convey_return": c_m["mean_return"],
            "sticky_return": s_m["mean_return"],
            "return_ratio": ratio if ratio != float("inf") else -1.0,
            "mass_gt": int(mass_gt),
            "ratio_ok": int(ratio_ok),
            "h1_pair": int(ok),
        }
        rows.append(row)
        print(
            f"  {c_name}→{s_name}: mass {c_m['inactive_mass']:.3f}→{s_m['inactive_mass']:.3f}  "
            f"return {c_m['mean_return']:.3f}→{s_m['mean_return']:.3f}  "
            f"ratio={ratio if ratio != float('inf') else 'inf'}  H1pair={ok}"
        )

    h1 = all(pair_ok)
    h2 = ctrl_hyst

    # H3: parity_hub return not ≥1.2× memoryless
    mem_r = next(r for r in rows if r["convey"] == "memoryless")["convey_return"]
    ph = metrics(rules_parity_hub)
    if mem_r > 0 and mem_r != float("inf") and ph["mean_return"] != float("inf"):
        ph_ratio = ph["mean_return"] / mem_r
    else:
        ph_ratio = float("inf")
    h3 = not (ph_ratio >= RATIO_MIN)

    if h1 and h2:
        verdict_word = "STICKY_FINITE_TRAP"
    elif h1:
        verdict_word = "BASIN_ONLY"
    elif h2:
        verdict_word = "HYSTERESIS_ONLY"
    else:
        verdict_word = "NO_STICKY_TRAP"

    reading = (
        f"{verdict_word} — H1 pairs={pair_ok}; hyst_gap={hyst_gap:.4f}; "
        f"parity_hub/memoryless return ratio={ph_ratio:.4f}"
    )

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (sticky enlarges mass or return): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (#109 hysteresis gap):            {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (parity_hub not sticky-like):     {'SUPPORTED' if h3 else 'REFUTED'}  "
          f"(ratio={ph_ratio:.4f})")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(
        f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
        f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
        f"H3={('SUPPORTED' if h3 else 'REFUTED')}"
    )
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "pairs.csv"), "w", newline="") as fh:
        fields = list(rows[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            out = dict(r)
            for k in ("convey_mass", "sticky_mass", "convey_return", "sticky_return", "return_ratio"):
                out[k] = f"{r[k]:.8f}"
            w.writerow(out)
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "hyst_gap": f"{hyst_gap:.8f}",
            "parity_hub_ratio": f"{ph_ratio:.8f}",
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
