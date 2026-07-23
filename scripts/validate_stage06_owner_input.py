#!/usr/bin/env python3
"""Stage 06 Owner Input Validator"""
import sys, os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNER = os.path.join(ROOT, 'stages/stage-06-controlled-lab-deployment/owner-input-checklist.md')

def main():
    if not os.path.exists(OWNER):
        print(json.dumps({"result":"FAIL","reason":"missing"}))
        sys.exit(1)
    with open(OWNER) as f: c = f.read()
    items = ['Router type','VPS count','SSH usernames','Deployment approval','NOT production','No real users']
    found = sum(1 for i in items if i in c)
    all_ok = found >= 4
    print(json.dumps({"items":len(items),"found":found,"result":"PASS" if all_ok else "FAIL"}, indent=2))
    sys.exit(0 if all_ok else 1)

if __name__ == '__main__': main()
