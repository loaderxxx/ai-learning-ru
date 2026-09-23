"""Tests derived from SPEC.md. Factory injection runs the same checks on each variant."""
import unittest
from job_store import JobStore, ConflictError


def job(ident="a", title="Example", priority=1):
    return {"id": ident, "title": title, "priority": priority}


class SmokeChecks(unittest.TestCase):
    factory = JobStore

    def setUp(self):
        self.store = self.factory()

    def test_one_job(self):
        self.assertEqual(self.store.submit(job()), job())

    def test_two_different_jobs(self):
        self.store.submit(job("a"))
        self.store.submit(job("b"))
        self.assertEqual(len(self.store.list_jobs()), 2)


class ContractChecks(SmokeChecks):
    def test_title_is_trimmed(self):
        self.assertEqual(self.store.submit(job(title="  Задача  "))["title"], "Задача")

    def test_retry_is_idempotent(self):
        self.store.submit(job())
        self.store.submit(job())
        self.assertEqual(self.store.list_jobs(), [job()])

    def test_normalized_retry_is_same_job(self):
        self.store.submit(job(title=" Example "))
        self.store.submit(job())
        self.assertEqual(self.store.list_jobs(), [job()])

    def test_conflict_preserves_existing(self):
        self.store.submit(job())
        with self.assertRaises(ConflictError):
            self.store.submit(job(title="Changed"))
        self.assertEqual(self.store.list_jobs(), [job()])

    def test_invalid_id(self):
        for ident in ["", "UPPER", "a/b", "a b", "x" * 41, 12, None]:
            with self.subTest(ident=ident), self.assertRaises(ValueError):
                self.store.submit(job(ident=ident))

    def test_invalid_title(self):
        for title in ["", "  ", "x" * 121, 7, None]:
            with self.subTest(title=title), self.assertRaises(ValueError):
                self.store.submit(job(title=title))

    def test_priority_boundaries(self):
        for priority in [0, 3]:
            self.store.submit(job(ident=str(priority), priority=priority))
        for priority in [-1, 4, 1.0, True, False, "1", None]:
            with self.subTest(priority=priority), self.assertRaises(ValueError):
                self.store.submit(job(ident="bad", priority=priority))

    def test_exact_fields(self):
        for payload in [{"id": "a"}, {**job(), "admin": True}, [], None]:
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                self.store.submit(payload)

    def test_batch_success_and_empty(self):
        self.assertEqual(self.store.submit_batch([]), [])
        self.assertEqual(self.store.submit_batch([job("a"), job("b")]), [job("a"), job("b")])

    def test_invalid_batch_rolls_back(self):
        self.store.submit(job("old"))
        with self.assertRaises(ValueError):
            self.store.submit_batch([job("new"), job("bad", priority=4)])
        self.assertEqual(self.store.list_jobs(), [job("old")])

    def test_conflicting_batch_rolls_back(self):
        with self.assertRaises(ConflictError):
            self.store.submit_batch([job("a"), job("b"), job("a", title="Conflict")])
        self.assertEqual(self.store.list_jobs(), [])

    def test_batch_shape_and_limit(self):
        for payload in [None, {}, tuple(), [job()] * 51]:
            with self.subTest(payload_type=type(payload).__name__), self.assertRaises(ValueError):
                self.store.submit_batch(payload)
        self.assertEqual(self.store.list_jobs(), [])

    def test_result_is_detached(self):
        payload = job()
        result = self.store.submit(payload)
        payload["title"] = "external input changed"
        result["title"] = "external result changed"
        self.assertEqual(self.store.list_jobs(), [job()])

    def test_snapshot_is_detached(self):
        self.store.submit(job())
        self.store.list_jobs()[0]["title"] = "external snapshot changed"
        self.assertEqual(self.store.list_jobs(), [job()])

    def test_stable_order(self):
        self.store.submit(job("z"))
        self.store.submit(job("a"))
        self.assertEqual([x["id"] for x in self.store.list_jobs()], ["a", "z"])


def suite(factory=JobStore, level="contract"):
    base = {"smoke": SmokeChecks, "contract": ContractChecks}[level]
    selected = type("SelectedChecks", (base,), {"factory": factory})
    return unittest.defaultTestLoader.loadTestsFromTestCase(selected)
