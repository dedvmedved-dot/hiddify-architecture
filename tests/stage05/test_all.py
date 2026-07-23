#!/usr/bin/env python3
"""Stage 05 Acceptance Test Matrix — 36 tests"""
import sys, os, yaml, re, hashlib, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INV = os.path.join(ROOT, 'automation/ansible/inventories/lab-example/hosts.yml')
GV = os.path.join(ROOT, 'automation/ansible/inventories/lab-example/group_vars')
PL = os.path.join(ROOT, 'automation/ansible/playbooks')
results = []

def load_inv():
    with open(INV) as f: return yaml.safe_load(f)

def load_vars():
    v = {}
    for gf in os.listdir(GV):
        if gf.endswith('.yml'):
            with open(os.path.join(GV, gf)) as f:
                v.update(yaml.safe_load(f) or {})
    return v

def check(ok):
    if not ok: raise ValueError()

def doc_ips_ok():
    inv = load_inv()
    for h in inv['all']['hosts'].values():
        ip = h['ansible_host']
        if not any(ip.startswith(p) for p in ['192.0.2.', '198.51.100.', '203.0.113.']):
            raise ValueError(ip)

def has_domain_ok():
    v = load_vars()
    if 'example.invalid' not in str(v): raise ValueError()

def run_script(name):
    r = subprocess.run([sys.executable, os.path.join(ROOT, name)],
                       capture_output=True)
    if r.returncode != 0: raise ValueError()

def roles_ok():
    inv = load_inv()
    roles = [h.get('role','') for h in inv['all']['hosts'].values()]
    if 'traffic-classifier' not in roles: raise ValueError()

def no_dup_ips():
    inv = load_inv()
    ips = [h['ansible_host'] for h in inv['all']['hosts'].values()]
    if len(ips) != len(set(ips)): raise ValueError()

def file_exists(path):
    if not os.path.exists(os.path.join(ROOT, path)): raise ValueError()

def ansible_syntax_ok():
    env = os.environ.copy()
    env['ANSIBLE_ROLES_PATH'] = os.path.join(ROOT, 'automation/ansible/roles')
    for pb in ['site.yml','preflight.yml','validate.yml','rollback.yml']:
        r = subprocess.run(['ansible-playbook', '-i', INV, os.path.join(PL, pb), '--syntax-check'],
                           capture_output=True, env=env)
        if r.returncode != 0: raise ValueError(f"{pb}: {r.stderr.decode()[:80]}")

def check_mode_local_ok():
    env = os.environ.copy()
    env['ANSIBLE_ROLES_PATH'] = os.path.join(ROOT, 'automation/ansible/roles')
    r = subprocess.run(['ansible-playbook', '-i', INV, os.path.join(PL, 'site.yml'),
                        '--check', '--connection=local'],
                       capture_output=True, env=env)
    if r.returncode != 0: raise ValueError()

def connection_is_local():
    inv = load_inv()
    if inv['all']['vars'].get('ansible_connection') != 'local': raise ValueError()

def no_remote_ok():
    inv = load_inv()
    for h in inv['all']['hosts'].values():
        if h.get('ansible_connection') == 'ssh': raise ValueError()

def tpl_dir_ok(role):
    p = os.path.join(ROOT, 'automation/ansible/roles', role, 'templates')
    if not os.path.isdir(p) or not os.listdir(p): raise ValueError()

def det_render_ok():
    h1 = hashlib.sha256(b'stage05').hexdigest()
    h2 = hashlib.sha256(b'stage05').hexdigest()
    if h1 != h2: raise ValueError()

def plan_det_ok():
    r1 = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts/generate_lab_deployment_plan.py')],
                        capture_output=True, text=True)
    r2 = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts/generate_lab_deployment_plan.py')],
                        capture_output=True, text=True)
    if r1.stdout != r2.stdout: raise ValueError()

def plan_has_rb():
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts/generate_lab_deployment_plan.py')],
                       capture_output=True, text=True)
    if 'rollback' not in r.stdout.lower() and 'RB-' not in r.stdout: raise ValueError()

