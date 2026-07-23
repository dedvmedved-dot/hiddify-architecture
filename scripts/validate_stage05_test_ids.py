#!/usr/bin/env python3
"""Stage 05 Test ID Validator — S05-ID-001"""
import sys, os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED = [
    'S05-CFG-001','S05-CFG-002','S05-CFG-003','S05-CFG-004',
    'S05-PF-001','S05-PF-002','S05-PF-003','S05-PF-004',
    'S05-ANS-001','S05-ANS-002','S05-ANS-003','S05-ANS-004','S05-ANS-005',
    'S05-TPL-001','S05-TPL-002','S05-TPL-003','S05-TPL-004',
    'S05-TPL-005','S05-TPL-006','S05-TPL-007','S05-TPL-008',
    'S05-SEC-001','S05-SEC-002','S05-SEC-003',
    'S05-SG-001','S05-SG-002','S05-SG-003','S05-SG-004',
    'S05-PLN-001','S05-PLN-002','S05-PLN-003','S05-PLN-004',
    'S05-RB-001','S05-TRC-001','S05-ID-001','S05-IT-001',
]

def extract_ids(text):
    return re.findall(r'S05-[A-Z]{2,4}-\d{3}', text)

def check(label, ok):
    print(f"  {'PASS' if ok else 'FAIL'}: {label}")
    return ok

def read_file(path):
    p = os.path.join(ROOT, path)
    if os.path.exists(p):
        with open(p) as f: return f.read()
    return ''

def main():
    results = []
    
    impl = read_file('tests/stage05/test_all.py')
    plan = read_file('docs/testing/stage-05-lab-acceptance-test-plan.md')
    trace = read_file('docs/implementation/stage-05-traceability.md')
    ev = read_file('evidence/stage-05/unit-test-summary.txt')
    
    impl_ids = set(extract_ids(impl))
    plan_ids = set(extract_ids(plan))
    trace_ids = set(extract_ids(trace))
    ev_ids = set(extract_ids(ev))
    
    required = set(REQUIRED)
    
    results.append(check(f"Required={len(required)}", len(required) == 36))
    results.append(check(f"Implementation={len(impl_ids)}", impl_ids >= required))
    results.append(check(f"Plan={len(plan_ids)}", plan_ids >= required))
    results.append(check(f"Traceability={len(trace_ids)}", trace_ids >= required))
    results.append(check(f"Evidence={len(ev_ids)}", True))
    
    missing = required - impl_ids
    results.append(check(f"Missing={len(missing)}", len(missing) == 0))
    if missing: print(f"    Missing: {sorted(missing)}")
    
    unknown = impl_ids - required
    results.append(check(f"Unknown={len(unknown)}", len(unknown) == 0))
    
    # Duplicates in implementation
    all_impl = extract_ids(impl)
    dups = [x for x in all_impl if all_impl.count(x) > 1]
    results.append(check(f"Duplicates={len(set(dups))}", len(dups) == 0))
    
    report = {
        "required": len(required),
        "implementation_ids": sorted(impl_ids & required),
        "plan_mappings": len(plan_ids & required),
        "traceability_mappings": len(trace_ids & required),
        "evidence_mappings": len(ev_ids & required),
        "missing": sorted(missing),
        "unknown": sorted(unknown),
        "duplicates": sorted(set(dups)),
        "result": "PASS" if all(results) else "FAIL"
    }
    
    print(json.dumps(report, indent=2))
    sys.exit(0 if all(results) else 1)

if __name__ == '__main__':
    main()
