"""Unit tests for settling-time measures on forms with known answers.

Run:  python -m org_frontier.ergodicity.test_settling
  or: python org_frontier/ergodicity/test_settling.py

No Φ. Thresholds match the frozen defaults (ε_conv=0.01, ε_flip=0.05).
"""

from __future__ import annotations

import math
import os
import sys
import unittest

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from org_frontier.ergodicity.eoa import (
    bit_observable,
    control_full_cycle_n3,
    control_identity_single,
    control_two_absorbing,
    rules_to_next_map,
    uniform_ensemble,
)
from org_frontier.ergodicity.settling import (
    DEFAULT_EPS_CONV,
    DEFAULT_EPS_FLIP,
    control_chain_to_fixed,
    control_two_step_cycle,
    convergence_time,
    spectral_gap,
    summarize_convergence,
    summarize_mixing,
    summarize_transients,
    transient_length,
    tv_mixing_bound,
)


class TestTransientKnownAnswers(unittest.TestCase):
    def test_identity_all_zero(self):
        """Identity map: every state is a fixed point ⇒ transient = 0."""
        rules = control_identity_single()
        nxt = rules_to_next_map(rules)
        for s in uniform_ensemble(3):
            self.assertEqual(transient_length(nxt, s), 0)
        summary = summarize_transients(nxt)
        self.assertAlmostEqual(summary.mean, 0.0, places=9)
        self.assertAlmostEqual(summary.max, 0.0, places=9)
        self.assertAlmostEqual(summary.basin_weighted_mean, 0.0, places=9)
        self.assertEqual(summary.n_attractors, 8)
        self.assertEqual(summary.max_period, 1)

    def test_full_cycle_all_zero(self):
        """Hamiltonian 8-cycle: every state is on the cycle ⇒ transient = 0."""
        nxt = control_full_cycle_n3()
        summary = summarize_transients(nxt)
        self.assertAlmostEqual(summary.mean, 0.0, places=9)
        self.assertEqual(summary.n_attractors, 1)
        self.assertEqual(summary.max_period, 8)
        self.assertAlmostEqual(summary.mean_period, 8.0, places=9)

    def test_chain_to_fixed_hamming(self):
        """Drain-to-000 map: transient length = Hamming weight; mean = 1.5."""
        nxt = control_chain_to_fixed()
        expected = {
            (0, 0, 0): 0,
            (1, 0, 0): 1,
            (0, 1, 0): 1,
            (0, 0, 1): 1,
            (1, 1, 0): 2,
            (1, 0, 1): 2,
            (0, 1, 1): 2,
            (1, 1, 1): 3,
        }
        for st, L in expected.items():
            self.assertEqual(transient_length(nxt, st), L, msg=st)
        summary = summarize_transients(nxt)
        self.assertAlmostEqual(summary.mean, 1.5, places=9)
        self.assertAlmostEqual(summary.max, 3.0, places=9)
        self.assertAlmostEqual(summary.basin_weighted_mean, 1.5, places=9)
        self.assertEqual(summary.n_attractors, 1)
        self.assertEqual(summary.max_period, 1)

    def test_two_step_cycle_transients(self):
        """2-cycle plus one-step drain: transient 0 on cycle, 1 elsewhere."""
        nxt = control_two_step_cycle()
        self.assertEqual(transient_length(nxt, (0, 0, 0)), 0)
        self.assertEqual(transient_length(nxt, (1, 0, 0)), 0)
        self.assertEqual(transient_length(nxt, (0, 1, 0)), 1)
        summary = summarize_transients(nxt)
        # 2 starts with L=0, 6 with L=1 ⇒ mean = 6/8 = 0.75
        self.assertAlmostEqual(summary.mean, 0.75, places=9)
        self.assertEqual(summary.n_attractors, 1)
        self.assertEqual(summary.max_period, 2)


class TestConvergenceKnownAnswers(unittest.TestCase):
    def test_fixed_point_converges_at_one(self):
        """On an absorbing state, Ā_1 already equals the cycle mean."""
        nxt = control_chain_to_fixed()
        obs = bit_observable(0)
        T = convergence_time(nxt, (0, 0, 0), obs, eps_conv=DEFAULT_EPS_CONV)
        self.assertEqual(T, 1)

    def test_chain_nonzero_start_needs_burn_in(self):
        """From 111, bit-0 starts at 1 and the attractor mean is 0.

        The cumulative average of bit 0 along 111→011→001→000→000… is
        1, 0.5, 1/3, 0.25, … so the first T with |Ā_T| < 0.01 is T=101
        (1/T < 0.01). Cap at a smaller t_max to mark unresolved.
        """
        nxt = control_chain_to_fixed()
        obs = bit_observable(0)
        T = convergence_time(nxt, (1, 1, 1), obs, eps_conv=0.01, t_max=50)
        self.assertEqual(T, 51)  # unresolved under t_max=50
        T_ok = convergence_time(nxt, (1, 1, 1), obs, eps_conv=0.01, t_max=200)
        self.assertEqual(T_ok, 101)

    def test_identity_party_summary(self):
        """Identity: every start is already at its attractor mean ⇒ mean_T=1."""
        rules = control_identity_single()
        summary = summarize_convergence(rules, party_indices=(0, 1, 2))
        self.assertAlmostEqual(summary.mean_T, 1.0, places=9)
        self.assertEqual(summary.n_unresolved, 0)
        self.assertEqual(summary.n_cells, 8 * 3)


