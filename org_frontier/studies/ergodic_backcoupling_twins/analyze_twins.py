"""Strand A4 — convey vs accumulating Boolean twins.

Hypotheses fixed in hypotheses.md before computing.

Run:  python org_frontier/studies/ergodic_backcoupling_twins/analyze_twins.py
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
    instrument_gates,
    rules_memoryless,
    rules_or_commit,
    rules_parity_hub,
    rules_sticky,
    rules_sticky_or,
    rules_sticky_parity,
    skew_factor_s_independent,
    whole_verdict,
)

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

PAIRS = [
    ("memoryless", rules_memoryless, "sticky", rules_sticky),
    ("or_commit", rules_or_commit, "sticky_or", rules_sticky_or),
    ("parity_hub", rules_parity_hub, "sticky_parity", rules_sticky_parity),
]


def main():
    print("STRAND A4 — BACK-COUPLING TWINS (convey vs accumulating)")
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
    if not gates["ok"]:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rows = []
    print("TWINS")
    print("-" * 80)
    for c_name, c_build, a_name, a_build in PAIRS:
        c_rules = c_build()
        a_rules = a_build()
        c_skew = skew_factor_s_independent(c_rules)
        a_skew = skew_factor_s_independent(a_rules)
        c_v = whole_verdict(c_rules)
        a_v = whole_verdict(a_rules)
        flip = c_v.structure != a_v.structure
        row = {
            "convey": c_name,
            "accum": a_name,
            "convey_skew": int(c_skew),
            "accum_skew": int(a_skew),
            "convey_structure": c_v.structure,
            "convey_phi": float(c_v.max_phi),
            "accum_structure": a_v.structure,
            "accum_phi": float(a_v.max_phi),
            "verdict_flip": int(flip),
        }
        rows.append(row)
        print(
            f"  {c_name:<12} skew={c_skew} {c_v.structure} Φ={c_v.max_phi:.3f}  |  "
            f"{a_name:<12} skew={a_skew} {a_v.structure} Φ={a_v.max_phi:.3f}  "
            f"flip={flip}"
        )

    h1 = all(r["convey_skew"] == 1 and r["accum_skew"] == 0 for r in rows)
    h2 = any(r["verdict_flip"] == 1 for r in rows)
    h3 = all(
        r["accum_structure"] == "triadic" and r["convey_structure"] == "dyadic"
        for r in rows
    )

    if h1 and h3:
        verdict_word = "SKEW_AND_PHI_ALIGN"
    elif h1 and h2:
        verdict_word = "BACKCOUPLING_SPLITS"
    elif h1:
        verdict_word = "SKEW_ONLY"
    else:
        verdict_word = "NO_BACKCOUPLING_SIGNATURE"

    reading = (
        f"{verdict_word} — skew tracks convey/accumulate={h1}; "
        f"any Φ flip={h2}; strong accumulating⇒triadic={h3}"
    )

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (skew tracks split):              {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (at least one verdict flip):      {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (accum⇒triadic & convey⇒dyadic):  {'SUPPORTED' if h3 else 'REFUTED'}")
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
    with open(os.path.join(RESULTS, "twins.csv"), "w", newline="") as fh:
        fields = list(rows[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                **r,
                "convey_phi": f"{r['convey_phi']:.8f}",
                "accum_phi": f"{r['accum_phi']:.8f}",
            })
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
