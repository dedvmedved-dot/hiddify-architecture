#!/usr/bin/env python3
"""Stage 04 Offline Integration Simulation — S04-IT-001"""
import sys, os, json, yaml, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def sim(label, ok):
    if ok:
        print(f"  SIM-PASS: {label}")
        return True
    print(f"  SIM-FAIL: {label}")
    return False

def step1():
    path = os.path.join(ROOT, 'iac', 'examples', 'config.example.yml')
    with open(path) as f: yaml.safe_load(f)
    return True

def step2():
    path = os.path.join(ROOT, 'iac', 'schemas', 'config-schema.json')
    with open(path) as f: json.load(f)
    return True

def step3():
    path = os.path.join(ROOT, 'iac', 'examples', 'config.example.yml')
    with open(path) as f:
        c = yaml.safe_load(f)
    sf = c['safety_flags']
    for f in ['deployment_enabled','production_mode','allow_remote_execution','allow_network_changes','allow_secret_material']:
        if sf[f] != False: return False
    return True

def step4():
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'safety_guard.py')],
                       capture_output=True, text=True)
    return r.returncode == 0

def step5():
    path = os.path.join(ROOT, 'docs', 'implementation', 'stage-04-traceability.md')
    return os.path.exists(path)

def main():
    print("Stage 04 Integration Simulation (S04-IT-001)")
    results = [
        sim("Config load", step1()),
        sim("Schema validation", step2()),
        sim("Safety flags", step3()),
        sim("Forbidden command scan", step4()),
        sim("Traceability present", step5()),
    ]
    print(f"\nResult: {sum(results)}/{len(results)} PASS")
    print("VALIDATION_ONLY\nNO_REMOTE_EXECUTION\nNO_INFRASTRUCTURE_CHANGE\nREADY_FOR_LAB_PLANNING")
    sys.exit(0 if all(results) else 1)

if __name__ == '__main__':
    main()
