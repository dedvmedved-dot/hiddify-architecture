#!/usr/bin/env python3
"""Stage 06 Traceability Validator"""
import sys, os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def main():
    path = os.path.join(ROOT, 'docs/implementation/stage-06-traceability.md')
    if not os.path.exists(path):
        print("FAIL: file not found")
        sys.exit(1)
    with open(path) as f: content = f.read()
    for col in ['Req ID','Source','Artifact','Test ID','Evidence','Status']:
        if col not in content:
            print(f"FAIL: missing column {col}")
            sys.exit(1)
    reqs = len(re.findall(r'ST06-REQ-', content))
    tests = len(re.findall(r'ST06-T', content))
    ok = reqs >= 10 and tests >= 10
    print(json.dumps({"columns":"PASS","reqs":reqs,"tests":tests,"result":"PASS" if ok else "FAIL"}, indent=2))
    sys.exit(0 if ok else 1)
if __name__ == '__main__': main()
