"""A fixed, hand-written mutation demonstration, not a general mutation engine."""
import io
import json
import unittest
from checks import suite
from job_store import JobStore
from mutants import MUTANTS


def measure(factory, level):
    result = unittest.TextTestRunner(stream=io.StringIO()).run(suite(factory, level))
    return {"tests": result.testsRun, "successful": result.wasSuccessful(),
            "failures": len(result.failures), "errors": len(result.errors)}


def main():
    rows = [{"variant": name, "smoke": measure(factory, "smoke"),
             "contract": measure(factory, "contract")}
            for name, factory in [("reference", JobStore), *MUTANTS.items()]]
    mutants = rows[1:]
    report = {"kind": "fixed synthetic mutation exercise", "model_calls": 0,
              "mutants": len(mutants),
              "smoke_detected": sum(not x["smoke"]["successful"] for x in mutants),
              "contract_detected": sum(not x["contract"]["successful"] for x in mutants),
              "reference_passed": rows[0]["contract"]["successful"], "results": rows}
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["reference_passed"] else 1)


if __name__ == "__main__":
    main()
