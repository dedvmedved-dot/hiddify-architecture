#!/usr/bin/env python3
"""Stage 06 Hiddify Role Validator — checks role structure and syntax."""
import sys, os, json, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANSIBLE_DIR = os.path.join(ROOT, 'automation', 'ansible')
HIDDIFY_ROLE = os.path.join(ANSIBLE_DIR, 'roles', 'hiddify')
TEST_PLAYBOOK = os.path.join(HIDDIFY_ROLE, 'tests', 'test.yml')

REQUIRED_FILES = [
    'README.md', 'defaults/main.yml', 'handlers/main.yml', 'meta/main.yml',
    'tasks/main.yml', 'tasks/preflight.yml', 'tasks/install.yml',
    'tasks/configure.yml', 'tasks/service.yml', 'tasks/validate.yml',
    'templates/hiddify-panel.env.j2', 'templates/docker-compose.yml.j2',
    'templates/hiddify-panel.service.j2', 'vars/main.yml',
]

def main():
    print("=" * 60)
    print("Stage 06 Hiddify Role Validator")
    print("=" * 60)

    results = []
    missing = [f for f in REQUIRED_FILES if not os.path.exists(os.path.join(HIDDIFY_ROLE, f))]
    if missing:
        for m in missing:
            print(f"  FAIL: missing file {m}")
            results.append(False)
    else:
        print(f"  PASS: all {len(REQUIRED_FILES)} required files present")
        results.append(True)

    # Syntax check
    os.chdir(ANSIBLE_DIR)
    rc = subprocess.run(
        ['ansible-playbook', TEST_PLAYBOOK, '--syntax-check'],
        capture_output=True, text=True
    )
    syntax_ok = rc.returncode == 0
    if syntax_ok:
        print("  PASS: syntax-check passed")
    else:
        print(f"  FAIL: syntax-check failed\n{rc.stderr[:200]}")
    results.append(syntax_ok)

    all_ok = all(results)
    report = {
        'files_present': len(REQUIRED_FILES) - len(missing),
        'files_missing': len(missing),
        'syntax_check': 'PASS' if syntax_ok else 'FAIL',
        'result': 'PASS' if all_ok else 'FAIL'
    }
    print(json.dumps(report, indent=2))
    sys.exit(0 if all_ok else 1)

if __name__ == '__main__':
    main()
