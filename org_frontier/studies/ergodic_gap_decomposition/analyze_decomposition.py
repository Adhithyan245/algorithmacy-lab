"""Strand G residual — decompose the basin-mode EoA gap vs Φ_MIP.

Hypotheses fixed in hypotheses.md before this script produced numbers.
Instruments: org_frontier.ergodicity.eoa (basin) and
org_frontier.ergodicity.settling (oscillation / pre-cycle diversity).

Run (full panel):
  python org_frontier/studies/ergodic_gap_decomposition/analyze_decomposition.py

Run (CI subset — no random n=3, no n=4; H0–H4 NOT_TESTABLE):
  python org_frontier/studies/ergodic_gap_decomposition/analyze_decomposition.py --ci
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
    rules_ejected_latch,
    rules_ejected_latch_or,
)
from org_frontier.ergodicity.eoa import (
    REFERENCE_BASIN,
    bit_observable,
    parity_observable,
    rules_to_next_map,
    run_eoa,
    run_eoa_parties,
)
from org_frontier.ergodicity.settling import (
    summarize_oscillation,
    summarize_pre_cycle_diversity,
)
from org_frontier.classifier import forms as cforms

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
BASIN_FORMS = os.path.join(
    HERE, "..", "ergodic_eoa_basin", "results", "forms.csv"
)

# Frozen (hypotheses.md).
HORIZON_PRIMARY = 64
T_GRID = (16, 32, 64, 128, 256, 512)
SEED_RANDOM = 20260930
N_RANDOM = 20
PERM_SEED = 20260930
N_PERM = 2000
N_BOOT = 2000
GAP_MATCH_TOL = 1e-6
SHRINK_PASS = 0.50
SHRINK_SOFT = 0.75
SLOPE_LO = -1.25
SLOPE_HI = -0.75

GATE_PALETTE = ("AND", "OR", "XOR", "NAND", "NOR", "XNOR", "COPY0", "COPY1")
INPUT_PAIRS = ((0, 1), (0, 2), (1, 2))
GROUPS = ("g2_core", "classifier", "ejection", "random_n3", "n4")


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


def load_basin_committed():
    """Map form → committed basin-mode row (noise=0)."""
    out = {}
    with open(BASIN_FORMS, newline="") as fh:
        for row in csv.DictReader(fh):
            if row["mode"] != "basin":
                continue
            if abs(float(row["noise"]) - 0.0) > 1e-12:
                continue
            out[row["form"]] = row
    return out


def standardize(xs):
    m = sum(xs) / float(len(xs))
    var = sum((x - m) ** 2 for x in xs) / float(len(xs))
    sd = math.sqrt(var) if var > 0 else 1.0
    if sd < 1e-15:
        sd = 1.0
    return [(x - m) / sd for x in xs], m, sd


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
    n = len(xs)
    if n < 3:
        return float("nan"), float("nan")
    rx, ry = _ranks(xs), _ranks(ys)
    R = [_ranks(c) for c in controls]
    k = 1 + len(R)

    def residualize(target):
        AtA = [[0.0] * k for _ in range(k)]
        Aty = [0.0] * k
        for i in range(n):
            row = [1.0] + [R[j][i] for j in range(len(R))]
            for a in range(k):
                Aty[a] += row[a] * target[i]
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


def logistic_fit(y, X_cols):
    n = len(y)
    k = 1 + len(X_cols)
    rows = []
    for i in range(n):
        rows.append([1.0] + [X_cols[j][i] for j in range(len(X_cols))])
    beta = [0.0] * k
    for _ in range(50):
        Wz = [0.0] * k
        H = [[0.0] * k for _ in range(k)]
        for i in range(n):
            eta = sum(beta[a] * rows[i][a] for a in range(k))
            if eta >= 0:
                p = 1.0 / (1.0 + math.exp(-eta))
            else:
                e = math.exp(eta)
                p = e / (1.0 + e)
            w = max(p * (1.0 - p), 1e-12)
            resid = y[i] - p
            for a in range(k):
                Wz[a] += rows[i][a] * resid
                for b in range(k):
                    H[a][b] += w * rows[i][a] * rows[i][b]
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
    ses, ps = [], []
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
            ps.append(math.erfc(z / math.sqrt(2.0)))
    return beta, ses, ps


def rank_auc(scores, labels) -> float:
    pos = [s for s, lab in zip(scores, labels) if lab]
    neg = [s for s, lab in zip(scores, labels) if not lab]
    if not pos or not neg:
        return float("nan")
    wins = sum((p > n_) + 0.5 * (p == n_) for p in pos for n_ in neg)
    return wins / (len(pos) * len(neg))


def auc_permutation_p(scores, labels, alternative="two-sided"):
    """Permutation p for AUC vs chance (labels shuffled)."""
    obs = rank_auc(scores, labels)
    if math.isnan(obs):
        return obs, float("nan")
    rng = random.Random(PERM_SEED)
    labs = list(labels)
    extreme = 0
    for _ in range(N_PERM):
        shuffled = list(labs)
        rng.shuffle(shuffled)
        a = rank_auc(scores, shuffled)
        if math.isnan(a):
            extreme += 1
            continue
        if alternative == "greater":
            if a >= obs - 1e-15:
                extreme += 1
        else:
            # two-sided vs 0.5: compare |auc-0.5|
            if abs(a - 0.5) >= abs(obs - 0.5) - 1e-15:
                extreme += 1
    return obs, extreme / float(N_PERM)


def bootstrap_auc_ci(scores, labels):
    """Stratified bootstrap 95% CI for AUC (seed PERM_SEED)."""
    pos_idx = [i for i, lab in enumerate(labels) if lab]
    neg_idx = [i for i, lab in enumerate(labels) if not lab]
    if not pos_idx or not neg_idx:
        return float("nan"), float("nan"), float("nan")
    rng = random.Random(PERM_SEED)
    aucs = []
    for _ in range(N_BOOT):
        pi = [pos_idx[rng.randrange(len(pos_idx))] for _ in range(len(pos_idx))]
        ni = [neg_idx[rng.randrange(len(neg_idx))] for _ in range(len(neg_idx))]
        sc = [scores[i] for i in pi + ni]
        lb = [True] * len(pi) + [False] * len(ni)
        aucs.append(rank_auc(sc, lb))
    aucs.sort()
    lo = aucs[int(0.025 * (N_BOOT - 1))]
    hi = aucs[int(0.975 * (N_BOOT - 1))]
    return rank_auc(scores, labels), lo, hi


def ols_slope(xs, ys):
    """OLS slope of y on x (no intercept needed for log-log if centered, but use intercept)."""
    n = len(xs)
    if n < 2:
        return float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    if den <= 0:
        return float("nan")
    return num / den


def mediation_battery(gaps, triadic, phis, covariate):
    """Return dict with uni/partial logistic β for gap and partial Spearman."""
    y = [1.0 if t else 0.0 for t in triadic]
    g_std, _, _ = standardize(gaps)
    c_std, _, _ = standardize(covariate)
    b_uni, _, p_uni = logistic_fit(y, [g_std])
    b_part, _, p_part = logistic_fit(y, [g_std, c_std])
    beta_uni = b_uni[1]
    beta_partial = b_part[1]
    if abs(beta_uni) < 1e-15:
        ratio = float("nan")
    else:
        ratio = abs(beta_partial) / abs(beta_uni)
    rho_uni, rho_uni_p = spearman_rho(gaps, phis)
    rho_part, rho_part_p = partial_spearman(gaps, phis, [covariate])
    shrink_pass = (not math.isnan(ratio)) and ratio <= SHRINK_PASS
    lose_sig = (p_uni[1] < 0.05) and (p_part[1] >= 0.05)
    spearman_drop = (not math.isnan(rho_uni)) and (not math.isnan(rho_part)) and (
        abs(rho_part) < abs(rho_uni)
    )
    soft_ok = (
        (not math.isnan(ratio))
        and ratio <= SHRINK_SOFT
        and spearman_drop
    )
    # H1/H2/H3 mediation: shrink_pass OR lose_sig, AND spearman_drop
    # (H1 also allows soft_ok as alternative to shrink_pass)
    mediates_strict = (shrink_pass or lose_sig) and spearman_drop
    return {
        "beta_uni": beta_uni,
        "p_uni": p_uni[1],
        "beta_partial": beta_partial,
        "p_partial": p_part[1],
        "beta_ratio": ratio,
        "rho_uni": rho_uni,
        "rho_uni_p": rho_uni_p,
        "rho_partial": rho_part,
        "rho_partial_p": rho_part_p,
        "shrink_pass": shrink_pass,
        "lose_sig": lose_sig,
        "spearman_drop": spearman_drop,
        "soft_ok": soft_ok,
        "mediates_strict": mediates_strict,
    }


def write_csv(path, rows, fields=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not rows:
        # Touch an empty file with header only when fields given.
        if fields:
            with open(path, "w", newline="") as fh:
                csv.DictWriter(fh, fieldnames=fields).writeheader()
        return
    if fields is None:
        # Union keys across rows (n=3 vs n=4 bit columns differ).
        fields = []
        seen = set()
        for r in rows:
            for k in r.keys():
                if k not in seen:
                    seen.add(k)
                    fields.append(k)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            out = {}
            for k in fields:
                v = r.get(k, "")
                if isinstance(v, float):
                    if math.isinf(v):
                        out[k] = "inf" if v > 0 else "-inf"
                    elif math.isnan(v):
                        out[k] = "nan"
                    else:
                        out[k] = f"{v:.8f}"
                elif isinstance(v, bool):
                    out[k] = int(v)
                else:
                    out[k] = v
            w.writerow(out)


def evaluate_form(name, builder, labels, group, committed):
    rules = builder()
    n = len(labels)
    parties = tuple(i for i, lab in enumerate(labels) if lab != "S")
    s_idx = labels.index("S") if "S" in labels else None
    nxt = rules_to_next_map(rules, n=n)

    # Φ / structure from committed basin CSV (not recomputed).
    crow = committed[name]
    whole_structure = crow["whole_structure"]
    whole_phi = float(crow["whole_phi"])
    committed_gap = float(crow["gap_mean"])

    t0 = time.perf_counter()
    party_res = run_eoa_parties(
        nxt,
        parties,
        labels=labels,
        horizon=HORIZON_PRIMARY,
        noise=0.0,
        reference_mode=REFERENCE_BASIN,
        n=n,
    )
    gap_party = party_res.gap_mean
    gap_match = abs(gap_party - committed_gap) <= GAP_MATCH_TOL

    # Per-bit / mediator / parity gaps.
    per_bit = {}
    for i, lab in enumerate(labels):
        res = run_eoa(
            nxt,
            bit_observable(i),
            horizon=HORIZON_PRIMARY,
            noise=0.0,
            reference_mode=REFERENCE_BASIN,
            n=n,
            observable_name=lab,
        )
        per_bit[lab] = res.gap_mean
    gap_mediator = per_bit["S"] if s_idx is not None else float("nan")
    # Parity of first two party bits (W⊕C on n=3; W⊕C1 on n=4).
    if len(parties) >= 2:
        par = run_eoa(
            nxt,
            parity_observable(parties[:2]),
            horizon=HORIZON_PRIMARY,
            noise=0.0,
            reference_mode=REFERENCE_BASIN,
            n=n,
            observable_name="parity",
        )
        gap_parity = par.gap_mean
    else:
        gap_parity = float("nan")

    osc = summarize_oscillation(nxt, parties, n=n)
    div = summarize_pre_cycle_diversity(nxt, parties, n=n)

    # T-scaling: gap at each T.
    gaps_T = {}
    for T in T_GRID:
        res_T = run_eoa_parties(
            nxt,
            parties,
            labels=labels,
            horizon=T,
            noise=0.0,
            reference_mode=REFERENCE_BASIN,
            n=n,
        )
        gaps_T[T] = res_T.gap_mean
    logT = [math.log(T) for T in T_GRID]
    logG = [math.log(gaps_T[T] + 1e-12) for T in T_GRID]
    slope = ols_slope(logT, logG)
    gapT_vals = [gaps_T[T] * T for T in T_GRID]
    mean_gapT = sum(gapT_vals) / len(gapT_vals)
    if mean_gapT > 0:
        var_gapT = sum((v - mean_gapT) ** 2 for v in gapT_vals) / len(gapT_vals)
        cv_gapT = math.sqrt(var_gapT) / mean_gapT
    else:
        cv_gapT = float("nan")

    t_eoa = time.perf_counter() - t0
    row = {
        "form": name,
        "group": group,
        "n": n,
        "whole_structure": whole_structure,
        "whole_phi": whole_phi,
        "triadic": whole_structure == "triadic",
        "committed_gap": committed_gap,
        "gap_party": gap_party,
        "gap_match": gap_match,
        "gap_mediator": gap_mediator,
        "gap_parity": gap_parity,
        "party_osc_frac": osc.party_osc_frac,
        "mean_cycle_var": osc.mean_cycle_var,
        "mean_period": osc.mean_period,
        "max_period": osc.max_period,
        "n_attractors": osc.n_attractors,
        "pre_cycle_div": div.pre_cycle_div,
        "mean_transient": div.mean_transient,
        "t_scale_slope": slope,
        "gapT_cv": cv_gapT,
        "t_eoa_s": t_eoa,
    }
    for lab, g in per_bit.items():
        row[f"gap_bit_{lab}"] = g
    for T in T_GRID:
        row[f"gap_T{T}"] = gaps_T[T]
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ci", action="store_true", help="CI subset (no random n=3, no n=4)")
    args = ap.parse_args()
    ci = args.ci

    gates = instrument_gates()
    print(
        f"memoryless whole: {gates['memoryless'].structure} "
        f"Φ={gates['memoryless'].max_phi:.6f}  "
        f"{'PASS' if gates['ctrl_memoryless'] else 'FAIL'}"
    )
    print(
        f"sticky whole:     {gates['sticky'].structure} "
        f"Φ={gates['sticky'].max_phi:.6f}  "
        f"{'PASS' if gates['ctrl_sticky'] else 'FAIL'}"
    )
    if not gates["ok"]:
        raise SystemExit("instrument gates failed")

    committed = load_basin_committed()
    panel = build_panel(ci)
    missing = [name for name, _, _, _ in panel if name not in committed]
    if missing:
        raise SystemExit(f"committed basin CSV missing forms: {missing}")

    form_rows = []
    for name, builder, labels, group in panel:
        form_rows.append(evaluate_form(name, builder, labels, group, committed))

    n_mismatch = sum(1 for r in form_rows if not r["gap_match"])
    h5_status = "SUPPORTED" if n_mismatch == 0 else "REFUTED"
    print(f"H5 (recomputed gaps match committed):             {h5_status}")
    print(f"  mismatches={n_mismatch}/{len(form_rows)}")
    if n_mismatch > 0:
        for r in form_rows:
            if not r["gap_match"]:
                print(
                    f"  MISMATCH {r['form']}: recomputed={r['gap_party']:.8f} "
                    f"committed={r['committed_gap']:.8f}"
                )
        # Abort scoring H0–H4 per hypotheses.
        summary = {
            "ci": int(ci),
            "n_forms": len(form_rows),
            "h0": "NOT_TESTABLE",
            "h1": "NOT_TESTABLE",
            "h2": "NOT_TESTABLE",
            "h3": "NOT_TESTABLE",
            "h4": "NOT_TESTABLE",
            "h5": h5_status,
            "verdict": "GAP_DECOMPOSITION_INCONCLUSIVE",
            "winner": "",
        }
        write_csv(os.path.join(RESULTS, "forms.csv"), form_rows)
        write_csv(os.path.join(RESULTS, "summary.csv"), [summary])
        print("verdict: GAP_DECOMPOSITION_INCONCLUSIVE")
        raise SystemExit("H5 gate failed — aborting H0–H4")

    if ci:
        # Full-panel hypotheses not scored on the CI subset.
        for key in ("h0", "h1", "h2", "h3", "h4"):
            pass
        summary = {
            "ci": 1,
            "n_forms": len(form_rows),
            "h0": "NOT_TESTABLE",
            "h1": "NOT_TESTABLE",
            "h2": "NOT_TESTABLE",
            "h3": "NOT_TESTABLE",
            "h4": "NOT_TESTABLE",
            "h5": h5_status,
            "verdict": "GAP_DECOMPOSITION_INCONCLUSIVE",
            "winner": "",
            "auc": float("nan"),
            "auc_ci_lo": float("nan"),
            "auc_ci_hi": float("nan"),
            "auc_perm_p": float("nan"),
            "mean_t_slope": float("nan"),
            "beta_ratio_osc": float("nan"),
            "beta_ratio_div": float("nan"),
            "auc_party": float("nan"),
            "auc_mediator": float("nan"),
        }
        write_csv(os.path.join(RESULTS, "forms.csv"), form_rows)
        write_csv(os.path.join(RESULTS, "summary.csv"), [summary])
        write_csv(
            os.path.join(RESULTS, "mechanisms.csv"),
            [],
            fields=[
                "mechanism",
                "covariate",
                "hypothesis",
                "passes",
                "beta_ratio",
                "partial_rho",
                "rho_uni",
                "t_scaling_slope",
                "extra",
            ],
        )
        write_csv(
            os.path.join(RESULTS, "leave_one_group.csv"),
            [],
            fields=[
                "left_out",
                "n_remaining",
                "auc",
                "spearman_rho",
                "kills_band",
            ],
        )
        print("H0 (AUC not a fluke):                              NOT_TESTABLE")
        print("H1 (finite-T phase artifact):                      NOT_TESTABLE")
        print("H2 (within-basin heterogeneity):                   NOT_TESTABLE")
        print("H3 (observable choice / party oscillation):        NOT_TESTABLE")
        print("H4 (one panel group carries association):          NOT_TESTABLE")
        print("verdict: GAP_DECOMPOSITION_INCONCLUSIVE")
        return

    # ----- Full panel scoring -----
    gaps = [r["gap_party"] for r in form_rows]
    phis = [r["whole_phi"] for r in form_rows]
    triadic = [r["triadic"] for r in form_rows]
    osc = [r["party_osc_frac"] for r in form_rows]
    div = [r["pre_cycle_div"] for r in form_rows]
    gap_med = [r["gap_mediator"] for r in form_rows]
    slopes = [r["t_scale_slope"] for r in form_rows]
    cvs = [r["gapT_cv"] for r in form_rows]

    auc, auc_lo, auc_hi = bootstrap_auc_ci(gaps, triadic)
    _, auc_p = auc_permutation_p(gaps, triadic, alternative="two-sided")
    h0 = (auc_lo > 0.5) and (auc_p < 0.05)
    h0_status = "SUPPORTED" if h0 else "REFUTED"
    print(f"H0 (AUC not a fluke):                              {h0_status}")
    print(
        f"  AUC={auc:.4f}  bootstrap95=[{auc_lo:.4f}, {auc_hi:.4f}]  "
        f"perm_p={auc_p:.4f}"
    )

    mean_slope = sum(slopes) / float(len(slopes))
    cvs_finite = [c for c in cvs if not math.isnan(c)]
    mean_cv = (
        sum(cvs_finite) / float(len(cvs_finite)) if cvs_finite else float("nan")
    )
    med_a = mediation_battery(gaps, triadic, phis, osc)
    slope_ok = SLOPE_LO <= mean_slope <= SLOPE_HI
    h1_med = med_a["mediates_strict"] or med_a["soft_ok"]
    h1 = slope_ok and h1_med
    h1_status = "SUPPORTED" if h1 else "REFUTED"
    print(f"H1 (finite-T phase artifact):                      {h1_status}")
    print(
        f"  mean log-log slope={mean_slope:.4f}  "
        f"(band [{SLOPE_LO}, {SLOPE_HI}])  "
        f"β_ratio_osc={med_a['beta_ratio']:.4f}  "
        f"partial_ρ={med_a['rho_partial']:.4f}  "
        f"mean gap·T CV={mean_cv:.4f}"
    )

    med_b = mediation_battery(gaps, triadic, phis, div)
    h2 = med_b["mediates_strict"]
    h2_status = "SUPPORTED" if h2 else "REFUTED"
    print(f"H2 (within-basin heterogeneity):                   {h2_status}")
    print(
        f"  β_ratio_div={med_b['beta_ratio']:.4f}  "
        f"partial_ρ={med_b['rho_partial']:.4f}"
    )

    auc_party = rank_auc(gaps, triadic)
    auc_med = rank_auc(gap_med, triadic)
    rho_party, _ = spearman_rho(gaps, phis)
    rho_med, _ = spearman_rho(gap_med, phis)
    obs_sep = (auc_party - auc_med >= 0.10) or (
        abs(rho_party) - abs(rho_med) >= 0.10
    )
    # H3 mediation uses party_osc_frac (same as H1 covariate by design).
    h3 = obs_sep and h1_med
    h3_status = "SUPPORTED" if h3 else "REFUTED"
    print(f"H3 (observable choice / party oscillation):        {h3_status}")
    print(
        f"  AUC party={auc_party:.4f}  AUC mediator={auc_med:.4f}  "
        f"Δ={auc_party - auc_med:.4f}  "
        f"ρ_party={rho_party:.4f}  ρ_med={rho_med:.4f}"
    )

    # Leave-one-group-out.
    logo_rows = []
    h4 = False
    for g in GROUPS:
        keep_gaps = [r["gap_party"] for r in form_rows if r["group"] != g]
        keep_tri = [r["triadic"] for r in form_rows if r["group"] != g]
        keep_phi = [r["whole_phi"] for r in form_rows if r["group"] != g]
        if sum(1 for t in keep_tri if t) == 0 or sum(1 for t in keep_tri if not t) == 0:
            a = float("nan")
            rho = float("nan")
            kills = False
        else:
            a = rank_auc(keep_gaps, keep_tri)
            rho, _ = spearman_rho(keep_gaps, keep_phi)
            kills = (a < 0.65) and (abs(rho) < 0.30)
            if kills:
                h4 = True
        logo_rows.append(
            {
                "left_out": g,
                "n_remaining": len(keep_gaps),
                "auc": a,
                "spearman_rho": rho,
                "kills_band": kills,
            }
        )
    h4_status = "SUPPORTED" if h4 else "REFUTED"
    print(f"H4 (one panel group carries association):          {h4_status}")
    for lr in logo_rows:
        print(
            f"  leave-out {lr['left_out']}: AUC={lr['auc']:.4f}  "
            f"ρ={lr['spearman_rho']:.4f}  kills={lr['kills_band']}"
        )

    # Ranking among mechanisms that pass.
    mech_rows = [
        {
            "mechanism": "a_phase_artifact",
            "covariate": "party_osc_frac",
            "hypothesis": "H1",
            "passes": h1,
            "beta_ratio": med_a["beta_ratio"],
            "partial_rho": med_a["rho_partial"],
            "rho_uni": med_a["rho_uni"],
            "t_scaling_slope": mean_slope,
            "extra": mean_cv,
        },
        {
            "mechanism": "b_within_basin",
            "covariate": "pre_cycle_div",
            "hypothesis": "H2",
            "passes": h2,
            "beta_ratio": med_b["beta_ratio"],
            "partial_rho": med_b["rho_partial"],
            "rho_uni": med_b["rho_uni"],
            "t_scaling_slope": float("nan"),
            "extra": float("nan"),
        },
        {
            "mechanism": "c_party_oscillation",
            "covariate": "party_osc_frac",
            "hypothesis": "H3",
            "passes": h3,
            "beta_ratio": med_a["beta_ratio"],
            "partial_rho": med_a["rho_partial"],
            "rho_uni": med_a["rho_uni"],
            "t_scaling_slope": float("nan"),
            "extra": auc_party - auc_med,
        },
        {
            "mechanism": "d_panel_composition",
            "covariate": "leave_one_group",
            "hypothesis": "H4",
            "passes": h4,
            "beta_ratio": float("nan"),
            "partial_rho": float("nan"),
            "rho_uni": float("nan"),
            "t_scaling_slope": float("nan"),
            "extra": float("nan"),
        },
    ]

    passing = [m for m in mech_rows if m["passes"] and m["mechanism"] != "d_panel_composition"]
    winner = ""
    if passing:
        # Smallest |β_ratio|; tie → larger drop in |Spearman|.
        def rank_key(m):
            ratio = m["beta_ratio"] if not math.isnan(m["beta_ratio"]) else 1e9
            drop = abs(m["rho_uni"]) - abs(m["partial_rho"]) if not math.isnan(
                m["partial_rho"]
            ) else -1e9
            return (ratio, -drop)

        passing.sort(key=rank_key)
        winner = passing[0]["mechanism"]
    elif not any(m["passes"] for m in mech_rows if m["mechanism"].startswith(("a", "b", "c"))):
        # Descriptive: smallest ratio among a–c anyway.
        candidates = [m for m in mech_rows if m["mechanism"].startswith(("a", "b", "c"))]
        candidates.sort(
            key=lambda m: m["beta_ratio"] if not math.isnan(m["beta_ratio"]) else 1e9
        )
        # winner stays empty for verdict; report descriptive in print
        print(
            f"  descriptive lowest β_ratio: {candidates[0]['mechanism']} "
            f"({candidates[0]['beta_ratio']:.4f})"
        )

    # Verdict word.
    if not h0:
        verdict = "GAP_ASSOC_FLUKE"
    elif h1 and winner == "a_phase_artifact":
        verdict = "GAP_PHASE_ARTIFACT"
    elif h2 and winner == "b_within_basin":
        verdict = "GAP_WITHIN_BASIN_HETERO"
    elif h3 and winner == "c_party_oscillation":
        verdict = "GAP_PARTY_OSCILLATION"
    elif h4 and not (h1 or h2 or h3):
        verdict = "GAP_PANEL_COMPOSITION"
    elif not (h1 or h2 or h3 or h4):
        verdict = "GAP_UNEXPLAINED"
    else:
        verdict = "GAP_DECOMPOSITION_INCONCLUSIVE"

    print(f"verdict: {verdict}")
    if winner:
        print(f"ranking winner: {winner}")

    summary = {
        "ci": 0,
        "n_forms": len(form_rows),
        "n_triadic": sum(1 for t in triadic if t),
        "n_dyadic": sum(1 for t in triadic if not t),
        "h0": h0_status,
        "h1": h1_status,
        "h2": h2_status,
        "h3": h3_status,
        "h4": h4_status,
        "h5": h5_status,
        "verdict": verdict,
        "winner": winner,
        "auc": auc,
        "auc_ci_lo": auc_lo,
        "auc_ci_hi": auc_hi,
        "auc_perm_p": auc_p,
        "mean_t_slope": mean_slope,
        "mean_gapT_cv": mean_cv,
        "beta_ratio_osc": med_a["beta_ratio"],
        "beta_ratio_div": med_b["beta_ratio"],
        "partial_rho_osc": med_a["rho_partial"],
        "partial_rho_div": med_b["rho_partial"],
        "rho_uni": med_a["rho_uni"],
        "auc_party": auc_party,
        "auc_mediator": auc_med,
        "rho_party": rho_party,
        "rho_mediator": rho_med,
        "beta_gap_uni": med_a["beta_uni"],
        "beta_gap_uni_p": med_a["p_uni"],
    }
    write_csv(os.path.join(RESULTS, "forms.csv"), form_rows)
    write_csv(os.path.join(RESULTS, "summary.csv"), [summary])
    write_csv(os.path.join(RESULTS, "mechanisms.csv"), mech_rows)
    write_csv(os.path.join(RESULTS, "leave_one_group.csv"), logo_rows)
    write_csv(
        os.path.join(RESULTS, "mediation.csv"),
        [
            {"mechanism": "a_osc", **{k: med_a[k] for k in med_a}},
            {"mechanism": "b_div", **{k: med_b[k] for k in med_b}},
        ],
    )


if __name__ == "__main__":
    main()
