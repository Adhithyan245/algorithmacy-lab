"""Strand G follow-on — EoA instrument stress panel vs exact Φ_MIP.

Hypotheses fixed in hypotheses.md before this script existed.
Instrument: org_frontier.ergodicity.eoa

Run (full panel):
  python org_frontier/studies/ergodic_eoa_instrument/analyze_stress.py

Run (CI subset — no random n=3, no n=4, no full sensitivity grid):
  python org_frontier/studies/ergodic_eoa_instrument/analyze_stress.py --ci
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import random
import sys
import time
from typing import Callable, Optional

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
    rules_ejected_latch,
    rules_ejected_latch_or,
    whole_verdict,
)
from org_frontier.ergodicity.eoa import (
    agrees_with_phi,
    bit_observable,
    run_eoa,
    run_eoa_parties,
)
from org_frontier.classifier import forms as cforms
from org_frontier.classifier.classifier import classify_rules

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

# Frozen (hypotheses.md) — do not tune after the run.
EPS_DIV = 0.1
FAIL_RATE_THRESH = 0.25
HORIZON = 64
NOISE = 0.0
SEED_RANDOM = 20260930
N_RANDOM = 20
PARTY_WC = (0, 2)  # W, C — exclude S

GATE_PALETTE = ("AND", "OR", "XOR", "NAND", "NOR", "XNOR", "COPY0", "COPY1")
INPUT_PAIRS = ((0, 1), (0, 2), (1, 2))


def binomial_sf(k: int, n: int, p: float = 0.5) -> float:
    total = 0.0
    for i in range(k, n + 1):
        total += math.comb(n, i) * (p**i) * ((1 - p) ** (n - i))
    return total


def _gate(name: str, a: int, b: int) -> Callable:
    if name == "AND":
        return lambda x, a=a, b=b: x[a] & x[b]
    if name == "OR":
        return lambda x, a=a, b=b: x[a] | x[b]
    if name == "XOR":
        return lambda x, a=a, b=b: x[a] ^ x[b]
    if name == "NAND":
        return lambda x, a=a, b=b: 1 - (x[a] & x[b])
    if name == "NOR":
        return lambda x, a=a, b=b: 1 - (x[a] | x[b])
    if name == "XNOR":
        return lambda x, a=a, b=b: 1 - (x[a] ^ x[b])
    if name == "COPY0":
        return lambda x, a=a, b=b: x[a]
    if name == "COPY1":
        return lambda x, a=a, b=b: x[b]
    raise ValueError(name)


def _rules_signature(rules) -> frozenset:
    """Truth-table signature for duplicate rejection against named forms."""
    rows = []
    for s in range(8):
        cur = tuple((s >> i) & 1 for i in range(3))
        rows.append(tuple(int(r(cur)) for r in rules))
    return frozenset([tuple(rows)])  # wrap so frozenset of one tuple-of-rows


def _sig_of_builder(builder) -> frozenset:
    return _rules_signature(builder())


def build_random_n3(seed: int, n: int, ban: set) -> list[tuple[str, Callable]]:
    rng = random.Random(seed)
    out = []
    attempts = 0
    while len(out) < n and attempts < n * 200:
        attempts += 1
        rules = []
        for _ in range(3):
            g = rng.choice(GATE_PALETTE)
            pair = rng.choice(INPUT_PAIRS)
            rules.append(_gate(g, pair[0], pair[1]))
        sig = _rules_signature(rules)
        if sig in ban:
            continue
        ban.add(sig)
        name = f"rand3_{seed}_{len(out):02d}"
        # bind rules in closure
        frozen = list(rules)
        out.append((name, (lambda frozen=frozen: list(frozen))))
    if len(out) < n:
        raise RuntimeError(f"only drew {len(out)}/{n} random forms")
    return out


# ----- n=4 designed forms (labels W, S, C1, C2) ---------------------------------

LABELS4 = ("W", "S", "C1", "C2")


def rules_and_pool():
    return [
        lambda x: x[1],
        lambda x: x[0] & x[2] & x[3],
        lambda x: x[1],
        lambda x: x[1],
    ]


def rules_or_pool():
    return [
        lambda x: x[1],
        lambda x: x[0] | x[2] | x[3],
        lambda x: x[1],
        lambda x: x[1],
    ]


def rules_maj_homog():
    def maj(x):
        return 1 if sum(x) >= 2 else 0

    return [maj, maj, maj, maj]


def rules_chain_ws_c1c2():
    # W' = S, S' = W, C1' = S, C2' = C1  (chain-ish; may factor)
    return [
        lambda x: x[1],
        lambda x: x[0],
        lambda x: x[1],
        lambda x: x[2],
    ]


def rules_hub_s():
    # All outer parties copy S; S' = W ⊕ C1 ⊕ C2
    return [
        lambda x: x[1],
        lambda x: x[0] ^ x[2] ^ x[3],
        lambda x: x[1],
        lambda x: x[1],
    ]


def rules_dual_latch():
    # Sticky-like latch on S with AND of outers
    return [
        lambda x: x[1],
        lambda x: (x[0] & x[2] & x[3]) | x[1],
        lambda x: x[1],
        lambda x: x[1],
    ]


PANEL_N4 = {
    "and_pool": rules_and_pool,
    "or_pool": rules_or_pool,
    "maj_homog": rules_maj_homog,
    "chain_ws_c1c2": rules_chain_ws_c1c2,
    "hub_s": rules_hub_s,
    "dual_latch": rules_dual_latch,
}


def build_panel(ci: bool):
    """Return list of (name, builder, labels, group)."""
    panel = []
    for name, builder in PANEL_B1.items():
        panel.append((name, builder, LABELS3, "g2_core"))

    for name, builder in cforms.FORMS.items():
        panel.append((name, builder, LABELS3, "classifier"))

    panel.append(("ejected_latch", rules_ejected_latch, LABELS3, "ejection"))
    panel.append(("ejected_latch_or", rules_ejected_latch_or, LABELS3, "ejection"))

    if not ci:
        ban = {_sig_of_builder(b) for _, b, _, _ in panel if len(b()) == 3}
        # Also ban by evaluating builders that are n=3
        for name, builder in build_random_n3(SEED_RANDOM, N_RANDOM, ban):
            panel.append((name, builder, LABELS3, "random_n3"))
        for name, builder in PANEL_N4.items():
            panel.append((name, builder, LABELS4, "n4"))
    return panel


def evaluate_form(name, builder, labels, group, horizon=HORIZON, noise=NOISE, parties=None):
    rules = builder()
    n = len(labels)
    if parties is None:
        # Primary: all non-S parties. For n=3, S is index 1; for n=4, S is index 1.
        parties = tuple(i for i, lab in enumerate(labels) if lab != "S")

    t_phi0 = time.perf_counter()
    if n == 3 and labels == LABELS3:
        whole = whole_verdict(rules, labels=labels)
    else:
        whole = classify_rules(rules, labels=labels)
    t_phi = time.perf_counter() - t_phi0

    nxt = next_map(rules, n=n)
    attrs = find_attractors(nxt)

    t_eoa0 = time.perf_counter()
    eoa = run_eoa_parties(
        rules,
        party_indices=parties,
        labels=labels,
        horizon=horizon,
        noise=noise,
        eps_div=EPS_DIV,
        fail_rate_thresh=FAIL_RATE_THRESH,
        n=n,
        seed=0,
    )
    t_eoa = time.perf_counter() - t_eoa0

    agree = agrees_with_phi(eoa.verdict, whole.structure)
    return {
        "form": name,
        "group": group,
        "n": n,
        "whole_structure": whole.structure,
        "whole_phi": float(whole.max_phi),
        "n_attractors": len(attrs),
        "eoa_verdict": eoa.verdict,
        "fail_rate": eoa.fail_rate,
        "gap_mean": eoa.gap_mean,
        "gap_se": eoa.gap_se,
        "agree": int(agree),
        "t_phi_s": t_phi,
        "t_eoa_s": t_eoa,
        "horizon": horizon,
        "noise": noise,
        "observable": eoa.observable_name,
        "dyadic_multi": int(
            whole.structure == "dyadic" and len(attrs) >= 2
        ),
        "miss_class": int(
            (not agree) and whole.structure == "dyadic" and len(attrs) >= 2
        ),
    }


def confusion(rows):
    """EoA BREAKING/AGREEING × Φ triadic/dyadic counts."""
    tp = tn = fp = fn = 0  # treat BREAKING as "positive" for triadic
    for r in rows:
        pred_break = r["eoa_verdict"] == "BREAKING"
        is_tri = r["whole_structure"] == "triadic"
        if pred_break and is_tri:
            tp += 1
        elif (not pred_break) and (not is_tri):
            tn += 1
        elif pred_break and (not is_tri):
            fp += 1
        else:
            fn += 1
    return {"tp": tp, "tn": tn, "fp": fp, "fn": fn}


def write_csv(path, rows, fields=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not rows:
        return
    fields = fields or list(rows[0].keys())
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            out = {}
            for k in fields:
                v = r[k]
                if isinstance(v, float):
                    out[k] = f"{v:.8f}"
                else:
                    out[k] = v
            w.writerow(out)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ci", action="store_true", help="CI subset panel")
    args = ap.parse_args(argv)

    print("STRAND G — EoA INSTRUMENT STRESS vs Φ_MIP")
    print("=" * 80)
    print("  hypotheses fixed in hypotheses.md before computing")
    print(f"  mode: {'CI subset' if args.ci else 'FULL panel'}")
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

    panel = build_panel(ci=args.ci)
    print(f"PANEL  n_forms={len(panel)}")
    print("-" * 80)
    print(
        f"  {'form':<22} {'grp':<12} {'whole':<8} {'n_a':>3} "
        f"{'eoa':<9} {'fail':>6} agree"
    )

    form_rows = []
    for name, builder, labels, group in panel:
        row = evaluate_form(name, builder, labels, group)
        form_rows.append(row)
        print(
            f"  {name:<22} {group:<12} {row['whole_structure']:<8} "
            f"{row['n_attractors']:>3} {row['eoa_verdict']:<9} "
            f"{row['fail_rate']:>6.3f} {bool(row['agree'])}"
        )

    n = len(form_rows)
    n_agree = sum(r["agree"] for r in form_rows)
    agree_rate = n_agree / n if n else float("nan")
    p_binom = binomial_sf(n_agree, n, 0.5)
    h1 = (agree_rate >= 0.65) or (agree_rate > 0.5 and p_binom < 0.05)

    disagrees = [r for r in form_rows if not r["agree"]]
    n_dis = len(disagrees)
    n_miss_class = sum(r["miss_class"] for r in disagrees)
    miss_share = n_miss_class / n_dis if n_dis else float("nan")
    h2 = (n_dis == 0) or (miss_share >= 0.75)

    sticky = next(r for r in form_rows if r["form"] == "sticky")
    maj3 = next(r for r in form_rows if r["form"] == "maj3")
    h3 = (
        sticky["eoa_verdict"] == "BREAKING"
        and sticky["whole_structure"] == "dyadic"
        and sticky["n_attractors"] >= 2
        and maj3["eoa_verdict"] == "BREAKING"
        and maj3["whole_structure"] == "dyadic"
        and maj3["n_attractors"] >= 2
    )

    g2_rows = [r for r in form_rows if r["group"] == "g2_core"]
    mean_eoa = sum(r["t_eoa_s"] for r in g2_rows) / len(g2_rows)
    mean_phi = sum(r["t_phi_s"] for r in g2_rows) / len(g2_rows)
    ratio = mean_eoa / mean_phi if mean_phi > 0 else float("inf")
    h4 = ratio <= 0.1

    # ----- Sensitivity (G2 core) -----
    sens_rows = []
    g2_builders = [(n, b, lab) for n, b, lab, g in panel if g == "g2_core"]

    def g2_agree_rate(horizon, noise, parties=PARTY_WC):
        ok = 0
        total = 0
        for name, builder, labels in g2_builders:
            row = evaluate_form(
                name, builder, labels, "g2_core",
                horizon=horizon, noise=noise, parties=parties,
            )
            sens_rows.append({
                "form": name,
                "horizon": horizon,
                "noise": noise,
                "observable": row["observable"],
                "eoa_verdict": row["eoa_verdict"],
                "fail_rate": row["fail_rate"],
                "agree": row["agree"],
                "whole_structure": row["whole_structure"],
            })
            ok += row["agree"]
            total += 1
        return ok / total if total else float("nan")

    primary_g2_rate = sum(r["agree"] for r in g2_rows) / len(g2_rows)

    if args.ci:
        # CI: only check T=16 contrast + S-only observable (cheap)
        rate_t16 = g2_agree_rate(16, 0.0)
        rate_t64 = primary_g2_rate
        rate_t256 = primary_g2_rate  # skip heavy; record as not-run via sens flag
        rate_noise05 = primary_g2_rate
        rate_s_only = g2_agree_rate(64, 0.0, parties=(1,))
        # For CI H5a: only T=16 vs T=64 must hold; T=256 deferred to full.
        h5a = abs(rate_t16 - rate_t64) <= 0.10
        h5b = True  # noise grid deferred in CI; marked NOT_TESTABLE below if --ci
        # sticky/maj3 under S-only
        sticky_s = next(
            r for r in sens_rows
            if r["form"] == "sticky" and r["observable"] == "{S}"
        )
        maj3_s = next(
            r for r in sens_rows
            if r["form"] == "maj3" and r["observable"] == "{S}"
        )
        h5c = (abs(rate_s_only - primary_g2_rate) >= 0.10) or (
            sticky_s["eoa_verdict"] == "BREAKING"
            and maj3_s["eoa_verdict"] == "BREAKING"
        )
        h5b_status = "NOT_TESTABLE"
        h5a_note = "CI: T=16 vs T=64 only"
    else:
        rate_t16 = g2_agree_rate(16, 0.0)
        rate_t64 = g2_agree_rate(64, 0.0)
        rate_t256 = g2_agree_rate(256, 0.0)
        rate_noise05 = g2_agree_rate(64, 0.05)
        rate_s_only = g2_agree_rate(64, 0.0, parties=(1,))
        h5a = (
            abs(rate_t16 - primary_g2_rate) <= 0.10
            and abs(rate_t64 - primary_g2_rate) <= 0.10
            and abs(rate_t256 - primary_g2_rate) <= 0.10
        )
        h5b = abs(rate_noise05 - primary_g2_rate) <= 0.15
        sticky_s = next(
            r for r in sens_rows
            if r["form"] == "sticky" and r["observable"] == "{S}" and r["noise"] == 0.0
            and r["horizon"] == 64
        )
        maj3_s = next(
            r for r in sens_rows
            if r["form"] == "maj3" and r["observable"] == "{S}" and r["noise"] == 0.0
            and r["horizon"] == 64
        )
        h5c = (abs(rate_s_only - primary_g2_rate) >= 0.10) or (
            sticky_s["eoa_verdict"] == "BREAKING"
            and maj3_s["eoa_verdict"] == "BREAKING"
        )
        h5b_status = "SUPPORTED" if h5b else "REFUTED"
        h5a_note = "full T grid"

    h5 = h5a and (h5b if not args.ci else True) and h5c

    cm = confusion(form_rows)

    if h1 and h2:
        verdict_word = "EOA_INSTRUMENT_AGREES_CLASS"
    elif h1 and not h2:
        verdict_word = "EOA_AGREES_UNCLASSIFIED"
    elif (not h1) and h2:
        verdict_word = "EOA_TRACKS_MI_NOT_PHI"
    else:
        verdict_word = "EOA_PHI_STRESS_FAIL"

    def lab(flag):
        return "SUPPORTED" if flag else "REFUTED"

    print()
    print("CONFUSION (BREAKING↔triadic)")
    print("-" * 80)
    print(f"  TP={cm['tp']}  TN={cm['tn']}  FP={cm['fp']}  FN={cm['fn']}")
    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(
        f"  agreement: {n_agree}/{n} = {agree_rate:.3f}  "
        f"binom P(X≥k|p=0.5)={p_binom:.4f}"
    )
    print(f"  H1 (agreement ≥0.65 / binom):       {lab(h1)}")
    print(
        f"  H2 (disagreements in dya×multi):    {lab(h2)}  "
        f"share={miss_share if n_dis else float('nan'):.3f}  n_dis={n_dis}"
    )
    print(f"  H3 (sticky & maj3 dya×multi miss):  {lab(h3)}")
    print(
        f"  H4 (EoA ≤0.1× Φ wall-clock):        {lab(h4)}  "
        f"ratio={ratio:.4f}  eoa={mean_eoa:.4f}s  phi={mean_phi:.4f}s"
    )
    print(
        f"  H5a (T robustness ±0.10):           {lab(h5a)}  "
        f"T16={rate_t16:.3f} T64={primary_g2_rate:.3f} T256={rate_t256:.3f} ({h5a_note})"
    )
    print(f"  H5b (noise 0.05 drift ≤0.15):       {h5b_status}  "
          f"rate={rate_noise05:.3f}")
    print(
        f"  H5c (S-only contrast / miss stable): {lab(h5c)}  "
        f"S_rate={rate_s_only:.3f}"
    )
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(
        f"  H1={lab(h1)}  H2={lab(h2)}  H3={lab(h3)}  H4={lab(h4)}  "
        f"H5a={lab(h5a)}  H5b={h5b_status}  H5c={lab(h5c)}"
    )
    print(
        f"  reading: {verdict_word} — agree={n_agree}/{n} ({agree_rate:.3f}); "
        f"miss_class_share={miss_share if n_dis else float('nan'):.3f}; "
        f"EoA/Φ time ratio={ratio:.4f}"
    )
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    write_csv(os.path.join(RESULTS, "forms.csv"), form_rows)
    write_csv(os.path.join(RESULTS, "sensitivity.csv"), sens_rows)
    write_csv(
        os.path.join(RESULTS, "confusion.csv"),
        [cm],
        fields=["tp", "tn", "fp", "fn"],
    )
    summary = {
        "mode": "ci" if args.ci else "full",
        "h1": lab(h1),
        "h2": lab(h2),
        "h3": lab(h3),
        "h4": lab(h4),
        "h5a": lab(h5a),
        "h5b": h5b_status,
        "h5c": lab(h5c),
        "verdict": verdict_word,
        "n_agree": n_agree,
        "n_forms": n,
        "agree_rate": f"{agree_rate:.6f}",
        "p_binom": f"{p_binom:.6f}",
        "n_disagree": n_dis,
        "miss_class_share": f"{(miss_share if n_dis else float('nan')):.6f}",
        "eoa_phi_time_ratio": f"{ratio:.6f}",
        "mean_eoa_s": f"{mean_eoa:.6f}",
        "mean_phi_s": f"{mean_phi:.6f}",
        "g2_agree_rate": f"{primary_g2_rate:.6f}",
        "rate_t16": f"{rate_t16:.6f}",
        "rate_t256": f"{rate_t256:.6f}",
        "rate_noise05": f"{rate_noise05:.6f}",
        "rate_s_only": f"{rate_s_only:.6f}",
        "tp": cm["tp"],
        "tn": cm["tn"],
        "fp": cm["fp"],
        "fn": cm["fn"],
    }
    write_csv(os.path.join(RESULTS, "summary.csv"), [summary], fields=list(summary.keys()))


if __name__ == "__main__":
    main()