class TestMixingKnownAnswers(unittest.TestCase):
    def test_identity_positive_gap_under_noise(self):
        """Flip noise on the identity map yields a positive spectral gap."""
        rules = control_identity_single()
        mix = summarize_mixing(rules, eps_flip=DEFAULT_EPS_FLIP)
        self.assertGreater(mix.spectral_gap, 0.0)
        self.assertFalse(math.isinf(mix.relaxation_time))
        self.assertEqual(mix.n_states, 8)

    def test_two_absorbing_zero_gap(self):
        """maj3-like poles under single-bit flip noise stay reducible.

        Deterministic image is 000 or 111; flipping one bit of that image
        never crosses the weight-1 / weight-2 cut, so the chain has two
        communicating classes and spectral gap 0 (relaxation = +inf).
        """
        rules = control_two_absorbing()
        mix = summarize_mixing(rules, eps_flip=0.05)
        self.assertAlmostEqual(mix.spectral_gap, 0.0, places=9)
        self.assertTrue(math.isinf(mix.relaxation_time))

    def test_full_cycle_gap(self):
        """Single mixing cycle under noise still has a well-defined gap."""
        nxt = control_full_cycle_n3()
        mix = summarize_mixing(nxt, eps_flip=0.05)
        self.assertGreater(mix.spectral_gap, 0.0)
        bound = tv_mixing_bound(mix.spectral_gap, 0.25)
        self.assertGreater(bound, 0.0)
        self.assertFalse(math.isinf(bound))

    def test_spectral_gap_singleton(self):
        P = [[1.0]]
        self.assertAlmostEqual(spectral_gap(P), 1.0, places=9)

    def test_eps_flip_must_be_positive(self):
        rules = control_identity_single()
        with self.assertRaises(ValueError):
            summarize_mixing(rules, eps_flip=0.0)


class TestOscillationAndPathDiversity(unittest.TestCase):
    def test_identity_no_oscillation(self):
        """Every state a fixed point ⇒ party bits constant on every cycle."""
        from org_frontier.ergodicity.settling import summarize_oscillation

        rules = control_identity_single()
        osc = summarize_oscillation(rules, party_indices=(0, 2))
        self.assertAlmostEqual(osc.party_osc_frac, 0.0, places=9)
        self.assertAlmostEqual(osc.mean_cycle_var, 0.0, places=9)
        self.assertEqual(osc.max_period, 1)
        self.assertEqual(osc.n_attractors, 8)

    def test_full_cycle_full_oscillation(self):
        """Hamiltonian 8-cycle: each bit takes both values ⇒ osc_frac=1."""
        from org_frontier.ergodicity.settling import summarize_oscillation

        nxt = control_full_cycle_n3()
        osc = summarize_oscillation(nxt, party_indices=(0, 2))
        self.assertAlmostEqual(osc.party_osc_frac, 1.0, places=9)
        self.assertAlmostEqual(osc.mean_cycle_var, 0.25, places=9)
        self.assertEqual(osc.max_period, 8)
        self.assertEqual(osc.n_attractors, 1)

    def test_two_step_cycle_bit0_oscillates(self):
        """000↔100: bit 0 oscillates; bits 1,2 constant on the unique cycle."""
        from org_frontier.ergodicity.settling import summarize_oscillation

        nxt = control_two_step_cycle()
        # Only one attractor (the 2-cycle); drains go there.
        osc0 = summarize_oscillation(nxt, party_indices=(0,))
        self.assertAlmostEqual(osc0.party_osc_frac, 1.0, places=9)
        osc12 = summarize_oscillation(nxt, party_indices=(1, 2))
        self.assertAlmostEqual(osc12.party_osc_frac, 0.0, places=9)

    def test_identity_pre_cycle_div_zero(self):
        """Identity: every start on-cycle ⇒ pre_cycle_div = 0."""
        from org_frontier.ergodicity.settling import summarize_pre_cycle_diversity

        rules = control_identity_single()
        div = summarize_pre_cycle_diversity(rules, party_indices=(0, 2))
        self.assertAlmostEqual(div.pre_cycle_div, 0.0, places=9)
        self.assertAlmostEqual(div.mean_transient, 0.0, places=9)
        self.assertEqual(div.scale, 4)

    def test_chain_pre_cycle_div_positive(self):
        """Hamming drain: nonzero starts visit distinct party patterns."""
        from org_frontier.ergodicity.settling import summarize_pre_cycle_diversity

        nxt = control_chain_to_fixed()
        div = summarize_pre_cycle_diversity(nxt, party_indices=(0, 2))
        self.assertGreater(div.pre_cycle_div, 0.0)
        self.assertAlmostEqual(div.mean_transient, 1.5, places=9)


if __name__ == "__main__":
    unittest.main(verbosity=2)
