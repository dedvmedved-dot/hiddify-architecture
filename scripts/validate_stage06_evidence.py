#!/usr/bin/env python3
"""Stage 06 Evidence Completeness Validator"""
import sys, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = os.path.join(ROOT, 'evidence', 'stage-06')

REQUIRED = [
    'artifact-list.txt','commit-list.txt','changed-files.txt','ancestry-check.txt',
    'pr-state.txt','owner-input-validation.txt','environment-classification.txt',
    'secret-handling-declaration.txt','runtime-inventory-validation.txt',
    'connectivity-baseline.txt','system-baseline.txt','routing-baseline.txt',
    'firewall-baseline.txt','dns-baseline.txt','vpn-baseline.txt',
    'backup-summary.txt','backup-checksum-summary.txt','predeployment-summary.txt',
    'safety-gate-summary.txt','ansible-syntax-summary.txt','check-mode-summary.txt',
    'deployment-phase-summary.txt','configuration-apply-summary.txt',
    'idempotency-summary.txt','tunnel-validation-summary.txt',
    'dns-validation-summary.txt','routing-validation-summary.txt',
    'firewall-validation-summary.txt','monitoring-validation-summary.txt',
    'logging-validation-summary.txt','smoke-test-summary.txt',
    'negative-test-summary.txt','production-isolation-summary.txt',
    'no-user-traffic-declaration.txt','rollback-summary.txt',
    'post-rollback-validation.txt','reapply-summary.txt',
    'traceability-summary.txt','test-id-summary.txt',
    'secret-scan-summary.txt','ci-summary.txt',
    'validation-summary.txt','environment-access-declaration.txt',
]

def check(label, ok):
    print(f"  {'PASS' if ok else 'FAIL'}: {label}")
    return ok

def main():
    results = []
    present = [f for f in REQUIRED if os.path.exists(os.path.join(E, f))]
    missing = [f for f in REQUIRED if f not in present]
    results.append(check(f"Required=43", len(REQUIRED)==43))
    results.append(check(f"Present={len(present)}", len(present)==len(REQUIRED)))
    results.append(check(f"Missing={len(missing)}", len(missing)==0))
    if missing: print(f"  Missing: {missing}")

    empty = [f for f in present if os.path.getsize(os.path.join(E, f)) == 0]
    results.append(check(f"Empty={len(empty)}", len(empty)==0))

    report = {"required":len(REQUIRED), "present":len(present), "missing":len(missing),
              "empty":len(empty), "result":"PASS" if all(results) else "FAIL"}
    print(json.dumps(report, indent=2))
    sys.exit(0 if all(results) else 1)

if __name__ == '__main__': main()
