"""Ergodicity × Algorithmacy first cell — components / divergence vs Φ_MIP.

Strand B1–B3 (+ E4 witness). Hypotheses fixed in hypotheses.md before
computing. Exact binary IIT-4.0.

Run:  python org_frontier/studies/ergodic_components_vs_phi/analyze_components.py
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
    LABELS3,
    N3,
    PANEL_B1,
    attractor_phi,
    basin_entropy,
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
DELTA_C = 0.5
DELTA_H = 0.1


def main():
    print("ERGODIC COMPONENTS vs Φ_MIP — Strand B1–B3 first cell")
    print("=" * 80)
    print("  hypotheses fixed in hypotheses.md before computing")
    print("  measure: attractors/basins; party time–ensemble divergence; exact Φ")
    print("  panel: 9 designed n=3 forms (frozen)")
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
    attr_rows = []
    div_rows = []
    coexist_forms = []

    print("PANEL — components × Φ")
    print("-" * 80)
    print(
        f"  {'form':<16} {'whole':<8} {'n_c':>3} {'H_b':>6} "
        f"{'tri_a':>5} {'dya_a':>5}  div_frac"
    )

    for name, builder in PANEL_B1.items():
        rules = builder()
        nxt = next_map(rules)
        attrs = find_attractors(nxt)
        whole = whole_verdict(rules)
        sizes = [len(b) for _, b in attrs]
        h_b = basin_entropy(sizes, N3)
        n_tri = 0
        n_dya = 0
        n_div_cells = 0
        n_div_denom = 0
        cores_by_attr = []
        party_avgs_by_attr = []

        # Precompute cycle averages and basin-weighted mixture (ensemble over starts)
        cycle_avgs = []
        for cyc, basin in attrs:
            cycle_avgs.append({
                lab: party_cycle_avg(cyc, i) for i, lab in enumerate(LABELS3)
            })
        mixture = {}
        for i, lab in enumerate(LABELS3):
            mixture[lab] = sum(
                cycle_avgs[k][lab] * (len(attrs[k][1]) / float(2**N3))
                for k in range(len(attrs))
            )

        for idx, (cyc, basin) in enumerate(attrs):
            verdict, max_phi, state_rows = attractor_phi(rules, cyc)
            if verdict == "triadic":
                n_tri += 1
            else:
                n_dya += 1
            cores = {tuple(r["core_tuple"]) for r in state_rows}
            cores_by_attr.append(cores)
            pav = cycle_avgs[idx]
            party_avgs_by_attr.append(pav)
            cyc_str = "|".join("".join(str(b) for b in st) for st in cyc)
            attr_rows.append({
                "form": name,
                "attr_id": idx,
                "cycle": cyc_str,
                "period": len(cyc),
                "basin": len(basin),
                "verdict": verdict,
                "max_phi": max_phi,
                "cores": ";".join(
                    "{" + ",".join(c) + "}" if c else "(none)" for c in cores
                ),
            })
            for i, lab in enumerate(LABELS3):
                if lab == "S":
                    continue
                t_avg = pav[lab]
                e_cycle = t_avg  # uniform-on-attractor = time avg on a cycle (derived 0 gap)
                e_mix = mixture[lab]  # ensemble over uniform starts → basin mixture
                e_space = party_uniform_avg(N3, i)
                # Operational EoA for H3: |time_avg in component − ensemble over starts|
                div_mix = abs(t_avg - e_mix)
                div_space = abs(t_avg - e_space)
                n_div_denom += 1
                flag = div_mix > EPS_DIV
                if flag:
                    n_div_cells += 1
                div_rows.append({
                    "form": name,
                    "attr_id": idx,
                    "party": lab,
                    "time_avg": t_avg,
                    "ens_cycle": e_cycle,
                    "ens_mixture": e_mix,
                    "ens_space": e_space,
                    "div_primary_vacuous": abs(t_avg - e_cycle),
                    "div_mixture": div_mix,
                    "div_secondary": div_space,
                    "fail_eps": int(flag),
                    "whole_structure": whole.structure,
                    "attr_verdict": verdict,
                })

        if n_tri >= 1 and n_dya >= 1:
            coexist_forms.append(name)

        # E4: basins disagree on core or party occupancy
        core_disagree = False
        if len(cores_by_attr) >= 2:
            flat = [next(iter(c)) if c else tuple() for c in cores_by_attr]
            core_disagree = len(set(flat)) >= 2
        occ_disagree = False
        if len(party_avgs_by_attr) >= 2:
            for lab in ("W", "C"):
                vals = [p[lab] for p in party_avgs_by_attr]
                if max(vals) - min(vals) >= EPS_DIV:
                    occ_disagree = True
                    break

        div_frac = n_div_cells / n_div_denom if n_div_denom else 0.0
        form_rows.append({
            "form": name,
            "whole_structure": whole.structure,
            "whole_phi": float(whole.max_phi),
            "n_components": len(attrs),
            "basin_entropy": h_b,
            "n_triadic_attr": n_tri,
            "n_dyadic_attr": n_dya,
            "div_frac": div_frac,
            "n_div_cells": n_div_cells,
            "n_div_denom": n_div_denom,
            "coexist": int(n_tri >= 1 and n_dya >= 1),
            "e4_core_disagree": int(core_disagree),
            "e4_occ_disagree": int(occ_disagree),
        })
        print(
            f"  {name:<16} {whole.structure:<8} {len(attrs):>3} {h_b:>6.3f} "
            f"{n_tri:>5} {n_dya:>5}  {div_frac:.3f}"
        )

    # Hypothesis tests
    tri_forms = [r for r in form_rows if r["whole_structure"] == "triadic"]
    dya_forms = [r for r in form_rows if r["whole_structure"] == "dyadic"]
    mean_c_tri = (
        sum(r["n_components"] for r in tri_forms) / len(tri_forms)
        if tri_forms else float("nan")
    )
    mean_c_dya = (
        sum(r["n_components"] for r in dya_forms) / len(dya_forms)
        if dya_forms else float("nan")
    )
    mean_h_tri = (
        sum(r["basin_entropy"] for r in tri_forms) / len(tri_forms)
        if tri_forms else float("nan")
    )
    mean_h_dya = (
        sum(r["basin_entropy"] for r in dya_forms) / len(dya_forms)
        if dya_forms else float("nan")
    )

    # H3: fraction of div cells among triadic-form attractors vs dyadic-form
    def _div_frac_for(struct):
        cells = [d for d in div_rows if d["whole_structure"] == struct]
        if not cells:
            return float("nan")
        return sum(d["fail_eps"] for d in cells) / len(cells)

    frac_tri = _div_frac_for("triadic")
    frac_dya = _div_frac_for("dyadic")

    h1 = (mean_c_tri - mean_c_dya) >= DELTA_C
    h2 = (mean_h_tri - mean_h_dya) >= DELTA_H
    h3 = frac_tri > frac_dya  # higher among triadic

    # H4: coexistence ⇒ cross-basin party gap
    h4_forms = []
    h4_ok = True
    h4_any = False
    for name in coexist_forms:
        fr = next(r for r in form_rows if r["form"] == name)
        # recompute cross-basin from attr party avgs
        attrs_p = [d for d in div_rows if d["form"] == name]
        by_attr = {}
        for d in attrs_p:
            by_attr.setdefault(d["attr_id"], {}).setdefault(d["party"], d["time_avg"])
        # need attr verdicts
        attr_ver = {
            r["attr_id"]: r["verdict"]
            for r in attr_rows if r["form"] == name
        }
        tri_ids = [i for i, v in attr_ver.items() if v == "triadic"]
        dya_ids = [i for i, v in attr_ver.items() if v == "dyadic"]
        split = False
        for ti in tri_ids:
            for di in dya_ids:
                for party in ("W", "C"):
                    gap = abs(by_attr[ti][party] - by_attr[di][party])
                    if gap >= EPS_DIV:
                        split = True
        h4_forms.append((name, split))
        h4_any = True
        if not split:
            h4_ok = False
    h4 = h4_any and h4_ok

    # E4 secondary: fraction of multistable forms with core or occ disagree
    multi = [r for r in form_rows if r["n_components"] >= 2]
    e4_hits = sum(
        1 for r in multi if r["e4_core_disagree"] or r["e4_occ_disagree"]
    )
    e4_rate = e4_hits / len(multi) if multi else 0.0
    e4 = e4_rate >= (2.0 / 3.0)

    if h1 and h3:
        verdict_word = "COMPONENTS_TRACK_TRIAD"
    elif h1:
        verdict_word = "COUNT_ONLY"
    elif h3:
        verdict_word = "DIVERGENCE_ONLY"
    else:
        verdict_word = "NO_ERGODIC_SIGNATURE"
    secondary = []
    if h4:
        secondary.append("CROSS_BASIN_SPLIT")
    if e4:
        secondary.append("BASIN_DETERMINATION_SPLIT")
    if h2 and h1:
        secondary.append("ENTROPY_WITNESS")

    reading = (
        f"{verdict_word} — mean n_components tri={mean_c_tri:.3f} "
        f"dya={mean_c_dya:.3f} (Δ={mean_c_tri-mean_c_dya:.3f}); "
        f"div_frac tri={frac_tri:.3f} dya={frac_dya:.3f}; "
        f"coexist={coexist_forms}; E4_rate={e4_rate:.3f}"
    )

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  mean components: triadic={mean_c_tri:.4f}  dyadic={mean_c_dya:.4f}  "
          f"Δ={mean_c_tri-mean_c_dya:.4f}  (need ≥{DELTA_C})")
    print(f"  mean basin H:    triadic={mean_h_tri:.4f}  dyadic={mean_h_dya:.4f}  "
          f"Δ={mean_h_tri-mean_h_dya:.4f}  (need ≥{DELTA_H})")
    print(f"  div_frac (vs basin-mixture ens): triadic={frac_tri:.4f}  dyadic={frac_dya:.4f}")
    print(f"  coexist forms: {coexist_forms}")
    print(f"  H4 per coexist: {h4_forms}")
    print(f"  E4 multistable split rate: {e4_hits}/{len(multi)} = {e4_rate:.3f}")
    print(f"  H1 (component count tracks verdict): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (basin entropy tracks verdict):   {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (divergence tracks mediation):    {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (coexistence ⇒ cross-basin split):{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  E4 (basins disagree core/occ):       {'SUPPORTED' if e4 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    if secondary:
        print(f"  secondary: {'|'.join(secondary)}")
    print(
        f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
        f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
        f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
        f"H4={('SUPPORTED' if h4 else 'REFUTED')}"
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
            out = dict(r)
            out["whole_phi"] = f"{r['whole_phi']:.8f}"
            out["basin_entropy"] = f"{r['basin_entropy']:.8f}"
            out["div_frac"] = f"{r['div_frac']:.8f}"
            w.writerow(out)

    with open(os.path.join(RESULTS, "attractors.csv"), "w", newline="") as fh:
        fields = ["form", "attr_id", "cycle", "period", "basin",
                  "verdict", "max_phi", "cores"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in attr_rows:
            w.writerow({**r, "max_phi": f"{r['max_phi']:.8f}"})

    with open(os.path.join(RESULTS, "divergence.csv"), "w", newline="") as fh:
        fields = list(div_rows[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in div_rows:
            out = {
                **r,
                "time_avg": f"{r['time_avg']:.8f}",
                "ens_cycle": f"{r['ens_cycle']:.8f}",
                "ens_mixture": f"{r['ens_mixture']:.8f}",
                "ens_space": f"{r['ens_space']:.8f}",
                "div_primary_vacuous": f"{r['div_primary_vacuous']:.8f}",
                "div_mixture": f"{r['div_mixture']:.8f}",
                "div_secondary": f"{r['div_secondary']:.8f}",
            }
            w.writerow(out)

    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "e4": "SUPPORTED" if e4 else "REFUTED",
            "verdict": verdict_word,
            "secondary": "|".join(secondary),
            "mean_c_tri": f"{mean_c_tri:.6f}",
            "mean_c_dya": f"{mean_c_dya:.6f}",
            "mean_h_tri": f"{mean_h_tri:.6f}",
            "mean_h_dya": f"{mean_h_dya:.6f}",
            "frac_tri": f"{frac_tri:.6f}",
            "frac_dya": f"{frac_dya:.6f}",
            "coexist_forms": "|".join(coexist_forms),
            "e4_rate": f"{e4_rate:.6f}",
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
