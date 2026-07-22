#!/usr/bin/env python3
"""Stage 04 Offline Validation CLI."""
import sys, os, json, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TESTS_DIR = os.path.join(ROOT, 'tests', 'stage04')

def check(label, fn):
    try:
        fn()
        print(f"  PASS: {label}")
        return True
    except Exception as e:
        print(f"  FAIL: {label}", file=sys.stderr)
        return False

def validate_config():
    import yaml
    with open(os.path.join(ROOT, 'iac/schemas/config-schema.json')) as f:
        json.load(f)
    with open(os.path.join(ROOT, 'iac/examples/config.example.yml')) as f:
        config = yaml.safe_load(f)
    sf = config.get('safety_flags', {})
    assert sf.get('deployment_enabled') == False
    assert sf.get('production_mode') == False
    assert sf.get('allow_remote_execution') == False
    assert sf.get('allow_network_changes') == False
    assert sf.get('allow_secret_material') == False
    assert config.get('deployment_mode') == 'offline-skeleton'

def validate_placeholders():
    with open(os.path.join(ROOT, 'iac/examples/config.example.yml')) as f:
        content = f.read()
    assert 'CHANGE_ME' in content, "Must use CHANGE_ME placeholder"
    # Allow RFC 5737 documentation ranges: 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24
    content_clean = content
    for rfc in ['192\.0\.2\.', '198\.51\.100\.', '203\.0\.113\.']:
        content_clean = re.sub(rfc + r'\d{1,3}', 'DOC_IP', content_clean)
    real = re.findall(r'\b(10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3})\b', content_clean)
    assert not real, f"Potential real IPs: {real}"

def validate_structure():
    for d in ['iac', 'automation', 'scripts', 'tests/stage04']:
        assert os.path.isdir(os.path.join(ROOT, d)), f"Missing: {d}"

def run_unit_tests():
    if os.path.isdir(TESTS_DIR):
        for fn in sorted(os.listdir(TESTS_DIR)):
            if fn.startswith('test_') and fn.endswith('.py'):
                ns = {}
                with open(os.path.join(TESTS_DIR, fn)) as f:
                    exec(f.read(), ns)
                for name, obj in ns.items():
                    if name.startswith('test_') and callable(obj):
                        obj()
                        print(f"  PASS: {fn}::{name}")

def main():
    print("Stage 04 Offline Validation")
    results = []
    results.append(check("Config schema validation", validate_config))
    results.append(check("Placeholder validation", validate_placeholders))
    results.append(check("Directory structure", validate_structure))
    results.append(check("Unit tests", run_unit_tests))
    
    passed = sum(results)
    total = len(results)
    print(f"Result: {passed}/{total} PASS")
    sys.exit(0 if passed == total else 1)

if __name__ == '__main__':
    main()
