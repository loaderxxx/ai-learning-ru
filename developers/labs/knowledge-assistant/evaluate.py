"""Report baseline behavior on visible teaching cases; exit 0 is not a quality gate."""
import json
from pathlib import Path
from assistant import answer, load_documents, public_documents, validate_answer


def evaluate() -> dict:
    root = Path(__file__).resolve().parent
    cases = json.loads((root / "cases.json").read_text(encoding="utf-8"))
    docs = load_documents()
    allowed = {d["id"] for d in public_documents(docs)}
    results = []
    for case in cases:
        result = answer(case["query"], docs)
        validate_answer(result, allowed)
        status_ok = result["status"] == case["expected_status"]
        sources_ok = set(result["sources"]) == set(case["expected_sources"])
        results.append({"id": case["id"], "group": case["group"], "passed": status_ok and sources_ok,
                        "expected_status": case["expected_status"], "actual_status": result["status"],
                        "expected_sources": case["expected_sources"], "actual_sources": result["sources"]})
    groups = {}
    for row in results:
        group = groups.setdefault(row["group"], {"passed": 0, "total": 0})
        group["total"] += 1
        group["passed"] += int(row["passed"])
    return {"mode": "offline-extractive-baseline", "model_calls": 0,
            "note": "Visible fixture checks of status and source IDs, NOT semantic/LLM evaluation.",
            "passed": sum(row["passed"] for row in results), "total": len(results),
            "groups": groups, "results": results}


if __name__ == "__main__":
    print(json.dumps(evaluate(), ensure_ascii=False, indent=2))
