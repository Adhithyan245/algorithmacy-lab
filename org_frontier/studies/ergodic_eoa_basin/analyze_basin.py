"""Strand G follow-on — EoA basin/stationary reference vs exact Φ_MIP.

Hypotheses fixed in hypotheses.md before this script existed.
Instrument: org_frontier.ergodicity.eoa (reference_mode ∈ {uniform,basin,stationary})

Run (full panel):
  python org_frontier/studies/ergodic_eoa_basin/analyze_basin.py

Run (CI subset — no random n=3, no n=4, no noise arm):
  python org_frontier/studies/ergodic_eoa_basin/analyze_basin.py --ci
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import random
import sys
import time
from typing import Callable

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.ergodicity._boolean_ergo import (
    LABELS3,
    PANEL_B1,
    find_attractors,
    instrument_gates,
    next_map,
    rules_ejected_latch,
    rules_ejected_latch_or,
    whole_verdict,
)
from org_frontier.ergodicity.eoa import (
    REFERENCE_BASIN,
    REFERENCE_STATIONARY,
    REFERENCE_UNIFORM,
    agrees_with_phi,
    run_eoa_parties,
)
from org_frontier.classifier import forms as cforms
from org_frontier.classifier.classifier import classify_rules

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PRIOR_FORMS = os.path.join(
    HERE, "..", "ergodic_eoa_instrument", "results", "forms.csv"
)

# Frozen (hypotheses.md) — do not tune after the run.
EPS_DIV = 0.1
FAIL_RATE_THRESH = 0.25
HORIZON = 64
NOISE = 0.0
NOISE_ARM = 0.05
SEED_RANDOM = 20260930
N_RANDOM = 20

GATE_PALETTE = ("AND", "OR", "XOR", "NAND", "NOR", "XNOR", "COPY0", "COPY1")
INPUT_PAIRS = ((0, 1), (0, 2), (1, 2))

MODES = (REFERENCE_UNIFORM, REFERENCE_BASIN, REFERENCE_STATIONARY)


def binomial_sf(k: int, n: int, p: float = 0.5) -> float:
    total = 0.0
    for i in range(k, n + 1):
        total += math.comb(n, i) * (p**i) * ((1 - p) ** (n - i))
    return total


def rank_auc(scores, labels) -> float:
    pos = [s for s, lab in zip(scores, labels) if lab]
    neg = [s for s, lab in zip(scores, labels) if not lab]
    if not pos or not neg:
        return float("nan")
    wins = sum((p > n_) + 0.5 * (p == n_) for p in pos for n_ in neg)
    return wins / (len(pos) * len(neg))


def spearman_rho(xs, ys):
    """Spearman rank correlation; ties get average ranks. p via permutation."""
    n = len(xs)
    if n < 3:
        return float("nan"), float("nan")

    def ranks(vals):
        order = sorted(range(n), key=lambda i: vals[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg = 0.5 * (i + j) + 1.0
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r

    rx, ry = ranks(xs), ranks(ys)

    def pearson(a, b):
        ma = sum(a) / n
        mb = sum(b) / n
        num = sum((a[i] - ma) * (b[i] - mb) for i in range(n))
        da = math.sqrt(sum((a[i] - ma) ** 2 for i in range(n)))
        db = math.sqrt(sum((b[i] - mb) ** 2 for i in range(n)))
        if da == 0 or db == 0:
            return float("nan")
        return num / (da * db)

    rho = pearson(rx, ry)
    if math.isnan(rho):
        return rho, float("nan")
    # Two-sided permutation p on y ranks (2000 shuffles, fixed seed).
    rng = random.Random(20260930)
    extreme = 0
    for _ in range(2000):
        shuffled = list(ry)
        rng.shuffle(shuffled)
        r = pearson(rx, shuffled)
        if math.isnan(r) or abs(r) >= abs(rho) - 1e-15:
            extreme += 1
    p = extreme / 2000.0
    return rho, p


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
    rows = []
    for s in range(8):
        cur = tuple((s >> i) & 1 for i in range(3))
        rows.append(tuple(int(r(cur)) for r in rules))
    return frozenset([tuple(rows)])


def _sig_of_builder(builder) -> frozenset:
    return _rules_signature(builder())


def build_random_n3(seed: int, n: int, ban: set) -> list:
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
        frozen = list(rules)
        out.append((name, (lambda frozen=frozen: list(frozen))))
    if len(out) < n:
        raise RuntimeError(f"only drew {len(out)}/{n} random forms")
    return out


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
    return [
        lambda x: x[1],
        lambda x: x[0],
        lambda x: x[1],
        lambda x: x[2],
    ]


def rules_hub_s():
    return [
        lambda x: x[1],
        lambda x: x[0] ^ x[2] ^ x[3],
        lambda x: x[1],
        lambda x: x[1],
    ]


def rules_dual_latch():
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
    panel = []
    for name, builder in PANEL_B1.items():
        panel.append((name, builder, LABELS3, "g2_core"))
    for name, builder in cforms.FORMS.items():
        panel.append((name, builder, LABELS3, "classifier"))
    panel.append(("ejected_latch", rules_ejected_latch, LABELS3, "ejection"))
    panel.append(("ejected_latch_or", rules_ejected_latch_or, LABELS3, "ejection"))
    if not ci:
        ban = {_sig_of_builder(b) for _, b, _, _ in panel if len(b()) == 3}
        for name, builder in build_random_n3(SEED_RANDOM, N_RANDOM, ban):
            panel.append((name, builder, LABELS3, "random_n3"))
        for name, builder in PANEL_N4.items():
            panel.append((name, builder, LABELS4, "n4"))
    return panel


def load_prior_miss_classes():
    """Named miss classes from the committed uniform-instrument results CSV."""
    multi = set()
    single = set()
    if not os.path.isfile(PRIOR_FORMS):
        return multi, single
    with open(PRIOR_FORMS, newline="") as fh:
        for row in csv.DictReader(fh):
            if row["agree"] != "0":
                continue
            if row["whole_structure"] != "dyadic":
                continue
            if int(row["n_attractors"]) >= 2:
                multi.add(row["form"])
            else:
                single.add(row["form"])
    return multi, single


def evaluate_form(name, builder, labels, group, *, mode, horizon=HORIZON, noise=NOISE):
    rules = builder()
    n = len(labels)
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
        reference_mode=mode,
    )
    t_eoa = time.perf_counter() - t_eoa0

    agree = agrees_with_phi(eoa.verdict, whole.structure)
    return {
        "form": name,
        "group": group,
        "mode": mode,
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
        "dyadic_multi": int(whole.structure == "dyadic" and len(attrs) >= 2),
        "dyadic_single": int(whole.structure == "dyadic" and len(attrs) == 1),
    }


def confusion(rows):
    tp = tn = fp = fn = 0
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


def summarize_mode(rows, mode_name):
    n = len(rows)
    n_agree = sum(r["agree"] for r in rows)
    agree_rate = n_agree / n if n else float("nan")
    p_binom = binomial_sf(n_agree, n, 0.5)
    cm = confusion(rows)
    scores = [r["gap_mean"] for r in rows]
    labels = [1 if r["whole_structure"] == "triadic" else 0 for r in rows]
    auc = rank_auc(scores, labels)
    phis = [r["whole_phi"] for r in rows]
    rho, rho_p = spearman_rho(scores, phis)
    n_break = sum(1 for r in rows if r["eoa_verdict"] == "BREAKING")
    n_agreeing = n - n_break
    return {
        "mode": mode_name,
        "n_forms": n,
        "n_agree": n_agree,
        "agree_rate": agree_rate,
        "p_binom": p_binom,
        "n_breaking": n_break,
        "n_agreeing_verdict": n_agreeing,
        "tp": cm["tp"],
        "tn": cm["tn"],
        "fp": cm["fp"],
        "fn": cm["fn"],
        "auc": auc,
        "spearman_rho": rho,
        "spearman_p": rho_p,
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ci", action="store_true", help="CI subset panel")
    args = ap.parse_args(argv)

    print("STRAND G — EoA BASIN / STATIONARY vs Φ_MIP")
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

    prior_multi, prior_single = load_prior_miss_classes()
    print(
        f"PRIOR MISS CLASSES  multi={len(prior_multi)}  single={len(prior_single)}"
    )
    print("-" * 80)

    panel = build_panel(ci=args.ci)
    print(f"PANEL  n_forms={len(panel)}")
    print("-" * 80)

    form_rows = []
    mode_summaries = {}
    for mode in MODES:
        print()
        print(f"REFERENCE MODE: {mode}")
        print("-" * 80)
        print(
            f"  {'form':<22} {'grp':<12} {'whole':<8} {'n_a':>3} "
            f"{'eoa':<9} {'fail':>6} {'gap':>7} agree"
        )
        mode_rows = []
        for name, builder, labels, group in panel:
            row = evaluate_form(name, builder, labels, group, mode=mode)
            form_rows.append(row)
            mode_rows.append(row)
            print(
                f"  {name:<22} {group:<12} {row['whole_structure']:<8} "
                f"{row['n_attractors']:>3} {row['eoa_verdict']:<9} "
                f"{row['fail_rate']:>6.3f} {row['gap_mean']:>7.3f} "
                f"{bool(row['agree'])}"
            )
        mode_summaries[mode] = summarize_mode(mode_rows, mode)

    # ----- H1: basin rescues prior dyadic×multi misses -----
    basin_by_form = {
        r["form"]: r for r in form_rows if r["mode"] == REFERENCE_BASIN
    }
    multi_present = [f for f in prior_multi if f in basin_by_form]
    n_multi = len(multi_present)
    n_multi_rescued = sum(
        1 for f in multi_present if basin_by_form[f]["eoa_verdict"] == "AGREEING"
    )
    multi_rescue = n_multi_rescued / n_multi if n_multi else float("nan")
    h1 = (n_multi > 0) and (multi_rescue >= 0.75)

    # ----- H2: stationary rescues prior dyadic×single misses -----
    stat_by_form = {
        r["form"]: r for r in form_rows if r["mode"] == REFERENCE_STATIONARY
    }
    single_present = [f for f in prior_single if f in stat_by_form]
    n_single = len(single_present)
    n_single_rescued = sum(
        1 for f in single_present if stat_by_form[f]["eoa_verdict"] == "AGREEING"
    )
    single_rescue = n_single_rescued / n_single if n_single else float("nan")
    h2 = (n_single > 0) and (single_rescue >= 0.80)
    if args.ci and n_single == 0:
        h2_status = "NOT_TESTABLE"
        h2 = False
    else:
        h2_status = "SUPPORTED" if h2 else "REFUTED"

    # ----- H3 / H4 per mode -----
    def h3_pass(s):
        return (s["agree_rate"] >= 0.65) or (
            s["agree_rate"] > 0.5 and s["p_binom"] < 0.05
        )

    def h4_pass(s):
        auc_ok = (not math.isnan(s["auc"])) and s["auc"] >= 0.65
        rho = s["spearman_rho"]
        rho_p = s["spearman_p"]
        rho_ok = (
            (not math.isnan(rho))
            and abs(rho) >= 0.30
            and (not math.isnan(rho_p))
            and rho_p < 0.05
        )
        return auc_ok or rho_ok

    h3_basin = h3_pass(mode_summaries[REFERENCE_BASIN])
    h3_stat = h3_pass(mode_summaries[REFERENCE_STATIONARY])
    h3 = h3_basin or h3_stat
    h4_basin = h4_pass(mode_summaries[REFERENCE_BASIN])
    h4_stat = h4_pass(mode_summaries[REFERENCE_STATIONARY])
    h4 = h4_basin or h4_stat

    # ----- H5: noise arm on G2 core under basin -----
    noise_rows = []
    if args.ci:
        h5_status = "NOT_TESTABLE"
        h5 = False
        basin_g2_rate = float("nan")
        noise_g2_rate = float("nan")
        n_flip_ab = 0
    else:
        g2 = [(n, b, lab) for n, b, lab, g in panel if g == "g2_core"]
        basin_g2 = [
            r
            for r in form_rows
            if r["mode"] == REFERENCE_BASIN and r["group"] == "g2_core"
        ]
        basin_g2_rate = sum(r["agree"] for r in basin_g2) / len(basin_g2)
        basin_g2_verdict = {r["form"]: r["eoa_verdict"] for r in basin_g2}
        noise_agree = 0
        n_flip_ab = 0
        for name, builder, labels in g2:
            row = evaluate_form(
                name,
                builder,
                labels,
                "g2_core",
                mode=REFERENCE_BASIN,
                horizon=HORIZON,
                noise=NOISE_ARM,
            )
            noise_rows.append(row)
            noise_agree += row["agree"]
            if (
                basin_g2_verdict[name] == "AGREEING"
                and row["eoa_verdict"] == "BREAKING"
            ):
                n_flip_ab += 1
        noise_g2_rate = noise_agree / len(g2)
        h5 = (n_flip_ab >= 1) or (abs(noise_g2_rate - basin_g2_rate) >= 0.10)
        h5_status = "SUPPORTED" if h5 else "REFUTED"

    # ----- Verdict word -----
    if h3 and h4:
        verdict_word = "EOA_BASIN_TRACKS_PHI"
    elif h1 and (h2_status == "SUPPORTED") and (not h3) and (not h4):
        verdict_word = "EOA_FIX_NO_PHI_SIGNAL"
    elif (not h1) or (h2_status == "REFUTED"):
        verdict_word = "EOA_FIX_INCOMPLETE"
    else:
        verdict_word = "EOA_BASIN_INCONCLUSIVE"

    def lab(flag):
        return "SUPPORTED" if flag else "REFUTED"

    print()
    print("MODE SUMMARIES (noise=0)")
    print("-" * 80)
    for mode in MODES:
        s = mode_summaries[mode]
        print(
            f"  {mode:<12} agree={s['n_agree']}/{s['n_forms']} "
            f"({s['agree_rate']:.3f})  "
            f"TP={s['tp']} TN={s['tn']} FP={s['fp']} FN={s['fn']}  "
            f"AUC={s['auc']:.3f}  ρ={s['spearman_rho']:.3f} "
            f"(p={s['spearman_p']:.3f})  "
            f"BREAKING={s['n_breaking']} AGREEING={s['n_agreeing_verdict']}"
        )

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(
        f"  H1 (basin rescues ≥0.75 of prior dya×multi):  {lab(h1)}  "
        f"rescued={n_multi_rescued}/{n_multi} share={multi_rescue if n_multi else float('nan'):.3f}"
    )
    print(
        f"  H2 (stationary rescues ≥0.80 of prior dya×1): {h2_status}  "
        f"rescued={n_single_rescued}/{n_single} "
        f"share={single_rescue if n_single else float('nan'):.3f}"
    )
    print(
        f"  H3 (agreement ≥0.65 basin|stationary):        {lab(h3)}  "
        f"basin={lab(h3_basin)} ({mode_summaries[REFERENCE_BASIN]['agree_rate']:.3f})  "
        f"stat={lab(h3_stat)} ({mode_summaries[REFERENCE_STATIONARY]['agree_rate']:.3f})"
    )
    print(
        f"  H4 (AUC≥0.65 or |ρ|≥0.30):                    {lab(h4)}  "
        f"basin={lab(h4_basin)}  stat={lab(h4_stat)}"
    )
    print(
        f"  H5 (basin noise arm restores signal):         {h5_status}  "
        f"flips_A→B={n_flip_ab}  "
        f"basin0={basin_g2_rate if not math.isnan(basin_g2_rate) else float('nan'):.3f}  "
        f"noise={noise_g2_rate if not math.isnan(noise_g2_rate) else float('nan'):.3f}"
    )
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(
        f"  H1={lab(h1)}  H2={h2_status}  H3={lab(h3)}  H4={lab(h4)}  H5={h5_status}"
    )
    print(
        f"  reading: {verdict_word} — after the per-outcome fix, "
        f"basin agree={mode_summaries[REFERENCE_BASIN]['agree_rate']:.3f}, "
        f"stationary agree={mode_summaries[REFERENCE_STATIONARY]['agree_rate']:.3f}; "
        f"prior multi rescued={n_multi_rescued}/{n_multi}, "
        f"prior single rescued={n_single_rescued}/{n_single}"
    )
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    write_csv(os.path.join(RESULTS, "forms.csv"), form_rows)
    if noise_rows:
        write_csv(os.path.join(RESULTS, "noise_arm.csv"), noise_rows)
    cm_rows = []
    for mode in MODES:
        s = mode_summaries[mode]
        cm_rows.append(
            {
                "mode": mode,
                "tp": s["tp"],
                "tn": s["tn"],
                "fp": s["fp"],
                "fn": s["fn"],
                "n_agree": s["n_agree"],
                "n_forms": s["n_forms"],
                "agree_rate": s["agree_rate"],
                "auc": s["auc"],
                "spearman_rho": s["spearman_rho"],
                "spearman_p": s["spearman_p"],
                "n_breaking": s["n_breaking"],
                "n_agreeing_verdict": s["n_agreeing_verdict"],
            }
        )
    write_csv(os.path.join(RESULTS, "confusion.csv"), cm_rows)

    summary = {
        "mode_run": "ci" if args.ci else "full",
        "h1": lab(h1),
        "h2": h2_status,
        "h3": lab(h3),
        "h4": lab(h4),
        "h5": h5_status,
        "verdict": verdict_word,
        "n_multi_prior": n_multi,
        "n_multi_rescued": n_multi_rescued,
        "multi_rescue_share": f"{(multi_rescue if n_multi else float('nan')):.6f}",
        "n_single_prior": n_single,
        "n_single_rescued": n_single_rescued,
        "single_rescue_share": f"{(single_rescue if n_single else float('nan')):.6f}",
        "basin_agree_rate": f"{mode_summaries[REFERENCE_BASIN]['agree_rate']:.6f}",
        "basin_tp": mode_summaries[REFERENCE_BASIN]["tp"],
        "basin_tn": mode_summaries[REFERENCE_BASIN]["tn"],
        "basin_fp": mode_summaries[REFERENCE_BASIN]["fp"],
        "basin_fn": mode_summaries[REFERENCE_BASIN]["fn"],
        "basin_auc": f"{mode_summaries[REFERENCE_BASIN]['auc']:.6f}",
        "basin_rho": f"{mode_summaries[REFERENCE_BASIN]['spearman_rho']:.6f}",
        "stat_agree_rate": f"{mode_summaries[REFERENCE_STATIONARY]['agree_rate']:.6f}",
        "stat_tp": mode_summaries[REFERENCE_STATIONARY]["tp"],
        "stat_tn": mode_summaries[REFERENCE_STATIONARY]["tn"],
        "stat_fp": mode_summaries[REFERENCE_STATIONARY]["fp"],
        "stat_fn": mode_summaries[REFERENCE_STATIONARY]["fn"],
        "stat_auc": f"{mode_summaries[REFERENCE_STATIONARY]['auc']:.6f}",
        "stat_rho": f"{mode_summaries[REFERENCE_STATIONARY]['spearman_rho']:.6f}",
        "uniform_agree_rate": f"{mode_summaries[REFERENCE_UNIFORM]['agree_rate']:.6f}",
        "basin_g2_agree_noise0": (
            f"{basin_g2_rate:.6f}" if not math.isnan(basin_g2_rate) else "nan"
        ),
        "basin_g2_agree_noise05": (
            f"{noise_g2_rate:.6f}" if not math.isnan(noise_g2_rate) else "nan"
        ),
        "n_flip_agreeing_to_breaking": n_flip_ab,
    }
    write_csv(
        os.path.join(RESULTS, "summary.csv"),
        [summary],
        fields=list(summary.keys()),
    )


if __name__ == "__main__":
    main()
