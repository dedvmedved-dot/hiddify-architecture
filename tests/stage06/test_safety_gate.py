#!/usr/bin/env python3
"""Unit tests for Stage 06 Safety Gate.

Tests cover:
  - Deployment blocked (default — no env var set)
  - Deployment blocked (explicit NO)
  - Exit codes for blocked state
  - No || true masking in workflow
  - Clear error messages
"""
import sys, os, tempfile, subprocess
from pathlib import Path

import pytest

# Path to safety gate script
SAFETY_GATE = os.path.join(
    os.path.dirname(__file__), '..', '..', 'scripts', 'stage06_safety_gate.py'
)


def run_safety_gate(env_extra=None):
    """Run safety gate script and return (exit_code, stdout, stderr)."""
    env = os.environ.copy()
    if env_extra:
        env.update(env_extra)
    result = subprocess.run(
        [sys.executable, SAFETY_GATE],
        capture_output=True, text=True, env=env,
    )
    return result.returncode, result.stdout, result.stderr


class TestSafetyGateBlocked:
    """Safety gate should block deployment without approval."""

    def test_deployment_blocked_by_default(self):
        """STAGE06_LAB_DEPLOYMENT_APPROVED=NO — should exit 1."""
        rc, stdout, stderr = run_safety_gate(
            {'STAGE06_LAB_DEPLOYMENT_APPROVED': 'NO'}
        )
        assert rc == 1, f"Expected exit 1, got {rc}"
        assert 'BLOCKED' in stdout

    def test_deployment_blocked_no_variable(self):
        """No env variable at all — should exit 1."""
        env = os.environ.copy()
        env.pop('STAGE06_LAB_DEPLOYMENT_APPROVED', None)
        result = subprocess.run(
            [sys.executable, SAFETY_GATE],
            capture_output=True, text=True, env=env,
        )
        assert result.returncode == 1

    def test_deployment_blocked_message(self):
        """Blocked message is clear and actionable."""
        rc, stdout, stderr = run_safety_gate(
            {'STAGE06_LAB_DEPLOYMENT_APPROVED': 'NO'}
        )
        assert 'BLOCKED' in stdout
        assert 'STAGE06_LAB_DEPLOYMENT_APPROVED' in stdout
        assert 'export' in stdout


class TestSafetyGateApproved:
    """Safety gate env-var gate passes when STAGE06_LAB_DEPLOYMENT_APPROVED=YES.

    Note: Full approval also requires the owner-input-checklist.md to contain
    'Deployment approval: YES' and 'NOT production: YES'. These are checked as
    a second gate after the env var check. When the real checklist file does not
    contain these strings (as in the BLOCKED baseline), the safety gate will
    exit 1 at the checklist check even with the env var set.
    """

    def test_env_var_gate_passes(self):
        """Setting STAGE06_LAB_DEPLOYMENT_APPROVED=YES passes the env-var gate.

        The second gate (checklist check) may fail if the checklist hasn't been
        updated, but the env-var gate itself works correctly.
        """
        rc, stdout, stderr = run_safety_gate(
            {'STAGE06_LAB_DEPLOYMENT_APPROVED': 'YES'}
        )
        # At minimum the env-var check is bypassed correctly
        assert 'STAGE06_LAB_DEPLOYMENT_APPROVED is not YES' not in stdout


class TestSafetyGateExitCodes:
    """Exit code behavior."""

    def test_blocked_exit_code_is_one(self):
        """Blocked deployment MUST exit with code 1."""
        rc, stdout, stderr = run_safety_gate(
            {'STAGE06_LAB_DEPLOYMENT_APPROVED': 'NO'}
        )
        assert rc == 1

    def test_blocked_exit_is_not_zero(self):
        """Blocked deployment must NOT exit with code 0."""
        rc, stdout, stderr = run_safety_gate(
            {'STAGE06_LAB_DEPLOYMENT_APPROVED': 'NO'}
        )
        assert rc != 0


class TestSafetyGateNoMasking:
    """Verify safety gate is no longer masked with || true."""

    def test_no_or_true_in_workflow(self):
        """stage-06-validation.yml does not use || true on safety gate."""
        workflow_path = os.path.join(
            os.path.dirname(__file__), '..', '..', '.github',
            'workflows', 'stage-06-validation.yml'
        )
        with open(workflow_path) as f:
            content = f.read()

        safety_gate_lines = [
            line for line in content.split('\n')
            if 'stage06_safety_gate' in line
        ]
        for line in safety_gate_lines:
            assert '|| true' not in line, (
                f"Safety gate still masked: {line.strip()}"
            )

    def test_expect_exit_code_used_for_safety_gate(self):
        """Safety gate uses expect_exit_code.sh for strict exit code validation."""
        workflow_path = os.path.join(
            os.path.dirname(__file__), '..', '..', '.github',
            'workflows', 'stage-06-validation.yml'
        )
        with open(workflow_path) as f:
            content = f.read()
        # Safety gate step must use expect_exit_code.sh with expected exit 1
        assert 'expect_exit_code.sh 1 python3 scripts/stage06_safety_gate.py' in content
