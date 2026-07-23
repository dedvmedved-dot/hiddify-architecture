#!/usr/bin/env python3
"""Stage 05 Check-Mode Harness — S05-ANS-001/002"""
import sys, os, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    inv_path = os.path.join(ROOT, 'automation/ansible/inventories/lab-example/hosts.yml')
    playbook = os.path.join(ROOT, 'automation/ansible/playbooks/site.yml')

    # Syntax check
    print("=== Syntax Check ===")
    r = subprocess.run(['ansible-playbook', playbook, '--syntax-check'],
                       capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr.strip())
    ok = r.returncode == 0

    # Check mode
    print("=== Check Mode (local) ===")
    r2 = subprocess.run(['ansible-playbook', playbook, '--check', '--connection=local'],
                        capture_output=True, text=True)
    print(r2.stdout.strip()[:200])
    ok = ok and r2.returncode == 0

    print(f"\nCHECK_MODE_VALID: {ok}")
    sys.exit(0 if ok else 1)

if __name__ == '__main__': main()
