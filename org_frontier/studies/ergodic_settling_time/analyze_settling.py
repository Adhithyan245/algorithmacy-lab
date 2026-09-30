"""Strand G residual — settling time vs exact Φ_MIP on the frozen 42-form panel.

Hypotheses fixed in hypotheses.md before this script produced numbers.
Instrument: org_frontier.ergodicity.settling

Run (full panel):
  python org_frontier/studies/ergodic_settling_time/analyze_settling.py

Run (CI subset — no random n=3, no n=4; H3/H5 NOT_TESTABLE):
  python org_frontier/studies/ergodic_settling_time/analyze_settling.py --ci
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
    instrument_gates,
    next_map,
    rules_ejected_latch,
    rules_ejected_latch_or,
    whole_verdict,
)
from org_frontier.ergodicity.settling import (
    DEFAULT_EPS_CONV,
    DEFAULT_EPS_FLIP,
    DEFAULT_T_MAX,
    summarize_convergence,
    summarize_mixing,
    summarize_transients,
)
from org_frontier.classifier import forms as cforms
from org_frontier.classifier.classifier import classify_rules

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
BASIN_FORMS = os.path.join(
    HERE, "..", "ergodic_eoa_basin", "results", "forms.csv"
)

# Frozen (hypotheses.md) — do not tune after the run.
EPS_CONV = DEFAULT_EPS_CONV
T_MAX = DEFAULT_T_MAX
EPS_FLIP = DEFAULT_EPS_FLIP
SEED_RANDOM = 20260930
N_RANDOM = 20
PERM_SEED = 20260930
N_PERM = 2000

GATE_PALETTE = ("AND", "OR", "XOR", "NAND", "NOR", "XNOR", "COPY0", "COPY1")
INPUT_PAIRS = ((0, 1), (0, 2), (1, 2))


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


def load_basin_gaps():
    """form → basin-mode gap_mean from the committed ergodic_eoa_basin CSV."""
    out = {}
    if not os.path.isfile(BASIN_FORMS):
        return out
    with open(BASIN_FORMS, newline="") as fh:
        for row in csv.DictReader(fh):
            if row["mode"] != "basin":
                continue
            if float(row["noise"]) != 0.0:
                continue
            out[row["form"]] = float(row["gap_mean"])
    return out


def rank_auc(scores, labels) -> float:
    pos = [s for s, lab in zip(scores, labels) if lab]
    neg = [s for s, lab in zip(scores, labels) if not lab]
    if not pos or not neg:
        return float("nan")
    wins = sum((p > n_) + 0.5 * (p == n_) for p in pos for n_ in neg)
    return wins / (len(pos) * len(neg))


def mann_whitney_onesided(scores, labels, *, higher_label=1):
    """AUC and one-sided permutation p (scores larger under higher_label)."""
    auc = rank_auc(scores, [1 if lab == higher_label else 0 for lab in labels])
    if math.isnan(auc):
        return auc, float("nan")
    rng = random.Random(PERM_SEED)
    n_pos = sum(1 for lab in labels if lab == higher_label)
    extreme = 0
    labs = list(labels)
    for _ in range(N_PERM):
        rng.shuffle(labs)
        a = rank_auc(scores, [1 if lab == higher_label else 0 for lab in labs])
        if math.isnan(a) or a >= auc - 1e-15:
            extreme += 1
    return auc, extreme / float(N_PERM)


def _ranks(vals):
    n = len(vals)
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


def _pearson(a, b):
    n = len(a)
    ma = sum(a) / n
    mb = sum(b) / n
    num = sum((a[i] - ma) * (b[i] - mb) for i in range(n))
    da = math.sqrt(sum((a[i] - ma) ** 2 for i in range(n)))
    db = math.sqrt(sum((b[i] - mb) ** 2 for i in range(n)))
    if da == 0 or db == 0:
        return float("nan")
    return num / (da * db)


def spearman_rho(xs, ys):
    n = len(xs)
    if n < 3:
        return float("nan"), float("nan")
    rx, ry = _ranks(xs), _ranks(ys)
    rho = _pearson(rx, ry)
    if math.isnan(rho):
        return rho, float("nan")
    rng = random.Random(PERM_SEED)
    extreme = 0
    for _ in range(N_PERM):
        shuffled = list(ry)
        rng.shuffle(shuffled)
        r = _pearson(rx, shuffled)
        if math.isnan(r) or abs(r) >= abs(rho) - 1e-15:
            extreme += 1
    return rho, extreme / float(N_PERM)


def partial_spearman(xs, ys, controls):
    """Spearman of residuals of rank(x), rank(y) after OLS on rank(controls)."""
    n = len(xs)
    if n < 3:
        return float("nan"), float("nan")
    rx, ry = _ranks(xs), _ranks(ys)
    # Build design matrix of ranked controls + intercept.
    R = [_ranks(c) for c in controls]
    # Residualize via normal equations on [1 | controls].
    k = 1 + len(R)

    def residualize(target):
        # Solve (A^T A) β = A^T y for A = [1, c1, ...]
        AtA = [[0.0] * k for _ in range(k)]
        Aty = [0.0] * k
        for i in range(n):
            row = [1.0] + [R[j][i] for j in range(len(R))]
            for a in range(k):
                Aty[a] += row[a] * target[i]
                for b in range(k):
                    AtA[a][b] += row[a] * row[b]
        # Gaussian elimination.
        M = [AtA[a][:] + [Aty[a]] for a in range(k)]
        for col in range(k):
            pivot = col
            for r in range(col + 1, k):
                if abs(M[r][col]) > abs(M[pivot][col]):
                    pivot = r
            M[col], M[pivot] = M[pivot], M[col]
            if abs(M[col][col]) < 1e-15:
                return [float("nan")] * n
            div = M[col][col]
            for c in range(col, k + 1):
                M[col][c] /= div
            for r in range(k):
                if r == col:
                    continue
                fac = M[r][col]
                for c in range(col, k + 1):
                    M[r][c] -= fac * M[col][c]
        beta = [M[a][k] for a in range(k)]
        out = []
        for i in range(n):
            pred = beta[0] + sum(beta[1 + j] * R[j][i] for j in range(len(R)))
            out.append(target[i] - pred)
        return out

    ex = residualize(rx)
    ey = residualize(ry)
    if any(math.isnan(v) for v in ex + ey):
        return float("nan"), float("nan")
    rho = _pearson(ex, ey)
    if math.isnan(rho):
        return rho, float("nan")
    rng = random.Random(PERM_SEED)
    extreme = 0
    for _ in range(N_PERM):
        shuffled = list(ey)
        rng.shuffle(shuffled)
        r = _pearson(ex, shuffled)
        if math.isnan(r) or abs(r) >= abs(rho) - 1e-15:
            extreme += 1
    return rho, extreme / float(N_PERM)


def residualize_linear(scores, controls):
    """OLS residual of scores on controls (+ intercept)."""
    n = len(scores)
    k = 1 + len(controls)
    AtA = [[0.0] * k for _ in range(k)]
    Aty = [0.0] * k
    for i in range(n):
        row = [1.0] + [controls[j][i] for j in range(len(controls))]
        for a in range(k):
            Aty[a] += row[a] * scores[i]
            for b in range(k):
                AtA[a][b] += row[a] * row[b]
    M = [AtA[a][:] + [Aty[a]] for a in range(k)]
    for col in range(k):
        pivot = col
        for r in range(col + 1, k):
            if abs(M[r][col]) > abs(M[pivot][col]):
                pivot = r
        M[col], M[pivot] = M[pivot], M[col]
        if abs(M[col][col]) < 1e-15:
            return list(scores)
        div = M[col][col]
        for c in range(col, k + 1):
            M[col][c] /= div
        for r in range(k):
            if r == col:
                continue
            fac = M[r][col]
            for c in range(col, k + 1):
                M[r][c] -= fac * M[col][c]
    beta = [M[a][k] for a in range(k)]
    out = []
    for i in range(n):
        pred = beta[0] + sum(
            beta[1 + j] * controls[j][i] for j in range(len(controls))
        )
        out.append(scores[i] - pred)
    return out


def logistic_fit(y, X_cols):
    """Newton–Raphson logistic regression. Returns (betas, ses, ps).

    X_cols is a list of predictor lists (no intercept); intercept is added.
    Two-sided p via normal approximation on β/se.
    """
    n = len(y)
    k = 1 + len(X_cols)
    # Design rows.
    rows = []
    for i in range(n):
        rows.append([1.0] + [X_cols[j][i] for j in range(len(X_cols))])
    beta = [0.0] * k
    for _ in range(50):
        Wz = [0.0] * k
        H = [[0.0] * k for _ in range(k)]
        for i in range(n):
            eta = sum(beta[a] * rows[i][a] for a in range(k))
            # Stable sigmoid.
            if eta >= 0:
                p = 1.0 / (1.0 + math.exp(-eta))
            else:
                e = math.exp(eta)
                p = e / (1.0 + e)
            w = p * (1.0 - p)
            if w < 1e-12:
                w = 1e-12
            resid = y[i] - p
            for a in range(k):
                Wz[a] += rows[i][a] * resid
                for b in range(k):
                    H[a][b] += w * rows[i][a] * rows[i][b]
        # Solve H δ = Wz.
        M = [H[a][:] + [Wz[a]] for a in range(k)]
        singular = False
        for col in range(k):
            pivot = col
            for r in range(col + 1, k):
                if abs(M[r][col]) > abs(M[pivot][col]):
                    pivot = r
            M[col], M[pivot] = M[pivot], M[col]
            if abs(M[col][col]) < 1e-15:
                singular = True
                break
            div = M[col][col]
            for c in range(col, k + 1):
                M[col][c] /= div
            for r in range(k):
                if r == col:
                    continue
                fac = M[r][col]
                for c in range(col, k + 1):
                    M[r][c] -= fac * M[col][c]
        if singular:
            break
        delta = [M[a][k] for a in range(k)]
        beta = [beta[a] + delta[a] for a in range(k)]
        if max(abs(d) for d in delta) < 1e-10:
            break
    # Covariance ≈ H^{-1} at final beta.
    H = [[0.0] * k for _ in range(k)]
    for i in range(n):
        eta = sum(beta[a] * rows[i][a] for a in range(k))
        if eta >= 0:
            p = 1.0 / (1.0 + math.exp(-eta))
        else:
            e = math.exp(eta)
            p = e / (1.0 + e)
        w = max(p * (1.0 - p), 1e-12)
        for a in range(k):
            for b in range(k):
                H[a][b] += w * rows[i][a] * rows[i][b]
    # Invert H.
    aug = [H[a][:] + [1.0 if a == b else 0.0 for b in range(k)] for a in range(k)]
    invertible = True
    for col in range(k):
        pivot = col
        for r in range(col + 1, k):
            if abs(aug[r][col]) > abs(aug[pivot][col]):
                pivot = r
        aug[col], aug[pivot] = aug[pivot], aug[col]
        if abs(aug[col][col]) < 1e-15:
            invertible = False
            break
        div = aug[col][col]
        for c in range(2 * k):
            aug[col][c] /= div
        for r in range(k):
            if r == col:
                continue
            fac = aug[r][col]
            for c in range(2 * k):
                aug[r][c] -= fac * aug[col][c]
    ses = []
    ps = []
    for a in range(k):
        if not invertible or aug[a][k + a] < 0:
            ses.append(float("nan"))
            ps.append(float("nan"))
            continue
        se = math.sqrt(aug[a][k + a])
        ses.append(se)
        if se <= 0 or math.isnan(se):
            ps.append(float("nan"))
        else:
            z = abs(beta[a] / se)
            # Two-sided normal p ≈ erfc(z/sqrt(2)).
            ps.append(math.erfc(z / math.sqrt(2.0)))
    return beta, ses, ps


def replace_inf(values):
    """Replace +inf with 1 + max(finite); leave finite unchanged."""
    finite = [v for v in values if not math.isinf(v) and not math.isnan(v)]
    if not finite:
        cap = 1.0
    else:
        cap = 1.0 + max(finite)
    return [cap if math.isinf(v) else v for v in values]


def median(vals):
    s = sorted(vals)
    m = len(s)
    if m == 0:
        return float("nan")
    if m % 2 == 1:
        return float(s[m // 2])
    return 0.5 * (s[m // 2 - 1] + s[m // 2])


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
                    if math.isinf(v):
                        out[k] = "inf" if v > 0 else "-inf"
                    elif math.isnan(v):
                        out[k] = "nan"
                    else:
                        out[k] = f"{v:.8f}"
                else:
                    out[k] = v
            w.writerow(out)


def evaluate_form(name, builder, labels, group, basin_gaps):
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

    t0 = time.perf_counter()
    trans = summarize_transients(nxt, n=n)
    conv = summarize_convergence(
        nxt, party_indices=parties, n=n, eps_conv=EPS_CONV, t_max=T_MAX
    )
    mix = summarize_mixing(nxt, eps_flip=EPS_FLIP, n=n)
    t_settle = time.perf_counter() - t0

    return {
        "form": name,
        "group": group,
        "n": n,
        "whole_structure": whole.structure,
        "whole_phi": float(whole.max_phi),
        "n_attractors": trans.n_attractors,
        "mean_period": trans.mean_period,
        "max_period": trans.max_period,
        "state_space_size": trans.state_space_size,
        "transient_mean": trans.mean,
        "transient_max": trans.max,
        "transient_basin_weighted": trans.basin_weighted_mean,
        "conv_mean_T": conv.mean_T,
        "conv_max_T": conv.max_T,
        "conv_median_T": conv.median_T,
        "conv_n_unresolved": conv.n_unresolved,
        "spectral_gap": mix.spectral_gap,
        "relaxation_time": mix.relaxation_time,
        "tv_mixing_bound": mix.tv_mixing_bound,
        "basin_gap_mean": basin_gaps.get(name, float("nan")),
        "t_phi_s": t_phi,
        "t_settle_s": t_settle,
        "eps_conv": EPS_CONV,
        "t_max": T_MAX,
        "eps_flip": EPS_FLIP,
        "observable": "{"
        + ",".join(labels[i] for i in parties)
        + "}",
    }


def h1_pass(auc, p):
    return ((not math.isnan(auc)) and auc >= 0.65) or (
        (not math.isnan(p)) and p < 0.05
    )


def h2_pass(rho, p):
    return (
        (not math.isnan(rho))
        and abs(rho) >= 0.30
        and (not math.isnan(p))
        and p < 0.05
    )


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ci", action="store_true", help="CI subset panel")
    args = ap.parse_args(argv)

    print("STRAND G — SETTLING TIME vs Φ_MIP")
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

    basin_gaps = load_basin_gaps()
    print(f"BASIN GAPS LOADED  n={len(basin_gaps)}")
    print("-" * 80)

    panel = build_panel(ci=args.ci)
    print(f"PANEL  n_forms={len(panel)}")
    print("-" * 80)
    print(
        f"  {'form':<22} {'grp':<12} {'whole':<8} {'Φ':>6} "
        f"{'tr_μ':>6} {'cv_μ':>6} {'rel':>8}"
    )

    form_rows = []
    for name, builder, labels, group in panel:
        row = evaluate_form(name, builder, labels, group, basin_gaps)
        form_rows.append(row)
        rel = row["relaxation_time"]
        rel_s = "inf" if math.isinf(rel) else f"{rel:8.3f}"
        print(
            f"  {name:<22} {group:<12} {row['whole_structure']:<8} "
            f"{row['whole_phi']:6.3f} {row['transient_mean']:6.3f} "
            f"{row['conv_mean_T']:6.2f} {rel_s}"
        )

    # ----- Score vectors -----
    labels_tri = [
        1 if r["whole_structure"] == "triadic" else 0 for r in form_rows
    ]
    phis = [r["whole_phi"] for r in form_rows]
    trans_means = [r["transient_mean"] for r in form_rows]
    conv_means = [r["conv_mean_T"] for r in form_rows]
    rel_raw = [r["relaxation_time"] for r in form_rows]
    rel_scores = replace_inf(rel_raw)
    gaps = [r["basin_gap_mean"] for r in form_rows]
    periods = [r["mean_period"] for r in form_rows]
    n_attrs = [float(r["n_attractors"]) for r in form_rows]
    ns = [r["n"] for r in form_rows]

    tri_trans = [t for t, lab in zip(trans_means, labels_tri) if lab]
    dya_trans = [t for t, lab in zip(trans_means, labels_tri) if not lab]

    # ----- H1 -----
    auc_t, p_t = mann_whitney_onesided(trans_means, labels_tri)
    h1 = h1_pass(auc_t, p_t)
    h1_status = "SUPPORTED" if h1 else "REFUTED"

    # ----- H2 -----
    rho_t, rho_t_p = spearman_rho(trans_means, phis)
    h2 = h2_pass(rho_t, rho_t_p)
    h2_status = "SUPPORTED" if h2 else "REFUTED"

    # ----- H3 -----
    gap_ok = [g for g in gaps if not math.isnan(g)]
    if args.ci or len(gap_ok) < len(form_rows) or len(form_rows) < 10:
        h3_status = "NOT_TESTABLE"
        h3 = False
        beta_uni = beta_part = float("nan")
        p_uni = p_part = float("nan")
        ratio = float("nan")
        rho_gap_uni = rho_gap_part = float("nan")
        rho_gap_uni_p = rho_gap_part_p = float("nan")
        h3_rule1 = h3_rule2 = h3_spearman_drop = False
    else:
        y = labels_tri
        # Standardize gap and transient for numerical stability.
        def zscore(xs):
            m = sum(xs) / len(xs)
            sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
            if sd < 1e-15:
                return [0.0] * len(xs)
            return [(x - m) / sd for x in xs]

        gap_z = zscore(gaps)
        tr_z = zscore(trans_means)
        b_uni, se_uni, p_uni_all = logistic_fit(y, [gap_z])
        b_part, se_part, p_part_all = logistic_fit(y, [gap_z, tr_z])
        beta_uni = b_uni[1]
        beta_part = b_part[1]
        p_uni = p_uni_all[1]
        p_part = p_part_all[1]
        if abs(beta_uni) < 1e-15:
            ratio = float("nan")
            h3_rule1 = False
        else:
            ratio = abs(beta_part) / abs(beta_uni)
            h3_rule1 = ratio <= 0.50
        h3_rule2 = (
            (not math.isnan(p_uni))
            and p_uni < 0.05
            and (not math.isnan(p_part))
            and p_part >= 0.05
        )
        rho_gap_uni, rho_gap_uni_p = spearman_rho(gaps, phis)
        rho_gap_part, rho_gap_part_p = partial_spearman(
            gaps, phis, [trans_means]
        )
        h3_spearman_drop = (
            (not math.isnan(rho_gap_uni))
            and (not math.isnan(rho_gap_part))
            and abs(rho_gap_part) < abs(rho_gap_uni)
        )
        h3 = (h3_rule1 or h3_rule2) and h3_spearman_drop
        h3_status = "SUPPORTED" if h3 else "REFUTED"

    # Secondary H3 report with convergence T (not a pass criterion).
    if h3_status != "NOT_TESTABLE":
        gap_z = [
            (g - sum(gaps) / len(gaps))
            / max(
                math.sqrt(
                    sum((x - sum(gaps) / len(gaps)) ** 2 for x in gaps)
                    / (len(gaps) - 1)
                ),
                1e-15,
            )
            for g in gaps
        ]
        cv_m = sum(conv_means) / len(conv_means)
        cv_sd = math.sqrt(
            sum((x - cv_m) ** 2 for x in conv_means) / (len(conv_means) - 1)
        )
        cv_z = [(x - cv_m) / cv_sd if cv_sd > 1e-15 else 0.0 for x in conv_means]
        b_uni_cv, _, p_uni_cv_all = logistic_fit(labels_tri, [gap_z])
        b_part_cv, _, p_part_cv_all = logistic_fit(labels_tri, [gap_z, cv_z])
        beta_uni_cv = b_uni_cv[1]
        beta_part_cv = b_part_cv[1]
        ratio_cv = (
            abs(beta_part_cv) / abs(beta_uni_cv)
            if abs(beta_uni_cv) > 1e-15
            else float("nan")
        )
        rho_gap_cv, _ = partial_spearman(gaps, phis, [conv_means])
    else:
        beta_uni_cv = beta_part_cv = ratio_cv = rho_gap_cv = float("nan")
        p_uni_cv_all = p_part_cv_all = [float("nan"), float("nan")]

    # ----- H4 -----
    auc_r, p_r = mann_whitney_onesided(rel_scores, labels_tri)
    h4 = h1_pass(auc_r, p_r)  # same pass rule (AUC≥0.65 or p<0.05)
    h4_status = "SUPPORTED" if h4 else "REFUTED"

    # ----- H5 -----
    if args.ci:
        h5_status = "NOT_TESTABLE"
        h5 = False
        auc_n3 = p_n3 = float("nan")
        rho_partial = rho_partial_p = float("nan")
        auc_resid = p_resid = float("nan")
        h5_n3 = h5_partial = h5_resid = False
    else:
        # (1) n=3 stratum
        idx3 = [i for i, n in enumerate(ns) if n == 3]
        scores3 = [trans_means[i] for i in idx3]
        labs3 = [labels_tri[i] for i in idx3]
        if sum(labs3) == 0 or sum(labs3) == len(labs3):
            auc_n3 = p_n3 = float("nan")
            h5_n3 = False
            n3_arm = "NOT_TESTABLE"
        else:
            auc_n3, p_n3 = mann_whitney_onesided(scores3, labs3)
            h5_n3 = h1_pass(auc_n3, p_n3)
            n3_arm = "ok"
        # (2) partial Spearman controlling period + n_attractors
        rho_partial, rho_partial_p = partial_spearman(
            trans_means, phis, [periods, n_attrs]
        )
        h5_partial = h2_pass(rho_partial, rho_partial_p)
        # residualized MW
        resid = residualize_linear(trans_means, [periods, n_attrs])
        auc_resid, p_resid = mann_whitney_onesided(resid, labels_tri)
        h5_resid = h1_pass(auc_resid, p_resid)
        # Pass if n=3 holds AND (partial OR residualized) holds.
        # If n3 arm NOT_TESTABLE, do not block on it.
        if n3_arm == "NOT_TESTABLE":
            h5 = h5_partial or h5_resid
        else:
            h5 = h5_n3 and (h5_partial or h5_resid)
        h5_status = "SUPPORTED" if h5 else "REFUTED"

    # ----- Verdict word -----
    if h1 and h3_status == "SUPPORTED":
        verdict = "SETTLING_EXPLAINS_RESIDUAL_GAP"
    elif h1 and h3_status == "REFUTED":
        verdict = "SETTLING_TRACKS_PHI_NOT_GAP"
    elif (not h1) and h4:
        verdict = "MIXING_NOT_TRANSIENT"
    elif (not h1) and (not h4):
        verdict = "SETTLING_NULL"
    else:
        # H3 NOT_TESTABLE under --ci, or mixed patterns
        verdict = "SETTLING_INCONCLUSIVE"

    # ----- Print summary -----
    print()
    print("SUMMARY")
    print("-" * 80)
    print(
        f"  triadic n={sum(labels_tri)}  dyadic n={len(labels_tri) - sum(labels_tri)}"
    )
    print(
        f"  transient mean  triadic median={median(tri_trans):.4f}  "
        f"dyadic median={median(dya_trans):.4f}"
    )
    print(
        f"  H1 transient AUC={auc_t:.3f}  p_one={p_t:.4f}  → {h1_status}"
    )
    print(
        f"  H2 transient~Φ  ρ={rho_t:.3f}  p={rho_t_p:.4f}  → {h2_status}"
    )
    if h3_status == "NOT_TESTABLE":
        print(f"  H3 gap|transient mediation:                 → {h3_status}")
    else:
        print(
            f"  H3 β_gap uni={beta_uni:.4f} (p={p_uni:.4f})  "
            f"partial={beta_part:.4f} (p={p_part:.4f})  "
            f"|βp|/|βu|={ratio:.3f}"
        )
        print(
            f"     Spearman gap~Φ uni={rho_gap_uni:.3f}  "
            f"partial={rho_gap_part:.3f}  → {h3_status}"
        )
        print(
            f"     (secondary conv-T) |βp|/|βu|={ratio_cv:.3f}  "
            f"partial ρ={rho_gap_cv:.3f}"
        )
    print(
        f"  H4 relaxation AUC={auc_r:.3f}  p_one={p_r:.4f}  → {h4_status}"
    )
    if h5_status == "NOT_TESTABLE":
        print(f"  H5 confounds:                               → {h5_status}")
    else:
        print(
            f"  H5 n=3 AUC={auc_n3:.3f} p={p_n3:.4f}  "
            f"partial ρ={rho_partial:.3f} p={rho_partial_p:.4f}  "
            f"resid AUC={auc_resid:.3f}  → {h5_status}"
        )
    print(f"  verdict: {verdict}")
    print()

    # ----- Write CSVs -----
    write_csv(os.path.join(RESULTS, "forms.csv"), form_rows)
    summary = {
        "mode_run": "ci" if args.ci else "full",
        "h1": h1_status,
        "h2": h2_status,
        "h3": h3_status,
        "h4": h4_status,
        "h5": h5_status,
        "verdict": verdict,
        "n_forms": len(form_rows),
        "n_triadic": sum(labels_tri),
        "n_dyadic": len(labels_tri) - sum(labels_tri),
        "transient_median_triadic": median(tri_trans),
        "transient_median_dyadic": median(dya_trans),
        "transient_mean_triadic": (
            sum(tri_trans) / len(tri_trans) if tri_trans else float("nan")
        ),
        "transient_mean_dyadic": (
            sum(dya_trans) / len(dya_trans) if dya_trans else float("nan")
        ),
        "h1_auc": auc_t,
        "h1_p": p_t,
        "h2_rho": rho_t,
        "h2_p": rho_t_p,
        "h3_beta_gap_uni": beta_uni if h3_status != "NOT_TESTABLE" else float("nan"),
        "h3_beta_gap_partial": (
            beta_part if h3_status != "NOT_TESTABLE" else float("nan")
        ),
        "h3_p_gap_uni": p_uni if h3_status != "NOT_TESTABLE" else float("nan"),
        "h3_p_gap_partial": (
            p_part if h3_status != "NOT_TESTABLE" else float("nan")
        ),
        "h3_beta_ratio": ratio if h3_status != "NOT_TESTABLE" else float("nan"),
        "h3_rho_gap_uni": (
            rho_gap_uni if h3_status != "NOT_TESTABLE" else float("nan")
        ),
        "h3_rho_gap_partial": (
            rho_gap_part if h3_status != "NOT_TESTABLE" else float("nan")
        ),
        "h3_secondary_beta_ratio_conv": ratio_cv,
        "h3_secondary_rho_gap_partial_conv": rho_gap_cv,
        "h4_auc": auc_r,
        "h4_p": p_r,
        "h5_auc_n3": auc_n3 if h5_status != "NOT_TESTABLE" else float("nan"),
        "h5_p_n3": p_n3 if h5_status != "NOT_TESTABLE" else float("nan"),
        "h5_rho_partial": (
            rho_partial if h5_status != "NOT_TESTABLE" else float("nan")
        ),
        "h5_rho_partial_p": (
            rho_partial_p if h5_status != "NOT_TESTABLE" else float("nan")
        ),
        "h5_auc_resid": (
            auc_resid if h5_status != "NOT_TESTABLE" else float("nan")
        ),
        "eps_conv": EPS_CONV,
        "t_max": T_MAX,
        "eps_flip": EPS_FLIP,
    }
    write_csv(os.path.join(RESULTS, "summary.csv"), [summary])

    # Group contrasts for the FINDINGS table.
    contrast = [
        {
            "measure": "transient_mean",
            "median_triadic": median(tri_trans),
            "median_dyadic": median(dya_trans),
            "auc": auc_t,
            "p_one": p_t,
            "spearman_phi": rho_t,
            "spearman_p": rho_t_p,
        },
        {
            "measure": "conv_mean_T",
            "median_triadic": median(
                [c for c, lab in zip(conv_means, labels_tri) if lab]
            ),
            "median_dyadic": median(
                [c for c, lab in zip(conv_means, labels_tri) if not lab]
            ),
            "auc": rank_auc(conv_means, labels_tri),
            "p_one": mann_whitney_onesided(conv_means, labels_tri)[1],
            "spearman_phi": spearman_rho(conv_means, phis)[0],
            "spearman_p": spearman_rho(conv_means, phis)[1],
        },
        {
            "measure": "relaxation_time",
            "median_triadic": median(
                [r for r, lab in zip(rel_scores, labels_tri) if lab]
            ),
            "median_dyadic": median(
                [r for r, lab in zip(rel_scores, labels_tri) if not lab]
            ),
            "auc": auc_r,
            "p_one": p_r,
            "spearman_phi": spearman_rho(rel_scores, phis)[0],
            "spearman_p": spearman_rho(rel_scores, phis)[1],
        },
    ]
    write_csv(os.path.join(RESULTS, "contrasts.csv"), contrast)

    print(f"wrote {RESULTS}/forms.csv  ({len(form_rows)} rows)")
    print(f"wrote {RESULTS}/summary.csv")
    print(f"wrote {RESULTS}/contrasts.csv")
    print(f"wall-clock: {time.time() - t_all:.1f}s")

    # Explicit hypothesis lines for ci/reproduce.json expect strings.
    print()
    print("HYPOTHESES")
    print("-" * 80)
    print(f"  H1 (triadic longer mean transient):              {h1_status}")
    print(f"  H2 (transient correlates with Φ):                {h2_status}")
    print(f"  H3 (basin gap explained by settling):            {h3_status}")
    print(f"  H4 (noisy relaxation separates triadic):         {h4_status}")
    print(f"  H5 (survives n / period / n_attractors):         {h5_status}")
    print(f"  verdict: {verdict}")


if __name__ == "__main__":
    main()
