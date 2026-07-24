#!/usr/bin/env python3
"""Stage 05 Evidence Completeness Validator"""
import sys, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = os.path.join(ROOT, 'evidence', 'stage-05')

REQUIRED = [
    'artifact-list.txt', 'commit-list.txt', 'changed-files.txt',
    'ancestry-check.txt', 'validation-summary.txt', 'ci-summary.txt',
    'configuration-validation-summary.txt', 'inventory-validation-summary.txt',
    'preflight-summary.txt', 'ansible-syntax-summary.txt',
    'check-mode-summary.txt', 'template-rendering-summary.txt',
    'deployment-plan-summary.txt', 'rollback-validation-summary.txt',
    'unit-test-summary.txt', 'integration-simulation-summary.txt',
    'safety-guard-summary.txt', 'secret-scan-summary.txt',
    'traceability-summary.txt', 'test-id-summary.txt',
    'environment-access-declaration.txt',
]

FORBIDDEN_PLACEHOLDERS = ['TBD', 'TODO', '<ID>', '<SHA>', '<COUNT>', 'UNKNOWN', 'NOT RECORDED']

def check(label, ok):
    print(f"  {'PASS' if ok else 'FAIL'}: {label}")
    return ok

def main():
    results = []
    present = [f for f in REQUIRED if os.path.exists(os.path.join(E, f))]
    missing = [f for f in REQUIRED if f not in present]

    results.append(check(f"Required={len(REQUIRED)}", len(REQUIRED)==21))
    results.append(check(f"Present={len(present)}", len(present)==21))
    results.append(check(f"Missing={len(missing)}", len(missing)==0))
    if missing: print(f"    Missing: {missing}")

    empty = []
    invalid = []
    placeholder_findings = []

    for fname in present:
        path = os.path.join(E, fname)
        size = os.path.getsize(path)
        if size == 0:
            empty.append(fname)
            continue

        with open(path) as f:
            content = f.read()

        # Check for HEAD SHA
        if fname != 'ci-summary.txt':  # ci-summary gets populated after CI
            has_head = bool(re.search(r'[0-9a-f]{40}', content))
            if not has_head:
                invalid.append(f"{fname}: missing full HEAD SHA")

        # Check for placeholders
        for ph in FORBIDDEN_PLACEHOLDERS:
            if ph in content:
                placeholder_findings.append(f"{fname}: contains '{ph}'")

        # Check access declaration
        if fname == 'environment-access-declaration.txt':
            if '***' in content:
                invalid.append(f"{fname}: contains '***'")
            if 'Secrets used: NO' not in content:
                invalid.append(f"{fname}: secrets declaration not NO")

    results.append(check(f"Empty={len(empty)}", len(empty)==0))
    results.append(check(f"Invalid={len(invalid)}", len(invalid)==0))
    results.append(check(f"Placeholders={len(placeholder_findings)}", len(placeholder_findings)==0))

    if empty: print(f"    Empty: {empty}")
    if invalid: print(f"    Invalid: {invalid}")
    if placeholder_findings: print(f"    Placeholders: {placeholder_findings}")

    report = {"required":21, "present":len(present), "missing":len(missing),
              "empty":len(empty), "invalid":len(invalid),
              "placeholders":len(placeholder_findings),
              "result": "PASS" if all(results) else "FAIL"}

    import json
    print(json.dumps(report, indent=2))
    sys.exit(0 if all(results) else 1)

if __name__ == '__main__':
    main()
