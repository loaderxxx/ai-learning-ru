"""Six deliberately defective teaching variants, not generated or production code."""
from copy import deepcopy
from job_store import JobStore


class AcceptsBlankTitle(JobStore):
    def _normalize(self, payload):
        if type(payload) is not dict:
            return super()._normalize(payload)
        payload = dict(payload)
        if isinstance(payload.get("title"), str) and not payload["title"].strip():
            payload["title"] = "untitled"
        return super()._normalize(payload)


class AcceptsBooleanPriority(JobStore):
    def _normalize(self, payload):
        if type(payload) is not dict:
            return super()._normalize(payload)
        payload = dict(payload)
        if type(payload.get("priority")) is bool:
            payload["priority"] = int(payload["priority"])
        return super()._normalize(payload)


class DuplicatesRetry(JobStore):
    def submit(self, payload):
        job = self._normalize(payload)
        self._jobs.append(job)
        return deepcopy(job)


class OverwritesConflict(JobStore):
    def submit(self, payload):
        job = self._normalize(payload)
        existing = next((x for x in self._jobs if x["id"] == job["id"]), None)
        if existing is not None:
            existing.update(job)
            return deepcopy(existing)
        return super().submit(payload)


class PartialBatchWrite(JobStore):
    def submit_batch(self, payloads):
        if type(payloads) is not list or len(payloads) > 50:
            raise ValueError("invalid batch")
        return [self.submit(payload) for payload in payloads]


class LeaksMutableSnapshot(JobStore):
    def list_jobs(self):
        return sorted(self._jobs, key=lambda job: job["id"])


MUTANTS = {
    "blank_title": AcceptsBlankTitle,
    "boolean_priority": AcceptsBooleanPriority,
    "duplicate_retry": DuplicatesRetry,
    "overwrite_conflict": OverwritesConflict,
    "partial_batch": PartialBatchWrite,
    "mutable_snapshot": LeaksMutableSnapshot,
}
