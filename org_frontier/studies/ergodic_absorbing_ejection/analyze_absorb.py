"""Strand D4 — absorbing ejected mediator as ergodic component.

Hypotheses fixed in hypotheses.md before computing.

Run:  python org_frontier/studies/ergodic_absorbing_ejection/analyze_absorb.py
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

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.ergodicity._boolean_ergo import (
    LABELS3,
    attractor_phi,
    find_attractors,
    instrument_gates,
    next_map,
    rules_ejected_latch,
    rules_ejected_latch_or,
    rules_memoryless,
    rules_sticky,
    whole_verdict,
)

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

FORMS = {
    "memoryless": rules_memoryless,
    "ejected_latch": rules_ejected_latch,
    "ejected_latch_or": rules_ejected_latch_or,
    "sticky": rules_sticky,
}


def exit_rate(nxt, cyc):
    """Fraction of cycle states whose successor leaves the cycle set."""
    cset = set(cyc)
    leave = 0
    for st in cyc:
        if nxt[st] not in cset:
            leave += 1
    return leave / float(len(cyc))


def main():
    print("STRAND D4 — ABSORBING EJECTED MEDIATOR")
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
    if not gates["ctrl_memoryless"]:
        raise SystemExit("ABORT: instrument control failed")
    print()

    form_rows = []
    attr_rows = []
    print("PANEL")
    print("-" * 80)
    for name, builder in FORMS.items():
        rules = builder()
        nxt = next_map(rules)
        attrs = find_attractors(nxt)
        whole = whole_verdict(rules)
        print(f"  {name}: whole={whole.structure} Φ={whole.max_phi:.3f} n_attr={len(attrs)}")
        for idx, (cyc, basin) in enumerate(attrs):
            verdict, max_phi, _ = attractor_phi(rules, cyc)
            er = exit_rate(nxt, cyc)
            inactive = all(st[1] == 0 for st in cyc)  # S=0 on cycle
            zero_state = all(sum(st) == 0 for st in cyc)
            attr_rows.append({
                "form": name,
                "attr_id": idx,
                "cycle": "|".join("".join(str(b) for b in st) for st in cyc),
                "basin": len(basin),
                "exit_rate": er,
                "absorbing": int(er == 0.0),
                "inactive_S0": int(inactive),
                "all_zero": int(zero_state),
                "verdict": verdict,
                "max_phi": max_phi,
            })
            print(
                f"    attr{idx}: {verdict} basin={len(basin)} exit={er:.2f} "
                f"S0={inactive} Φmax={max_phi:.4f} "
                f"cycle={'|'.join(''.join(str(b) for b in st) for st in cyc)}"
            )
        form_rows.append({
            "form": name,
            "whole_structure": whole.structure,
            "whole_phi": float(whole.max_phi),
            "n_attractors": len(attrs),
        })

    # H1: ejected_latch has absorbing inactive (S=0) attractor
    ej = [r for r in attr_rows if r["form"] == "ejected_latch"]
    h1 = any(r["absorbing"] == 1 and r["inactive_S0"] == 1 and r["basin"] >= 1 for r in ej)

    # H2: that attractor dyadic; memoryless whole triadic; if non-ejected attr exists, triadic
    mem_whole = next(r for r in form_rows if r["form"] == "memoryless")
    ej_abs = [r for r in ej if r["absorbing"] == 1 and r["inactive_S0"] == 1]
    ej_abs_dya = all(r["verdict"] == "dyadic" or r["max_phi"] <= PHI_EPS for r in ej_abs) if ej_abs else False
    ej_other = [r for r in ej if not (r["absorbing"] == 1 and r["inactive_S0"] == 1)]
    # If there is a non-ejected attractor, require it triadic; else contrast is memoryless
    if ej_other:
        other_tri = any(r["verdict"] == "triadic" for r in ej_other)
    else:
        other_tri = True  # rely on memoryless contrast
    h2 = (
        h1
        and ej_abs_dya
        and mem_whole["whole_structure"] == "triadic"
        and other_tri
    )

    # H3: sticky is not the absorbing-ejection witness
    st = [r for r in attr_rows if r["form"] == "sticky"]
    # sticky matches pattern if it has absorbing S=0 attractor that is the sole story erasing triadic
    sticky_abs_inactive = [r for r in st if r["absorbing"] == 1 and r["inactive_S0"] == 1]
    sticky_has_tri = any(r["verdict"] == "triadic" for r in st)
    sticky_matches = bool(sticky_abs_inactive) and not sticky_has_tri and all(
        r["verdict"] == "dyadic" for r in st
    )
    # H3 says sticky does NOT match ejected_latch pattern as extractive absorption.
    # Sticky IS multi-same dyadic with absorbing fixed points — need careful read.
    # Hypothesis: sticky does not satisfy H1's pattern as sole absorbing component that
    # erases all triadic attractors — it remains MULTI_SAME. Both sticky attractors are
    # absorbing fixed points (exit 0). Distinguisher: ejected_latch has ALL-S0 absorbing
    # component entered by turning S off; sticky also has 111 attractor (active latch).
    # H3 SUPPORTED if sticky hosts an active (S=1) attractor in addition to inactive —
    # i.e. not a one-way ejection into inactivity only.
    sticky_active = any(r["inactive_S0"] == 0 for r in st)
    h3 = sticky_active  # not a pure ejection-into-inactive witness

    if h1 and h2:
        verdict_word = "ABSORBING_EJECTION"
    elif h1:
        verdict_word = "ABSORB_NO_PHI_SPLIT"
    else:
        verdict_word = "NO_ABSORBING_EJECTION"

    reading = (
        f"{verdict_word} — ejected_latch absorbing inactive={h1}; "
        f"Φ split={h2}; sticky not pure ejection={h3}"
    )

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (absorbing inactive on ejected_latch): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (ejected dyadic / pre-ejection triadic):{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (sticky ≠ absorbing-ejection witness): {'SUPPORTED' if h3 else 'REFUTED'}")
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
    with open(os.path.join(RESULTS, "attractors.csv"), "w", newline="") as fh:
        fields = list(attr_rows[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in attr_rows:
            w.writerow({**r, "exit_rate": f"{r['exit_rate']:.8f}",
                        "max_phi": f"{r['max_phi']:.8f}"})
    with open(os.path.join(RESULTS, "forms.csv"), "w", newline="") as fh:
        fields = list(form_rows[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in form_rows:
            w.writerow({**r, "whole_phi": f"{r['whole_phi']:.8f}"})
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
