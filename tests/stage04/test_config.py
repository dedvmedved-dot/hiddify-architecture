# Stage 04 Unit Tests — OFFLINE ONLY
import os, yaml, sys

def _load_config():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'iac', 'examples', 'config.example.yml')
    with open(path) as f:
        return yaml.safe_load(f)

def test_config_loads():
    config = _load_config()
    assert config['environment'] == 'example'
    assert config['safety_flags']['deployment_enabled'] == False

def test_safety_flags():
    config = _load_config()
    for flag in ['deployment_enabled', 'production_mode', 'allow_remote_execution', 'allow_network_changes', 'allow_secret_material']:
        assert config['safety_flags'][flag] == False, f"{flag} must be false"

def test_documentation_ips():
    config = _load_config()
    for host_key in ['router', 'vps1', 'vps3']:
        addr = config['hosts'][host_key]['address']
        assert any(addr.startswith(p) for p in ['192.0.2.', '198.51.100.', '203.0.113.']), \
            f"{host_key} uses non-documentation IP: {addr}"

def test_placeholder_present():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'iac', 'examples', 'config.example.yml')
    with open(path) as f:
        content = f.read()
    assert 'CHANGE_ME' in content

def test_deployment_mode():
    config = _load_config()
    assert config['deployment_mode'] == 'offline-skeleton'

if __name__ == '__main__':
    passed = 0
    for name in list(globals().keys()):
        if name.startswith('test_'):
            try:
                globals()[name]()
                print(f"PASS: {name}")
                passed += 1
            except Exception as e:
                print(f"FAIL: {name} — {e}")
    print(f"\n{passed} tests passed")
    sys.exit(0 if passed == 5 else 1)
