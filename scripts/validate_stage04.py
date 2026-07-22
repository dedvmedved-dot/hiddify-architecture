#!/usr/bin/env python3
"""Stage 04 Offline Validation CLI."""
import sys, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check(label, ok):
    if ok:
        print(f"  PASS: {label}")
        return True
    print(f"  FAIL: {label}", file=sys.stderr)
    return False

def validate_config():
    import json, yaml
    with open(os.path.join(ROOT, 'iac/schemas/config-schema.json')) as f:
        json.load(f)
    with open(os.path.join(ROOT, 'iac/examples/config.example.yml')) as f:
        config = yaml.safe_load(f)
    sf = config.get('safety_flags', {})
    for flag in ['deployment_enabled', 'production_mode', 'allow_remote_execution', 'allow_network_changes', 'allow_secret_material']:
        if sf.get(flag) != False:
            raise ValueError(f"{flag} must be false")
    if config.get('deployment_mode') != 'offline-skeleton':
        raise ValueError("deployment_mode must be offline-skeleton")
    return True

def validate_placeholders():
    with open(os.path.join(ROOT, 'iac/examples/config.example.yml')) as f:
        content = f.read()
    if 'CHANGE_ME' not in content:
        raise ValueError("Must use CHANGE_ME placeholder")
    return True

def validate_structure():
    for d in ['iac', 'automation', 'scripts', 'tests/stage04']:
        if not os.path.isdir(os.path.join(ROOT, d)):
            raise FileNotFoundError(f"Missing: {d}")
    return True

def run_unit_tests():
    result = subprocess.run(
        [sys.executable, os.path.join(ROOT, 'tests', 'stage04', 'test_config.py')],
        capture_output=True, text=True, cwd=ROOT
    )
    print(result.stdout.strip())
    return result.returncode == 0

def main():
    print("Stage 04 Offline Validation")
    results = []
    try:
        validate_config()
        results.append(True)
        print("  PASS: Config schema validation")
    except Exception as e:
        print(f"  FAIL: Config schema validation — {e}")
        results.append(False)
    try:
        validate_placeholders()
        results.append(True)
        print("  PASS: Placeholder validation")
    except Exception as e:
        print(f"  FAIL: Placeholder validation — {e}")
        results.append(False)
    try:
        validate_structure()
        results.append(True)
        print("  PASS: Directory structure")
    except Exception as e:
        print(f"  FAIL: Directory structure — {e}")
        results.append(False)
    results.append(run_unit_tests())
    
    passed = sum(results)
    total = len(results)
    print(f"Result: {passed}/{total} PASS")
    sys.exit(0 if passed == total else 1)

if __name__ == '__main__':
    main()
