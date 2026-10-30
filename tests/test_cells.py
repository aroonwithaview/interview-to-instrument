"""Offline tests: no model calls. Run with  python -m unittest discover tests"""
import unittest
from pathlib import Path

from cells import agreement, curate, quotecheck, replay
from cells.transcripts import load_dir

DATA = Path(__file__).resolve().parent.parent / "data" / "synthetic"


class TestTranscripts(unittest.TestCase):
    def test_parse(self):
        t = load_dir(DATA)["W"]
        self.assertEqual(len(t.turns), 26)
        self.assertEqual(t.length, 38 * 60)
        self.assertEqual(t.turns[0].speaker, "Host")
        self.assertTrue(t.render().startswith("[T1] Host (0:05):"))


class TestQuoteCheck(unittest.TestCase):
    def setUp(self):
        self.t = load_dir(DATA)["X"]

    def test_exact_and_ellipsis(self):
        self.assertTrue(quotecheck.found("Earlier we paid a freelancer for the tech packs", self.t))
        self.assertTrue(quotecheck.found("he knows every buyer personally ... why does he need a system", self.t))
        self.assertTrue(quotecheck.found("I don’t have those twenty years", self.t))

    def test_not_found(self):
        self.assertFalse(quotecheck.found("we never use email", self.t))
        # pieces out of order do not count
        self.assertFalse(quotecheck.found("why does he need a system ... he knows every buyer personally", self.t))


class TestAgreement(unittest.TestCase):
    def test_compare(self):
        a = {"fills": [{"transcript": "W", "cells": [{"id": "c1", "value": "yes"}, {"id": "c2", "value": "no"}]}]}
        b = {"fills": [{"transcript": "W", "cells": [{"id": "c1", "value": "yes"}, {"id": "c2", "value": "not_raised"}]}]}
        rows = agreement.compare(a, b)
        self.assertEqual(sum(r["agree"] for r in rows), 1)


class TestReplay(unittest.TestCase):
    def test_flags_until_covered(self):
        t = load_dir(DATA)["W"]
        marks = replay.checkpoints(t, 5)
        self.assertEqual(marks[-1], (t.length, t.turns[-1].n))
        # a cell first covered at turn 23 (32:40) stays empty at every checkpoint before 35:00
        seen, rows = replay.replay(t, ["ai_use"], marks, lambda cut, upto: {"ai_use": 23})
        empty_until = [r["time"] for r in rows if "ai_use" in r["still_empty"]]
        self.assertEqual(empty_until[-1], "30:00")
        self.assertEqual(seen["ai_use"], 23)


class TestCurate(unittest.TestCase):
    def setUp(self):
        ev = lambda t: [{"transcript": t, "turn": 1, "quote": "q", "prompted": False}]
        self.cells = {"cells": [{"id": i, "label": i, "definition": i, "evidence": ev(i)} for i in "abcd"]}

    def test_keep_merge_drop(self):
        d = {"keep": ["a"], "drop": ["d"],
             "merge": [{"into": {"id": "bc", "label": "bc", "definition": "bc"}, "from": ["b", "c"]}]}
        kept = curate.curate(self.cells, d)
        self.assertEqual([c["id"] for c in kept["cells"]], ["a", "bc"])
        self.assertEqual(len(kept["cells"][1]["evidence"]), 2)

    def test_every_proposal_needs_a_decision(self):
        with self.assertRaises(SystemExit):
            curate.curate(self.cells, {"keep": ["a", "b"], "drop": ["c"]})


if __name__ == "__main__":
    unittest.main()
