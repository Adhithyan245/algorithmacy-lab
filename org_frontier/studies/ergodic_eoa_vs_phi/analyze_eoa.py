"""Strand G2 — operational EoA on synthetic logs vs Φ_MIP.

Hypotheses fixed in hypotheses.md before computing.

Run:  python org_frontier/studies/ergodic_eoa_vs_phi/analyze_eoa.py
"""

from __future__ import annotations

import csv
import math
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.ergodicity._boolean_ergo import (
    LABELS3,
    N3,
    PANEL_B1,
    find_attractors,
    instrument_gates,
    next_map,
    party_cycle_avg,
    party_uniform_avg,
    whole_verdict,
)

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
EPS_DIV = 0.1
FAIL_RATE_THRESH = 0.25


def binomial_sf(k, n, p=0.5):
    """One-sided P(X >= k) for X~Bin(n,p)."""
    # exact sum
    total = 0.0
    for i in range(k, n + 1):
        total += math.comb(n, i) * (p**i) * ((1 - p) ** (n - i))
    return total


def trajectory_party_avg(nxt, start, party_idx, max_steps=64):
    """Time average of party bit along trajectory until one full cycle after entry."""
    cur = start
    seen = {}
    path = []
    t = 0
    while cur not in seen and t < max_steps:
        seen[cur] = t
        path.append(cur)
        cur = nxt[cur]
        t += 1
    if cur in seen:
        # append one full period
        cycle_start = seen[cur]
        cycle = path[cycle_start:]
        # burn-in + one cycle
        series = path + cycle
    else:
        series = path
    if not series:
        return 0.0
    return sum(st[party_idx] for st in series) / float(len(series))


def main():
    print("STRAND G2 — EoA ON SYNTHETIC LOGS vs Φ_MIP")
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

    form_rows = []
    print("FORMS")
    print("-" * 80)
    print(f"  {'form':<16} {'whole':<8} {'n_a':>3} {'fail':>6} {'op':<4} agree")

    for name, builder in PANEL_B1.items():
        rules = builder()
        nxt = next_map(rules)
        attrs = find_attractors(nxt)
        whole = whole_verdict(rules)
        # ensemble = uniform on X for party bits
        n_fail = 0
        n_cells = 0
        for s in range(2**N3):
            start = tuple((s >> i) & 1 for i in range(N3))
            for party_idx, lab in enumerate(LABELS3):
                if lab == "S":
                    continue
                t_avg = trajectory_party_avg(nxt, start, party_idx)
                ens = party_uniform_avg(N3, party_idx)
                n_cells += 1
                if abs(t_avg - ens) > EPS_DIV:
                    n_fail += 1
        fail_rate = n_fail / n_cells if n_cells else 0.0
        op = "FAIL" if fail_rate >= FAIL_RATE_THRESH else "PASS"
        agree = (op == "FAIL" and whole.structure == "triadic") or (
            op == "PASS" and whole.structure == "dyadic"
        )
        form_rows.append({
            "form": name,
            "whole_structure": whole.structure,
            "whole_phi": float(whole.max_phi),
            "n_attractors": len(attrs),
            "fail_rate": fail_rate,
            "op_verdict": op,
            "agree": int(agree),
        })
        print(
            f"  {name:<16} {whole.structure:<8} {len(attrs):>3} "
            f"{fail_rate:>6.3f} {op:<4} {agree}"
        )

    n = len(form_rows)
    n_agree = sum(r["agree"] for r in form_rows)
    agree_rate = n_agree / n
    p_binom = binomial_sf(n_agree, n, 0.5)
    h1 = (n_agree >= 7) or (agree_rate > 0.5 and p_binom < 0.05)

    multi = [r for r in form_rows if r["n_attractors"] >= 2]
    single = [r for r in form_rows if r["n_attractors"] < 2]
    mean_multi = (
        sum(r["fail_rate"] for r in multi) / len(multi) if multi else float("nan")
    )
    mean_single = (
        sum(r["fail_rate"] for r in single) / len(single) if single else float("nan")
    )
    h2 = (mean_multi - mean_single) >= 0.15 if single else mean_multi >= 0.15

    sticky = next(r for r in form_rows if r["form"] == "sticky")
    h3 = sticky["op_verdict"] == "FAIL" and sticky["whole_structure"] == "dyadic"

    if h1:
        verdict_word = "EOA_AGREES_PHI"
    elif (not h1) and h2:
        verdict_word = "EOA_TRACKS_MI_NOT_PHI"
    else:
        verdict_word = "EOA_PHI_DISAGREE"

    reading = (
        f"{verdict_word} — agree={n_agree}/{n} ({agree_rate:.3f}); "
        f"p_binom_one_sided={p_binom:.4f}; "
        f"fail_rate multi={mean_multi:.3f} single={mean_single:.3f}; "
        f"sticky op={sticky['op_verdict']} (dyadic FAIL witness={h3})"
    )

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  agreement: {n_agree}/{n} = {agree_rate:.3f}  "
          f"binom P(X≥k|p=0.5)={p_binom:.4f}")
    print(f"  H1 (EoA agrees with Φ):              {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (multi-attractor fail rate higher):{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (sticky FAIL×dyadic witness):     {'SUPPORTED' if h3 else 'REFUTED'}")
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
    with open(os.path.join(RESULTS, "forms.csv"), "w", newline="") as fh:
        fields = list(form_rows[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in form_rows:
            w.writerow({
                **r,
                "whole_phi": f"{r['whole_phi']:.8f}",
                "fail_rate": f"{r['fail_rate']:.8f}",
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "n_agree": n_agree,
            "n_forms": n,
            "agree_rate": f"{agree_rate:.6f}",
            "p_binom": f"{p_binom:.6f}",
            "mean_fail_multi": f"{mean_multi:.6f}",
            "mean_fail_single": f"{mean_single:.6f}",
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
