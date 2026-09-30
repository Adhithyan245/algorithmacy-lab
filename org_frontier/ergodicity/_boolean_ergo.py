"""Shared finite-Boolean ergodicity helpers for the Ergodicity × Algorithmacy track.

Attractors = ergodic components on deterministic maps. Exact Φ via lab
instrument. No results here — import only.
"""

from __future__ import annotations

import math
from typing import Callable, Iterable

import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify_rules,
    cm_from_rules,
    tpm_from_rules,
)
from foundations.proxy_audit.exact_phi import exact_big_phi
from org_frontier.probes.lib import verdict as vlib

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

LABELS3 = ("W", "S", "C")
N3 = 3


def rules_memoryless():
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]


def rules_sticky():
    return [lambda x: x[1], lambda x: (x[0] & x[2]) | x[1], lambda x: x[1]]


def rules_xor_memory():
    return [lambda x: x[1], lambda x: (x[0] & x[2]) ^ x[1], lambda x: x[1]]


def rules_or_commit():
    return [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]]


def rules_sticky_or():
    return [lambda x: x[1], lambda x: (x[0] | x[2]) | x[1], lambda x: x[1]]


def rules_sticky_parity():
    return [lambda x: x[1], lambda x: (x[0] ^ x[2]) | x[1], lambda x: x[1]]


def rules_parity_hub():
    return [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]]


def rules_maj3():
    def maj(x):
        return 1 if (x[0] + x[1] + x[2]) >= 2 else 0

    return [maj, maj, maj]


def rules_w_follows_c():
    return [lambda x: x[2], lambda x: x[0] & x[2], lambda x: x[1]]


def rules_ejected_latch():
    """Absorbing inactive mediator: once S=0, stays 0; else S'=W∧C."""

    def s_rule(x):
        if x[1] == 0:
            return 0
        return x[0] & x[2]

    return [lambda x: x[1], s_rule, lambda x: x[1]]


def rules_ejected_latch_or():
    def s_rule(x):
        if x[1] == 0:
            return 0
        return x[0] | x[2]

    return [lambda x: x[1], s_rule, lambda x: x[1]]


PANEL_B1 = {
    "memoryless": rules_memoryless,
    "sticky": rules_sticky,
    "xor_memory": rules_xor_memory,
    "or_commit": rules_or_commit,
    "sticky_or": rules_sticky_or,
    "sticky_parity": rules_sticky_parity,
    "parity_hub": rules_parity_hub,
    "maj3": rules_maj3,
    "w_follows_c": rules_w_follows_c,
}


def next_map(rules: list[Callable], n: int = N3):
    nxt = {}
    for s in range(2**n):
        cur = tuple((s >> i) & 1 for i in range(n))
        nxt[cur] = tuple(int(rules[j](cur)) for j in range(n))
    return nxt


def find_attractors(nxt):
    """Return list of (cycle_tuple, basin_frozenset)."""
    cycle_of = {}
    cycles = {}
    states = list(nxt.keys())
    for start_state in states:
        cur = start_state
        path = []
        vis = {}
        while cur not in vis:
            if cur in cycle_of:
                break
            vis[cur] = len(path)
            path.append(cur)
            cur = nxt[cur]
        if cur in vis:
            cyc = tuple(path[vis[cur] :])
            key = frozenset(cyc)
            cyc_c = min(tuple(cyc[i:] + cyc[:i]) for i in range(len(cyc)))
            cycles[key] = cyc_c
            for st in cyc:
                cycle_of[st] = key

    basins = {k: set() for k in cycles}
    for start_state in states:
        cur = start_state
        seen = []
        visited = set()
        while cur not in visited:
            visited.add(cur)
            seen.append(cur)
            cur = nxt[cur]
        key = cycle_of[cur]
        basins[key].update(seen)

    return [(cycles[k], frozenset(basins[k])) for k in cycles]


