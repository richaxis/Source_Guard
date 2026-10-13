"""Offline source/design checks.

These checks do not emulate GenLayer consensus. Run with:
    python -m unittest discover -s tests
"""
import pathlib
import unittest

SOURCE = pathlib.Path(__file__).parents[1] / "contracts" / "source_guard.py"
CODE = SOURCE.read_text(encoding="utf-8")


class SourceGuardDesignChecks(unittest.TestCase):
    def test_has_consensus_evaluation(self):
        self.assertIn("gl.eq_principle.strict_eq(evaluate)", CODE)

    def test_requires_evidence_before_resolution(self):
        self.assertIn("Add at least one evidence source before resolving", CODE)

    def test_has_three_outcomes(self):
        for outcome in ('"supported"', '"refuted"', '"insufficient"'):
            self.assertIn(outcome, CODE)

    def test_has_challenge_flow(self):
        self.assertIn("def challenge_claim", CODE)
        self.assertIn('"challenged"', CODE)

    def test_has_read_methods(self):
        self.assertIn("def get_claims", CODE)
        self.assertIn("def get_evidence", CODE)


if __name__ == "__main__":
    unittest.main()
