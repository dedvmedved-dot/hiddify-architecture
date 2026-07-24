#!/usr/bin/env python3
"""Stage 06 Test ID Validator"""
import sys, os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = set(f'ST06-T{i:03d}' for i in range(1,41))
def main():
    plan = os.path.join(ROOT, 'docs/testing/stage-06-test-plan.md')
    ids = set()
    if os.path.exists(plan):
        with open(plan) as f: ids = set(re.findall(r'ST06-T\d{3}', f.read()))
    missing = REQUIRED - ids
    ok = len(ids) >= 40 and len(missing) == 0
    print(json.dumps({"required":len(REQUIRED),"plan":len(ids),"missing":sorted(missing),"result":"PASS" if ok else "FAIL"}, indent=2))
    sys.exit(0 if ok else 1)
if __name__ == '__main__': main()
