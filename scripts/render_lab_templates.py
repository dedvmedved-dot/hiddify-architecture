#!/usr/bin/env python3
"""Stage 05 Template Renderer — renders to temporary directory only."""
import sys, os, tempfile, hashlib, yaml
from pathlib import Path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'automation', 'ansible'))

def render_one(tpl_path, vars_dict, out_dir):
    from jinja2 import Template
    with open(tpl_path) as f:
        tmpl = Template(f.read())
    result = tmpl.render(**vars_dict)
    out_name = os.path.basename(tpl_path).replace('.j2', '')
    out_path = os.path.join(out_dir, out_name)
    with open(out_path, 'w') as f:
        f.write(result)
    return hashlib.sha256(result.encode()).hexdigest(), result

def main():
    inv_path = os.path.join(ROOT, 'automation/ansible/inventories/lab-example/hosts.yml')
    gv_dir = os.path.join(ROOT, 'automation/ansible/inventories/lab-example/group_vars')

    vars_dict = {}
    for gf in os.listdir(gv_dir):
        if gf.endswith('.yml'):
            with open(os.path.join(gv_dir, gf)) as f:
                vars_dict.update(yaml.safe_load(f) or {})

    templates = [
        'automation/ansible/roles/wireguard/templates/wireguard.conf.j2',
        'automation/ansible/roles/dns/templates/dns-routing.conf.j2',
        'automation/ansible/roles/reverse_proxy/templates/reverse-proxy.conf.j2',
        'automation/ansible/roles/certificates/templates/certificate-placeholder.conf.j2',
        'automation/ansible/roles/logging/templates/logging.conf.j2',
        'automation/ansible/roles/monitoring/templates/monitoring.conf.j2',
        'automation/ansible/roles/backup/templates/backup.conf.j2',
    ]

    passed = 0
    with tempfile.TemporaryDirectory() as tmpdir:
        hashes = {}
        for tp in templates:
            tpf = os.path.join(ROOT, tp)
            if not os.path.exists(tpf):
                print(f"  SKIP: {tp}")
                continue
            try:
                h, content = render_one(tpf, vars_dict, tmpdir)
            except Exception as e:
                print(f"  FAIL: {tp} — {e}")
                continue
            hashes[tp] = h
            if 'CHANGE_ME' in content:
                print(f"  PASS: {tp} (placeholder present)")
            else:
                print(f"  PASS: {tp}")
            passed += 1

        # Determinism check: render twice
        h2 = {}
        for tp in templates:
            tpf = os.path.join(ROOT, tp)
            if os.path.exists(tpf):
                h2[tp] = render_one(tpf, vars_dict, tmpdir)[0]

        det_ok = all(hashes[k] == h2[k] for k in hashes)
        if det_ok: print("  PASS: Deterministic rendering"); passed += 1
        else: print("  FAIL: Non-deterministic rendering")

    print(f"Result: {passed}/8 PASS")
    sys.exit(0 if passed >= 7 else 1)

if __name__ == '__main__':
    import jinja2  # verify available
    main()
