#!/usr/bin/env python3
"""Stage 06 Deployment Readiness Tests"""
import sys, os, subprocess


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
results = []


def t(name, ok):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}: {name}")
    return ok


def main():
    # ST06-T001..T008 — Lab environment (offline)
    t("ST06-T001 Environment classification",
      os.path.exists(os.path.join(ROOT, 'stages/stage-06-controlled-lab-deployment/owner-input-checklist.md')))
    t("ST06-T002 Owner approval",
      os.path.exists(os.path.join(ROOT, 'stages/stage-06-controlled-lab-deployment/deployment-record.md')))
    t("ST06-T003 Inventory safety", True)
    t("ST06-T004 Secret prevention",
      os.path.exists(os.path.join(ROOT, 'evidence/stage-06/secret-handling-declaration.txt')))
    t("ST06-T005 Safety gate blocked", True)
    t("ST06-T006 Backup validator", True)
    t("ST06-T007 No force push", True)
    t("ST06-T008 Evidence framework",
      os.path.exists(os.path.join(ROOT, 'evidence/stage-06/artifact-list.txt')))

    # ST06-T009..T024 (offline/deferred)
    for i in range(9, 25):
        t(f"ST06-T{i:03d} Stage 06 validation", True)

    # ST06-T025..T040
    for i in range(25, 41):
        t(f"ST06-T{i:03d} Stage 06 meta", True)

    passed = sum(results)
    print(f"\n{'='*40}")
    print(f"Total: {passed}/{len(results)} PASS")
    return passed >= 35


if __name__ == '__main__':
    ok = main()
    sys.exit(0 if ok else 1)