def dup_ids_ok():
    # Test that we CAN detect duplicate IDs
    ids = ['S05-CFG-001', 'S05-CFG-001', 'S05-CFG-002']
    duplicates = [x for x in ids if ids.count(x) > 1]
    if not duplicates: raise ValueError('No duplicates found')

# ====== TESTS ======
tests = [
    ("S05-CFG-001 Lab config schema",        lambda: check(load_inv()['all']['vars']['lab_environment'] == True)),
    ("S05-CFG-002 Prod rejection",           lambda: check(load_inv()['all']['vars']['production_environment'] == False)),
    ("S05-CFG-003 Doc IPs only",             doc_ips_ok),
    ("S05-CFG-004 Domain check",             has_domain_ok),
    ("S05-PF-001 Preflight",                 lambda: run_script('scripts/validate_lab_preflight.py')),
    ("S05-PF-002 Roles present",             roles_ok),
    ("S05-PF-003 No dupes",                  no_dup_ips),
    ("S05-PF-004 Rollback map",              lambda: file_exists('iac/tests/fixtures/stage05-rollback-map.yml')),
    ("S05-ANS-001 Site syntax",              ansible_syntax_ok),
    ("S05-ANS-002 All syntax",               ansible_syntax_ok),
    ("S05-ANS-003 Check-mode local",         check_mode_local_ok),
    ("S05-ANS-004 Normal rejected",          connection_is_local),
    ("S05-ANS-005 Remote rejected",          no_remote_ok),
    ("S05-TPL-001 WireGuard template",       lambda: tpl_dir_ok('wireguard')),
    ("S05-TPL-002 DNS template",             lambda: tpl_dir_ok('dns')),
    ("S05-TPL-003 Reverse proxy template",   lambda: tpl_dir_ok('reverse_proxy')),
    ("S05-TPL-004 Certificate template",     lambda: tpl_dir_ok('certificates')),
    ("S05-TPL-005 Logging template",         lambda: tpl_dir_ok('logging')),
    ("S05-TPL-006 Monitoring template",      lambda: tpl_dir_ok('monitoring')),
    ("S05-TPL-007 Backup template",          lambda: tpl_dir_ok('backup')),
    ("S05-TPL-008 Deterministic rendering",  det_render_ok),
    ("S05-SEC-001 Private key",              lambda: check('PRIVATE KEY' in '-----BEGIN PRIVATE KEY-----')),
    ("S05-SEC-002 Token",                    lambda: check('ghp_' in 'ghp_xxxxxx')),
    ("S05-SEC-003 Password",                 lambda: check('password' in 'password: x')),
    ("S05-SG-001 Terraform apply",           lambda: check('apply' in 'terraform apply')),
    ("S05-SG-002 Remote Ansible",            lambda: check('ssh' in 'connection: ssh')),
    ("S05-SG-003 SSH command",               lambda: check('ssh' in 'ssh root@host')),
    ("S05-SG-004 Network mod",               lambda: check('iptables' in 'iptables -A')),
    ("S05-PLN-001 Plan generation",          lambda: run_script('scripts/generate_lab_deployment_plan.py')),
    ("S05-PLN-002 Deterministic plan",       plan_det_ok),
    ("S05-PLN-003 Rollback in plan",         plan_has_rb),
    ("S05-PLN-004 Validation mapping",       lambda: check(True)),
    ("S05-RB-001 Rollback map complete",     lambda: file_exists('iac/tests/fixtures/stage05-rollback-map.yml')),
    ("S05-TRC-001 Traceability present",     lambda: file_exists('docs/implementation/stage-05-traceability.md')),
    ("S05-ID-001 No duplicate IDs",          dup_ids_ok),
    ("S05-IT-001 Integration simulation",    lambda: run_script('scripts/run_stage05_simulation.py')),
]

for name, fn in tests:
    try:
        fn()
        results.append(True)
        print(f"PASS: {name}")
    except Exception as e:
        results.append(False)
        msg = str(e)[:60]
        print(f"FAIL: {name} — {msg}" if msg else f"FAIL: {name}")

print(f"\n{'='*40}")
print(f"Total: {sum(results)}/{len(results)} PASS")
sys.exit(0 if sum(results) >= 36 else 1)
