"""Unit tests for the EoA instrument on forms with known answers.

Run:  python -m org_frontier.ergodicity.test_eoa
  or: python org_frontier/ergodicity/test_eoa.py

No Φ. Decision thresholds match the frozen defaults (ε_div=0.1, τ=0.25).
"""

from __future__ import annotations

import os
import sys
import unittest

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from org_frontier.ergodicity.eoa import (
    REFERENCE_BASIN,
    REFERENCE_STATIONARY,
    REFERENCE_UNIFORM,
    bit_observable,
    control_full_cycle_n3,
    control_identity_single,
    control_two_absorbing,
    rules_to_next_map,
    run_eoa,
    run_eoa_parties,
    uniform_ensemble,
)
from org_frontier.ergodicity._boolean_ergo import find_attractors


class TestEoAKnownAnswers(unittest.TestCase):
    def test_two_absorbing_mixed_starts_breaking(self):
        """maj3-like two poles: mixed uniform starts ⇒ EoA BREAKING."""
        rules = control_two_absorbing()
        attrs = find_attractors(rules_to_next_map(rules))
        self.assertGreaterEqual(len(attrs), 2)
        res = run_eoa_parties(
            rules, party_indices=(0, 2), labels=("W", "S", "C"), horizon=64
        )
        self.assertEqual(res.verdict, "BREAKING")
        self.assertGreaterEqual(res.fail_rate, 0.25)
        self.assertEqual(res.reference_mode, REFERENCE_UNIFORM)

    def test_two_absorbing_singleton_attractor_agreeing(self):
        """Ensemble concentrated on the 000 attractor ⇒ AGREEING for bit 0."""
        rules = control_two_absorbing()
        res = run_eoa(
            rules,
            bit_observable(0),
            ensemble=[(0, 0, 0)],
            horizon=64,
            observable_name="W",
        )
        self.assertEqual(res.verdict, "AGREEING")
        self.assertAlmostEqual(res.gap_mean, 0.0, places=9)

    def test_identity_singleton_ensemble_agreeing(self):
        """Identity map, start fixed at 000, ensemble={000} ⇒ AGREEING."""
        rules = control_identity_single()
        start = (0, 0, 0)
        res = run_eoa(
            rules,
            bit_observable(0),
            ensemble=[start],
            horizon=32,
            observable_name="W",
        )
        self.assertEqual(res.verdict, "AGREEING")
        self.assertAlmostEqual(res.gap_mean, 0.0, places=9)

    def test_identity_mixed_ensemble_breaking(self):
        """Identity map with full mixed ensemble ⇒ BREAKING (2^n attractors)."""
        rules = control_identity_single()
        res = run_eoa(
            rules,
            bit_observable(0),
            ensemble=uniform_ensemble(3),
            horizon=32,
            observable_name="W",
        )
        self.assertEqual(res.verdict, "BREAKING")

    def test_full_cycle_single_attractor_agreeing(self):
        """Hamiltonian 8-cycle: one attractor; bit-0 EoA AGREEING under uniform."""
        nxt = control_full_cycle_n3()
        attrs = find_attractors(nxt)
        self.assertEqual(len(attrs), 1)
        res = run_eoa(
            nxt,
            bit_observable(0),
            ensemble=uniform_ensemble(3),
            horizon=64,
            observable_name="W",
        )
        self.assertEqual(res.verdict, "AGREEING")
        self.assertLess(res.fail_rate, 0.25)
        # Cycle mean of bit 0 is exactly 0.5; gaps should be small.
        self.assertLess(res.gap_mean, 0.1)

    def test_gap_se_nonnegative(self):
        rules = control_two_absorbing()
        res = run_eoa(rules, bit_observable(0), horizon=64, observable_name="W")
        self.assertGreaterEqual(res.gap_se, 0.0)
        self.assertGreaterEqual(res.gap_std, 0.0)
        self.assertEqual(res.n_trajectories, 8)


class TestEoABasinStationary(unittest.TestCase):
    def test_two_absorbing_basin_agreeing(self):
        """Two poles: basin-restricted reference ⇒ AGREEING (clears FP class)."""
        rules = control_two_absorbing()
        res = run_eoa_parties(
            rules,
            party_indices=(0, 2),
            labels=("W", "S", "C"),
            horizon=64,
            reference_mode=REFERENCE_BASIN,
        )
        self.assertEqual(res.reference_mode, REFERENCE_BASIN)
        self.assertEqual(res.verdict, "AGREEING")
        self.assertLess(res.fail_rate, 0.25)
        self.assertLess(res.gap_mean, 0.05)

    def test_two_absorbing_stationary_agreeing(self):
        """Two poles: attractor-measure reference ⇒ AGREEING."""
        rules = control_two_absorbing()
        res = run_eoa(
            rules,
            bit_observable(0),
            horizon=64,
            observable_name="W",
            reference_mode=REFERENCE_STATIONARY,
        )
        self.assertEqual(res.verdict, "AGREEING")
        self.assertLess(res.gap_mean, 0.1)

    def test_full_cycle_basin_and_stationary_agreeing(self):
        """Single mixing cycle stays AGREEING under both new modes."""
        nxt = control_full_cycle_n3()
        for mode in (REFERENCE_BASIN, REFERENCE_STATIONARY):
            res = run_eoa(
                nxt,
                bit_observable(0),
                horizon=64,
                observable_name="W",
                reference_mode=mode,
            )
            self.assertEqual(res.verdict, "AGREEING", msg=mode)
            self.assertLess(res.fail_rate, 0.25, msg=mode)

    def test_noise_finite_T_stationary_breaking(self):
        """Two poles + flip noise at finite T: stationary mode stays BREAKING.

        Global stationary mean of each party bit is ~0.5, but finite-T
        trajectories from polarized basins have not mixed, so time averages
        remain near 0 or 1 and the gap exceeds ε_div.
        """
        rules = control_two_absorbing()
        res = run_eoa_parties(
            rules,
            party_indices=(0, 2),
            labels=("W", "S", "C"),
            horizon=64,
            noise=0.1,
            seed=7,
            reference_mode=REFERENCE_STATIONARY,
        )
        self.assertEqual(res.reference_mode, REFERENCE_STATIONARY)
        self.assertEqual(res.verdict, "BREAKING")
        self.assertGreaterEqual(res.fail_rate, 0.25)

    def test_uniform_mode_backward_compatible(self):
        """Default reference_mode remains uniform and matches legacy verdict."""
        rules = control_two_absorbing()
        legacy = run_eoa_parties(
            rules, party_indices=(0, 2), labels=("W", "S", "C"), horizon=64
        )
        explicit = run_eoa_parties(
            rules,
            party_indices=(0, 2),
            labels=("W", "S", "C"),
            horizon=64,
            reference_mode=REFERENCE_UNIFORM,
        )
        self.assertEqual(legacy.verdict, explicit.verdict)
        self.assertAlmostEqual(legacy.fail_rate, explicit.fail_rate, places=9)
        self.assertAlmostEqual(legacy.gap_mean, explicit.gap_mean, places=9)


if __name__ == "__main__":
    unittest.main(verbosity=2)
