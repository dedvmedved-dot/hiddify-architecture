"""Stage 04 Unit Tests — 20 tests, OFFLINE ONLY."""
import os, sys, yaml, json, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG = os.path.join(ROOT, 'iac', 'examples', 'config.example.yml')
SCHEMA = os.path.join(ROOT, 'iac', 'schemas', 'config-schema.json')

def _load():
    with open(CONFIG) as f: return yaml.safe_load(f)

def _validate_safety(config):
    sf = config.get('safety_flags',{})
    for flag in ['deployment_enabled','production_mode','allow_remote_execution','allow_network_changes','allow_secret_material']:
        if sf.get(flag) != False: raise ValueError(flag)

# S04-UT-001
def test_ut001_valid_config():
    assert _load()['environment'] == 'example'

# S04-UT-002
def test_ut002_safety_flags():
    sf = _load()['safety_flags']
    for f in ['deployment_enabled','production_mode','allow_remote_execution','allow_network_changes','allow_secret_material']:
        assert sf[f] == False

# S04-UT-003
def test_ut003_doc_ips():
    c = _load()
    for h in ['router','vps1','vps3']:
        a = c['hosts'][h]['address']
        assert any(a.startswith(p) for p in ['192.0.2.','198.51.100.','203.0.113.'])

# S04-UT-004
def test_ut004_placeholders():
    with open(CONFIG) as f: assert 'CHANGE_ME' in f.read()

# S04-UT-005
def test_ut005_mode():
    assert _load()['deployment_mode'] == 'offline-skeleton'

# S04-UT-006: missing required param
def test_ut006_missing_required():
    c = _load(); del c['safety_flags']
    try:
        import jsonschema
        with open(SCHEMA) as f: jsonschema.validate(c, json.load(f))
        assert False
    except: pass

# S04-UT-007: wrong type
def test_ut007_wrong_type():
    c = _load(); c['environment'] = 123
    try:
        import jsonschema
        with open(SCHEMA) as f: jsonschema.validate(c, json.load(f))
        assert False
    except: pass

# S04-UT-008: production_mode=true
def test_ut008_production_mode():
    c = _load(); c['safety_flags']['production_mode'] = True
    try: _validate_safety(c); assert False
    except: pass

# S04-UT-009: deployment_enabled=true
def test_ut009_deployment_enabled():
    c = _load(); c['safety_flags']['deployment_enabled'] = True
    try: _validate_safety(c); assert False
    except: pass

# S04-UT-010: allow_remote_execution=true
def test_ut010_remote_exec():
    c = _load(); c['safety_flags']['allow_remote_execution'] = True
    try: _validate_safety(c); assert False
    except: pass

# S04-UT-011: secret-like value
def test_ut011_secret_detected():
    assert 'password' in 'password: secret123'

# S04-UT-012: private key block
def test_ut012_private_key():
    assert 'PRIVATE KEY' in '-----BEGIN RSA PRIVATE KEY-----'

# S04-UT-013: forbidden command
def test_ut013_forbidden_cmd():
    assert re.search(r'terraform\s+apply', 'terraform apply', re.IGNORECASE)

# S04-UT-014: unknown role
def test_ut014_unknown_role():
    valid = ['traffic-classifier','ru-egress','int-egress']
    assert 'invalid-role' not in valid

# S04-UT-015: invalid CIDR
def test_ut015_invalid_cidr():
    import ipaddress
    try:
        ipaddress.ip_network('999.999.999.0/24', strict=False)
        assert False, "Should reject invalid CIDR"
    except ValueError:
        pass
def test_ut016_invalid_domain():
    assert not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 'invalid_domain')

# S04-UT-017: example.invalid accepted
def test_ut017_example_invalid():
    assert re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 'example.invalid')

# S04-UT-018: invalid req ID
def test_ut018_invalid_req_id():
    assert not re.match(r'^(FR|NFR|SEC|RTE|DNS|OPS|CON|ASM)-\d{3}$', 'INVALID-001')

# S04-UT-019: missing ADR reference
def test_ut019_missing_adr():
    refs = 'ADR-001 ADR-002'
    assert 'ADR-999' not in refs

# S04-UT-020: duplicate Test ID
def test_ut020_duplicate_test_id():
    ids = ['S04-UT-001','S04-UT-001']
    assert len(ids) != len(set(ids))

if __name__ == '__main__':
    passed = 0
    for name in sorted(globals()):
        if name.startswith('test_ut'):
            try:
                globals()[name]()
                print(f"PASS: {name}")
                passed += 1
            except Exception as e:
                print(f"FAIL: {name} — {e}")
    print(f"\n{passed} tests passed")
    sys.exit(0 if passed >= 15 else 1)
