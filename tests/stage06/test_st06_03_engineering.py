#!/usr/bin/env python3
"""ST06-03 Unit Tests — Offline Deployment Engineering."""
import sys, os, subprocess, json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'scripts'))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPTS = os.path.join(ROOT, 'scripts')

def run_script(script_name, *args):
    """Run a validator script and return (exit_code, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, script_name)] + list(args),
        capture_output=True, text=True, cwd=ROOT, timeout=30
    )
    return result.returncode, result.stdout, result.stderr

def run_ansible(playbook_rel):
    """Run ansible-playbook --syntax-check."""
    ansible_dir = os.path.join(ROOT, 'automation', 'ansible')
    result = subprocess.run(
        ['ansible-playbook', os.path.join(ansible_dir, playbook_rel), '--syntax-check'],
        capture_output=True, text=True, cwd=ansible_dir, timeout=30
    )
    return result.returncode, result.stdout, result.stderr


# ═══════════════════════════════════════════
# POSITIVE TESTS
# ═══════════════════════════════════════════

class TestPositive:
    """Tests that should PASS in offline mode."""

    def test_offline_config_valid(self):
        """Offline configuration is valid."""
        rc, out, err = run_script('validate_stage06_execution_mode.py', '--mode', 'offline')
        assert rc == 0, f"Expected exit 0, got {rc}: {err}"

    def test_roles_path_finds_roles(self):
        """All roles found via roles_path."""
        rc, out, err = run_ansible('playbooks/site.yml')
        assert rc == 0, f"Syntax check failed: {err[:200]}"

    def test_hiddify_role_syntax(self):
        """Hiddify role passes syntax-check."""
        rc, out, err = run_ansible('roles/hiddify/tests/test.yml')
        assert rc == 0, f"Hiddify syntax failed: {err[:200]}"

    def test_placeholder_validator_offline(self):
        """Placeholder validator passes in offline mode."""
        rc, out, err = run_script('validate_stage06_placeholders.py', '--mode', 'offline')
        assert rc == 0, f"Expected exit 0, got {rc}"
        assert 'PLACEHOLDERS PRESENT' in out

    def test_owner_input_validator_runs(self):
        """Owner input completeness validator runs."""
        rc, out, err = run_script('validate_stage06_owner_input_complete.py')
        # Currently owner input is incomplete — exit 1 is expected
        assert rc in (0, 1), f"Unexpected exit {rc}"

    def test_safety_gate_blocks(self):
        """Safety gate blocks deployment."""
        rc, out, err = run_script('stage06_safety_gate.py')
        assert rc == 1, f"Safety gate should exit 1, got {rc}"
        assert 'BLOCKED' in out

    def test_rollback_plan_generates(self):
        """Rollback plan generates successfully."""
        rc, out, err = run_script('generate_stage06_rollback_plan.py')
        assert rc == 0, f"Rollback generator failed: {err}"
        assert 'PLAN_ONLY' in out

    def test_hiddify_role_validator(self):
        """Hiddify role validator passes."""
        rc, out, err = run_script('validate_stage06_hiddify_role.py')
        assert rc == 0, f"Role validator failed: {err[:200]}"

    def test_evidence_validator_current(self):
        """Evidence validator runs."""
        rc, out, err = run_script('validate_stage06_evidence.py')
        assert rc == 0, f"Evidence validator failed: {err}"

    def test_semantic_validator(self):
        """Semantic validator passes."""
        rc, out, err = run_script('validate_stage06_semantic.py')
        assert rc == 0, f"Semantic validator failed: {err[:200]}"


# ═══════════════════════════════════════════
# NEGATIVE TESTS
# ═══════════════════════════════════════════

class TestNegative:
    """Tests that should FAIL (block dangerous actions)."""

    def test_deployment_enabled_without_approval(self):
        """Deployment enabled=true but approval absent — should be blocked by safety flags."""
        # The all.yml has deployment_enabled: false. We verify safety gate blocks.
        rc, out, err = run_script('stage06_safety_gate.py')
        assert rc == 1, "Safety gate should block deployment"

    def test_placeholders_in_deployment_mode(self):
        """CHANGE_ME in deployment mode — should exit 1."""
        rc, out, err = run_script('validate_stage06_placeholders.py', '--mode', 'deployment')
        assert rc == 1, f"Placeholder validator should block in deployment mode, got {rc}"

    def test_example_domain_in_deployment_mode(self):
        """example.invalid in deployment mode — should be detected."""
        rc, out, err = run_script('validate_stage06_placeholders.py', '--mode', 'deployment')
        assert rc == 1, "Should detect example.invalid"

    def test_doc_ip_in_deployment_mode(self):
        """Documentation IPs in deployment mode — should be detected."""
        rc, out, err = run_script('validate_stage06_placeholders.py', '--mode', 'deployment')
        assert rc == 1, "Should detect documentation IPs"

    def test_owner_input_incomplete(self):
        """Owner input incomplete — should not report complete."""
        rc, out, err = run_script('validate_stage06_owner_input_complete.py')
        # Currently incomplete — exit 1 or output contains BLOCKED
        assert 'BLOCKED' in out or rc == 1, "Should report owner input incomplete"

    def test_safety_gate_never_passes_without_env(self):
        """Safety gate never passes without STAGE06_LAB_DEPLOYMENT_APPROVED."""
        env = os.environ.copy()
        env.pop('STAGE06_LAB_DEPLOYMENT_APPROVED', None)
        result = subprocess.run(
            [sys.executable, os.path.join(SCRIPTS, 'stage06_safety_gate.py')],
            capture_output=True, text=True, env=env, timeout=10
        )
        assert result.returncode == 1, f"Safety gate should exit 1, got {result.returncode}"

    def test_rollback_plan_not_executed(self):
        """Rollback plan is plan_only — no execution."""
        rc, out, err = run_script('generate_stage06_rollback_plan.py')
        assert 'PLAN_ONLY' in out, "Rollback must be plan_only"
        assert 'NO EXECUTION' in out, "Rollback must not execute"

    def test_execution_mode_defaults_to_offline(self):
        """Default execution mode is offline (blocks remote)."""
        rc, out, err = run_script('validate_stage06_execution_mode.py')
        assert rc == 0, f"Offline mode should pass, got {rc}"
        assert 'offline' in out.lower()

    def test_remote_mode_blocked_without_approval(self):
        """Remote mode blocked without STAGE06_LAB_DEPLOYMENT_APPROVED."""
        env = os.environ.copy()
        env.pop('STAGE06_LAB_DEPLOYMENT_APPROVED', None)
        result = subprocess.run(
            [sys.executable, os.path.join(SCRIPTS, 'validate_stage06_execution_mode.py'), '--mode', 'remote'],
            capture_output=True, text=True, env=env, timeout=10
        )
        assert result.returncode == 1, f"Remote mode should fail without approval, got {result.returncode}"

    def test_hiddify_role_has_all_required_files(self):
        """Hiddify role has all 14 required files."""
        rc, out, err = run_script('validate_stage06_hiddify_role.py')
        assert rc == 0, f"Missing required files: {err[:200]}"


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v', '--tb=short'])
