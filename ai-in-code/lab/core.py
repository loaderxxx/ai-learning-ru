"""Offline teaching lab: scripted models, bounded tools, no network or writes.

Not a live LLM adapter, production authorization layer, or durable workflow.
Python 3.11+, standard library only.
"""
from __future__ import annotations

import copy
import json
import re
from typing import Any, Protocol


class LabError(Exception):
    """Controlled failure identified by a safe, non-sensitive code."""


class TransientError(LabError):
    """A scripted temporary provider failure; eligible for bounded fallback."""


class AccessError(LabError):
    """A denied operation; never use fallback to bypass it."""


class ContractError(LabError):
    """Input or response violates the small teaching contract."""


class Model(Protocol):
    name: str

    def reply(self, history: list[dict[str, Any]]) -> dict[str, Any]: ...


class ScriptedModel:
    """Returns predefined messages. It does not call an AI provider."""

    def __init__(self, name: str, script: list[Any]) -> None:
        self.name = name
        self.script = copy.deepcopy(script)
        self.calls = 0

    def reply(self, history: list[dict[str, Any]]) -> dict[str, Any]:
        self.calls += 1
        if not self.script:
            raise ContractError("script_exhausted")
        message = self.script.pop(0)
        if isinstance(message, Exception):
            raise message
        return copy.deepcopy(message)


RECORDS = {
    "alpha-hours": {"tenant": "alpha", "text": "Open 10:00-18:00. Synthetic."},
    "beta-hours": {"tenant": "beta", "text": "Open 12:00-17:00. Synthetic."},
}
TOOLS = {"calculate_total", "lookup_record"}


def safe_id(value: Any) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9_-]{1,64}", value) is not None


def fields(value: Any, expected: set[str]) -> None:
    if not isinstance(value, dict) or set(value) != expected:
        raise ContractError("fields")


def dispatch(name: str, args: Any, tenant: str) -> dict[str, Any]:
    """Allowlisted read-only/pure tools. Tenant is trusted application context."""
    if name == "calculate_total":
        fields(args, {"unit_cents", "quantity"})
        price, quantity = args["unit_cents"], args["quantity"]
        if type(price) is not int or type(quantity) is not int:
            raise ContractError("numeric_type")
        if not 0 <= price <= 1_000_000 or not 1 <= quantity <= 1000:
            raise ContractError("numeric_range")
        return {"total_cents": price * quantity}
    if name == "lookup_record":
        fields(args, {"record_id"})
        if not safe_id(args["record_id"]):
            raise ContractError("record_id")
        record = RECORDS.get(args["record_id"])
        # Identical external response for missing and unauthorized records.
        if record is None or record["tenant"] != tenant:
            raise AccessError("record_unavailable")
        return {"record_id": args["record_id"], "text": record["text"]}
    raise AccessError("tool_not_allowed")


def run(text: str, tenant: str, models: list[Model], *, request_id: str = "demo-01",
        max_steps: int = 4, max_calls: int = 6) -> dict[str, Any]:
    """Bounded synchronous mock loop. No network timeout enforcement is implemented.

    Fallback applies only to TransientError and only to supplied eligible models.
    Call-ID deduplication lasts for this run only, not across process restarts.
    """
    events: list[dict[str, Any]] = []
    results: list[dict[str, Any]] = []
    attempts = 0
    active = 0

    def event(kind: str, **safe_metadata: Any) -> None:
        events.append({"request_id": request_id, "event": kind, **safe_metadata})

    def finish(status: str, error: str | None = None, answer: str | None = None) -> dict[str, Any]:
        event("request_finished", status=status)
        candidate = getattr(models[active], "name", None) if isinstance(models, list) and active < len(models) else None
        return {"mode": "mock", "status": status, "answer": answer, "error": error,
                "model": candidate if safe_id(candidate) else None,
                "attempts": attempts, "tool_results": results, "events": events}

    if not safe_id(request_id):
        request_id = "invalid-id"
        return finish("invalid_input", "request_id")
    if not isinstance(text, str) or not text.strip() or len(text) > 2000:
        return finish("invalid_input", "text")
    if not safe_id(tenant):
        return finish("invalid_input", "tenant")
    if (not isinstance(models, list) or not models or len(models) > 4 or
            any(not safe_id(getattr(model, "name", None)) for model in models)):
        # Do not put invalid model metadata in output or logs.
        models = []
        return finish("invalid_input", "models")
    if type(max_steps) is not int or type(max_calls) is not int or not 1 <= max_steps <= 20 or not 1 <= max_calls <= 40:
        return finish("invalid_input", "limits")

    event("request_started")
    history: list[dict[str, Any]] = [{"role": "user", "text": text}]
    seen: dict[str, tuple[str, dict[str, Any]]] = {}
    for _ in range(max_steps):
        while True:
            if attempts >= max_calls:
                return finish("technical_error", "call_limit")
            attempts += 1
            event("model_started", model=models[active].name)
            try:
                message = models[active].reply(copy.deepcopy(history))
                break
            except TransientError:
                event("model_failed", model=models[active].name, error="transient")
                if active + 1 >= len(models):
                    return finish("technical_error", "provider_unavailable")
                active += 1
                event("fallback", model=models[active].name)
            except AccessError:
                return finish("denied", "provider_denied")
            except ContractError:
                return finish("technical_error", "model_contract")
            except Exception:
                # A safe outer boundary; unexpected exceptions are NOT retried.
                return finish("technical_error", "unexpected_model_error")
        try:
            if not isinstance(message, dict):
                raise ContractError("message")
            if message.get("type") == "final":
                fields(message, {"type", "text"})
                if not isinstance(message["text"], str) or not 1 <= len(message["text"]) <= 2000:
                    raise ContractError("final_text")
                return finish("answered", answer=message["text"])
            fields(message, {"type", "id", "name", "args"})
            if message["type"] != "tool" or not safe_id(message["id"]):
                raise ContractError("tool_message")
            name = message["name"]
            if not isinstance(name, str) or name not in TOOLS:
                raise AccessError("tool_not_allowed")
            if not isinstance(message["args"], dict):
                raise ContractError("arguments")
            fingerprint = json.dumps({"name": name, "args": message["args"]},
                                     sort_keys=True, allow_nan=False)
            event("tool_requested", tool=name, call_id=message["id"])
            if message["id"] in seen:
                old_fingerprint, result = seen[message["id"]]
                if fingerprint != old_fingerprint:
                    raise ContractError("call_id_conflict")
                event("tool_reused", tool=name, call_id=message["id"])
            else:
                result = dispatch(name, message["args"], tenant)
                seen[message["id"]] = (fingerprint, copy.deepcopy(result))
                results.append({"call_id": message["id"], "result": copy.deepcopy(result)})
                event("tool_completed", tool=name, call_id=message["id"])
            history.append(copy.deepcopy(message))
            history.append({"type": "tool_result", "id": message["id"], "result": copy.deepcopy(result)})
        except AccessError:
            return finish("denied", "tool_denied")
        except (ContractError, TypeError, ValueError):
            return finish("technical_error", "response_contract")
    return finish("technical_error", "step_limit")


if __name__ == "__main__":
    primary = ScriptedModel("mock-primary", [TransientError("synthetic")])
    backup = ScriptedModel("mock-backup", [
        {"type": "tool", "id": "call-1", "name": "calculate_total",
         "args": {"unit_cents": 250, "quantity": 4}},
        {"type": "final", "text": "Scripted example: four sessions cost 1000 cents."},
    ])
    print(json.dumps(run("Calculate four sessions.", "alpha", [primary, backup]), indent=2))
