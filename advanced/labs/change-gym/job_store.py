"""Synthetic in-memory job registry. No network, persistence or concurrency guarantee."""
from copy import deepcopy
import re


class ConflictError(ValueError):
    pass


class JobStore:
    def __init__(self):
        self._jobs = []

    def _normalize(self, payload):
        if type(payload) is not dict or set(payload) != {"id", "title", "priority"}:
            raise ValueError("expected exactly id, title and priority")
        ident, title, priority = payload["id"], payload["title"], payload["priority"]
        if not isinstance(ident, str) or re.fullmatch(r"[a-z0-9_-]{1,40}", ident) is None:
            raise ValueError("invalid id")
        if not isinstance(title, str) or not 1 <= len(title.strip()) <= 120:
            raise ValueError("invalid title")
        if type(priority) is not int or not 0 <= priority <= 3:
            raise ValueError("priority must be an integer from 0 to 3")
        return {"id": ident, "title": title.strip(), "priority": priority}

    def submit(self, payload):
        job = self._normalize(payload)
        existing = next((x for x in self._jobs if x["id"] == job["id"]), None)
        if existing is not None:
            if existing != job:
                raise ConflictError("same id with different normalized content")
            return deepcopy(existing)
        self._jobs.append(job)
        return deepcopy(job)

    def submit_batch(self, payloads):
        if type(payloads) is not list or len(payloads) > 50:
            raise ValueError("batch must be a list with at most 50 items")
        staged = type(self)()
        staged._jobs = deepcopy(self._jobs)
        result = [staged.submit(payload) for payload in payloads]
        self._jobs = staged._jobs
        return result

    def list_jobs(self):
        return deepcopy(sorted(self._jobs, key=lambda job: job["id"]))