def attractor_phi(rules, cyc, labels=LABELS3):
    tpm = tpm_from_rules(rules)
    cm = cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    rows = []
    for st in cyc:
        phi = exact_big_phi(tpm, cm, st)
        phi_f = 0.0 if phi is None else float(phi)
        core = None
        mc_phi = float("nan")
        try:
            mc = new_big_phi.maximal_complex(net, st)
            ni = getattr(mc, "node_indices", None)
            if ni is not None:
                core = tuple(labels[i] for i in ni)
                mc_phi = float(mc.phi)
        except Exception:
            pass
        rows.append({
            "state": "".join(str(b) for b in st),
            "phi_mip": phi_f,
            "core": "{" + ",".join(core) + "}" if core else "(none)",
            "core_tuple": core if core else tuple(),
            "mc_phi": mc_phi,
        })
    max_phi = max(r["phi_mip"] for r in rows) if rows else 0.0
    verdict = "triadic" if max_phi > PHI_EPS else "dyadic"
    return verdict, max_phi, rows


def party_cycle_avg(cyc, party_idx: int) -> float:
    return sum(st[party_idx] for st in cyc) / float(len(cyc))


def party_uniform_avg(n: int, party_idx: int) -> float:
    # each bit is 1 in exactly half of 2^n states
    return 0.5


def basin_entropy(basin_sizes: Iterable[int], n: int) -> float:
    total = float(2**n)
    h = 0.0
    for b in basin_sizes:
        if b <= 0:
            continue
        p = b / total
        h -= p * math.log(p, 2)
    return h


def skew_factor_s_independent(rules, labels=LABELS3) -> bool:
    """True iff S' does not depend on current S (bit index 1)."""
    s_idx = labels.index("S")
    # brute force: for all states, flip S and see if S' changes
    n = len(labels)
    for s in range(2**n):
        cur = tuple((s >> i) & 1 for i in range(n))
        flipped = list(cur)
        flipped[s_idx] = 1 - flipped[s_idx]
        flipped = tuple(flipped)
        if int(rules[s_idx](cur)) != int(rules[s_idx](flipped)):
            return False
    return True


def instrument_gates():
    v_m = vlib(rules_memoryless(), LABELS3)
    ctrl_m = v_m.structure == "triadic" and abs(v_m.max_phi - 2.0) < 1e-6
    v_s = vlib(rules_sticky(), LABELS3)
    ctrl_s = v_s.structure == "dyadic" and abs(v_s.max_phi) < 1e-6
    return {
        "memoryless": v_m,
        "sticky": v_s,
        "ctrl_memoryless": ctrl_m,
        "ctrl_sticky": ctrl_s,
        "ok": ctrl_m and ctrl_s,
    }


def whole_verdict(rules, labels=LABELS3):
    return classify_rules(rules, labels=labels)


def mean_return_time_to_set(nxt, target: set) -> float:
    """Mean finite return time to target over starts that eventually hit it."""
    times = []
    for start in nxt.keys():
        cur = start
        t = 0
        seen = {}
        hit = None
        while cur not in seen:
            seen[cur] = t
            if t >= 1 and cur in target:
                hit = t
                break
            cur = nxt[cur]
            t += 1
            if t > len(nxt) + 2:
                break
        # also handle start already in target: first return
        if hit is None and start in target:
            cur = nxt[start]
            t = 1
            seen = {start: 0}
            while cur not in seen:
                if cur in target:
                    hit = t
                    break
                seen[cur] = t
                cur = nxt[cur]
                t += 1
                if t > len(nxt) + 2:
                    break
        if hit is not None:
            times.append(hit)
    if not times:
        return float("inf")
    return sum(times) / float(len(times))


def inactive_basin_mass(attrs, n: int = N3) -> float:
    """Basin mass of attractors whose every state is 000...0."""
    zero = tuple(0 for _ in range(n))
    mass = 0
    for cyc, basin in attrs:
        if all(st == zero for st in cyc) or (len(cyc) == 1 and cyc[0] == zero):
            mass += len(basin)
        elif all(sum(st) == 0 for st in cyc):
            mass += len(basin)
    return mass / float(2**n)


def inactive000_basin_mass(attrs, n: int = N3) -> float:
    zero = tuple(0 for _ in range(n))
    mass = 0
    for cyc, basin in attrs:
        if set(cyc) == {zero}:
            mass += len(basin)
    return mass / float(2**n)
