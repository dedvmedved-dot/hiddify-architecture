#!/usr/bin/env python3
"""Stage 06 Execution Mode Validator — enforces safe execution modes."""
import sys, os, json, argparse
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVENTORY = os.path.join(ROOT, 'automation', 'ansible', 'inventories', 'lab-example')

def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f) or {}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['offline', 'check', 'remote'], default='offline')
    args = parser.parse_args()

    all_vars = load_yaml(os.path.join(INVENTORY, 'group_vars', 'all.yml'))
    deployment_enabled = all_vars.get('deployment_enabled', False)
    remote_exec = all_vars.get('remote_execution_enabled', False)
    allow_network = all_vars.get('allow_network_changes', False)
    allow_secrets = all_vars.get('allow_secret_material', False)
    lab_env = all_vars.get('lab_environment', False)
    prod_env = all_vars.get('production_environment', True)

    checks = []
    def chk(name, ok): checks.append(ok); print(f"  {'PASS' if ok else 'FAIL'}: {name}"); return ok

    print("=" * 60)
    print(f"Stage 06 Execution Mode Validator — mode={args.mode}")
    print("=" * 60)

    if args.mode == 'offline':
        chk("deployment_enabled is false", not deployment_enabled)
        chk("remote_execution_enabled is false", not remote_exec)
        chk("allow_network_changes is false", not allow_network)
        chk("allow_secret_material is false", not allow_secrets)
        chk("lab_environment is true", lab_env)
        chk("production_environment is false", not prod_env)
    elif args.mode == 'check':
        chk("deployment_enabled is false (check mode)", not deployment_enabled)
        chk("remote_execution_enabled is false (check mode)", not remote_exec)
        chk("lab_environment is true", lab_env)
        chk("production_environment is false", not prod_env)
    elif args.mode == 'remote':
        chk("deployment_enabled is true", deployment_enabled)
        chk("remote_execution_enabled is true", remote_exec)
        chk("lab_environment is true", lab_env)
        chk("production_environment is false", not prod_env)
        chk("STAGE06_LAB_DEPLOYMENT_APPROVED=YES", os.environ.get('STAGE06_LAB_DEPLOYMENT_APPROVED') == 'YES')

    passed = sum(checks)
    total = len(checks)
    print(f"\nExecution mode check: {passed}/{total} PASS")
    result = all(checks)
    print(json.dumps({'mode': args.mode, 'checks_passed': passed, 'checks_total': total, 'result': 'PASS' if result else 'FAIL'}, indent=2))
    sys.exit(0 if result else 1)

if __name__ == '__main__':
    main()
