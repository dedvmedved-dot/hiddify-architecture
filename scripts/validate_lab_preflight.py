#!/usr/bin/env python3
"""Stage 05 Preflight Validator"""
import sys, os, yaml, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check(label, ok):
    if ok: print(f"  PASS: {label}"); return True
    print(f"  FAIL: {label}"); return False

def main():
    inv_path = os.path.join(ROOT, 'automation/ansible/inventories/lab-example/hosts.yml')
    with open(inv_path) as f: inv = yaml.safe_load(f)
    results = []
    results.append(check("lab_environment=true", inv['all']['vars'].get('lab_environment') == True))
    results.append(check("production_environment=false", inv['all']['vars'].get('production_environment') == False))
    results.append(check("deployment_enabled=false", inv['all']['vars'].get('deployment_enabled') == False))
    results.append(check("remote_execution_enabled=false", inv['all']['vars'].get('remote_execution_enabled') == False))
    results.append(check("ansible_connection=local", inv['all']['vars'].get('ansible_connection') == 'local'))
    results.append(check("doc IPs only", all(any(ip.startswith(p) for p in ['192.0.2.','198.51.100.','203.0.113.']) for ip in [h['ansible_host'] for h in inv['all']['hosts'].values()])))
    print(f"Result: {sum(results)}/{len(results)} PASS")
    sys.exit(0 if all(results) else 1)

if __name__ == '__main__': main()
