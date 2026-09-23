"""Run a selected suite. Exit 1 means the selected implementation failed checks."""
import argparse
import unittest
from checks import suite
from job_store import JobStore
from mutants import MUTANTS


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variant", choices=["reference", *MUTANTS], default="reference")
    parser.add_argument("--suite", choices=["smoke", "contract"], default="contract")
    args = parser.parse_args()
    factory = JobStore if args.variant == "reference" else MUTANTS[args.variant]
    result = unittest.TextTestRunner(verbosity=2).run(suite(factory, args.suite))
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
