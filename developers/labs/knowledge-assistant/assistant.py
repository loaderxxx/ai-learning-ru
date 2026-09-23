"""Offline teaching baseline. No LLM, network, shell execution or external packages."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from typing import Any

ROOT = Path(__file__).resolve().parent
STOP = {"как", "что", "где", "и", "в", "на", "для", "с", "по", "ли", "можно", "мне"}


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[\w]+", text.casefold())) - STOP


def check_query(query: Any) -> str:
    if not isinstance(query, str) or not query.strip() or len(query) > 500:
        raise ValueError("query must be a nonempty string, at most 500 characters")
    return query.strip()


def load_documents() -> list[dict[str, Any]]:
    return json.loads((ROOT / "documents.json").read_text(encoding="utf-8"))


def public_documents(documents: list[dict[str, Any]]) -> list[dict[str, Any]]:
    # Teaching policy: metadata is assigned by the trusted corpus maintainer.
    # A real multi-user system must derive access from authenticated identity.
    return [d for d in documents if d.get("visibility") == "public" and d.get("active") is True]


def search_docs(query: str, documents: list[dict[str, Any]], limit: int = 3) -> list[dict[str, Any]]:
    query = check_query(query)
    if type(limit) is not int or not 1 <= limit <= 5:
        raise ValueError("limit must be an integer from 1 to 5")
    terms = tokens(query)
    if not terms:
        return []
    scored = []
    for doc in public_documents(documents):
        vocabulary = tokens(doc["title"] + " " + doc["text"] + " " + " ".join(doc.get("tags", [])))
        score = len(terms & vocabulary) / len(terms)
        if score >= 0.5:
            scored.append({"id": doc["id"], "text": doc["text"], "score": round(score, 4)})
    return sorted(scored, key=lambda row: (-row["score"], row["id"]))[:limit]


def answer(query: str, documents: list[dict[str, Any]]) -> dict[str, Any]:
    hits = search_docs(query, documents, limit=1)
    if not hits:
        return {"status": "not_found", "answer": "В учебной базе не найдено достаточного основания.", "sources": []}
    # Exact extraction, NOT model generation or a guarantee of relevance.
    return {"status": "answered", "answer": hits[0]["text"], "sources": [hits[0]["id"]]}


def validate_answer(payload: Any, allowed_ids: set[str]) -> None:
    """Small explicit contract validator, not a general JSON Schema implementation."""
    if not isinstance(payload, dict) or set(payload) != {"status", "answer", "sources"}:
        raise ValueError("wrong fields")
    if payload["status"] not in ("answered", "not_found"):
        raise ValueError("wrong status")
    if not isinstance(payload["answer"], str) or not 1 <= len(payload["answer"]) <= 4000:
        raise ValueError("wrong answer text")
    ids = payload["sources"]
    if not isinstance(ids, list) or any(not isinstance(x, str) for x in ids):
        raise ValueError("sources must be a list of strings")
    if len(ids) > 5 or len(ids) != len(set(ids)) or not set(ids) <= allowed_ids:
        raise ValueError("invalid source IDs")
    if payload["status"] == "answered" and not ids:
        raise ValueError("answered requires a source")
    if payload["status"] == "not_found" and ids:
        raise ValueError("not_found must have no sources")


class ToolSession:
    """Read-only allowlist with an explicit invocation budget for a single request."""
    def __init__(self, documents: list[dict[str, Any]], max_calls: int = 2):
        if type(max_calls) is not int or not 1 <= max_calls <= 10:
            raise ValueError("invalid max_calls")
        self.documents = documents
        self.max_calls = max_calls
        self.calls = 0

    def call(self, name: str, arguments: Any) -> Any:
        if self.calls >= self.max_calls:
            raise RuntimeError("tool budget exhausted")
        self.calls += 1  # Invalid attempts also consume the budget.
        if not isinstance(arguments, dict):
            raise ValueError("arguments must be an object")
        if name == "search_docs":
            if set(arguments) != {"query"}:
                raise ValueError("search_docs accepts only query")
            return search_docs(arguments["query"], self.documents)
        if name == "get_doc":
            if set(arguments) != {"id"} or not isinstance(arguments["id"], str):
                raise ValueError("get_doc accepts only a string id")
            # IDs are looked up; they are never interpreted as filesystem paths.
            matches = [d for d in public_documents(self.documents) if d["id"] == arguments["id"]]
            return {"found": False} if not matches else {"found": True, "id": matches[0]["id"], "text": matches[0]["text"]}
        raise ValueError("unknown tool")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    args = parser.parse_args()
    docs = load_documents()
    try:
        result = answer(args.query, docs)
        validate_answer(result, {d["id"] for d in public_documents(docs)})
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
