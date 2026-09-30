import unittest

from cases.real_gc_01.ai_compute.model import (
    Environment, POLICIES, consider, environments, initial_state, run, transition,
)


class PurposeTrialTests(unittest.TestCase):
    def test_information_and_ranking_identical_before_qualification(self):
        env = Environment(1, 0, 3, 0)
        state = initial_state(env)
        decisions = [consider(state, "US", p, "expand_capacity", env, 0) for p in POLICIES]
        for left, right in zip(*(d["candidates"] for d in decisions)):
            for key in ("candidate_purpose", "anticipated_state", "anticipated_new_channel_losses", "local_return_assumption"):
                self.assertEqual(left[key], right[key])
        self.assertNotEqual(decisions[0]["selected_purpose"], decisions[1]["selected_purpose"])

    def test_other_subject_alone_can_change_admission(self):
        env = Environment(1, 0, 3, 0)
        state = initial_state(env)
        decision = consider(state, "US", POLICIES[1], "expand_capacity", env, 0)
        expand = decision["candidates"][0]
        self.assertFalse(expand["anticipated_state"]["closed"]["US"])
        self.assertTrue(expand["anticipated_state"]["closed"]["third_parties"])
        self.assertFalse(expand["eligible_before_purpose_selection"])

    def test_forecast_cannot_restore_already_closed_channels(self):
        env = Environment(1, 6, 1, 6)
        state = initial_state(env)
        state["closed"]["third_parties"] = True
        decision = consider(state, "US", POLICIES[1], "restore_correction_time", env, 0)
        self.assertEqual(decision["status"], "NO_ADMISSIBLE_PURPOSE")
        self.assertIsNone(decision["selected_purpose"])
        after = transition(state, ("restore_correction_time",)*2, env, 0)
        self.assertTrue(after["closed"]["third_parties"])

    def test_matched_shock_sequences_and_named_subjects(self):
        env = Environment(2, 2, 3, 6)
        first = run(env, (POLICIES[0],)*2)
        second = run(env, (POLICIES[1],)*2)
        self.assertEqual(first["actual_shocks"], second["actual_shocks"])
        self.assertEqual(first["forecast_shocks"], second["forecast_shocks"])
        self.assertEqual(set(first["final_state"]["closed"]), {"US", "CN", "third_parties"})

    def test_failure_and_self_first_survival_are_retained(self):
        # A short finite trajectory remains open. It is not an infinite-horizon
        # counterexample. The frozen six-step grid is reported independently.
        short = run(Environment(1, 6, 1, 0, horizon=1), (POLICIES[0],)*2)
        self.assertFalse(any(short["final_state"]["closed"].values()))
        self.assertTrue(any(any(run(e, (POLICIES[1],)*2)["final_state"]["closed"].values()) for e in environments()))

    def test_role_exchange_symmetry(self):
        env = Environment(2, 0, 3, 0)
        left, right = run(env, POLICIES), run(env, POLICIES[::-1])
        self.assertEqual(left["final_state"]["strain"], right["final_state"]["strain"])
        self.assertEqual(left["final_state"]["capacity"]["US"], right["final_state"]["capacity"]["CN"])

    def test_invalid_inputs_rejected(self):
        with self.assertRaises(ValueError):
            Environment(True, 0, 1, 0)
        with self.assertRaises(ValueError):
            run(Environment(1, 0, 1, 0), ("unknown", POLICIES[0]))


if __name__ == "__main__":
    unittest.main()
