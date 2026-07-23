#!/usr/bin/env python3
"""Stage 05 Traceability Validator — S05-TRC-001"""
import sys, os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    path = os.path.join(ROOT, 'docs/implementation/stage-05-traceability.md')
    if not os.path.exists(path):
        print("FAIL: traceability not found")
        sys.exit(1)
    
    with open(path) as f:
        content = f.read()
    
    results = []
    
    # Check required columns in table header
    required_cols = ['Req ID', 'Arch Doc', 'ADR', 'Stage 04', 'Stage 05', 'Test ID', 'Status']
    for col in required_cols:
        results.append(check(f"Column '{col}'", col.lower() in content.lower()))
    
    # Check requirements referenced
    reqs = re.findall(r'(FR|NFR|SEC|RTE|DNS|OPS|CON|ASM)-\d{3}', content)
    results.append(check(f"Requirement refs={len(reqs)}", len(reqs) >= 3))
    
    # Check ADR references
    adrs = re.findall(r'ADR-\d{3}', content)
    results.append(check(f"ADR refs={len(adrs)}", len(adrs) >= 2))
    
    # Check Test IDs
    test_ids = re.findall(r'S05-[A-Z]{2,4}-\d{3}', content)
    results.append(check(f"Test ID refs={len(test_ids)}", len(test_ids) >= 10))
    
    # Check statuses
    statuses = re.findall(r'(LAB_PACKAGE_READY|PLAN_ONLY|VALIDATED_OFFLINE|DEFERRED|GAP|BLOCKED|NOT APPLICABLE)', content)
    results.append(check(f"Valid statuses={len(statuses)}", len(statuses) >= 1))
    
    report = {"columns_found": sum(r for r in results[:7]), "requirement_refs": len(reqs),
              "adr_refs": len(adrs), "test_id_refs": len(test_ids), "statuses": len(statuses),
              "result": "PASS" if all(results) else "FAIL"}
    
    print(json.dumps(report, indent=2))
    sys.exit(0 if all(results) else 1)

def check(label, ok):
    print(f"  {'PASS' if ok else 'FAIL'}: {label}")
    return ok

if __name__ == '__main__':
    main()
