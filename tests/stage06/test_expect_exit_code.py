#!/usr/bin/env python3
"""Unit tests for expect_exit_code.sh — strict negative gate helper."""
import os, subprocess, stat, pytest

HELPER = os.path.join(os.path.dirname(__file__), '..', '..', 'scripts', 'expect_exit_code.sh')

def run_helper(expected, command):
    """Run expect_exit_code.sh and return (exit_code, stdout, stderr)."""
    result = subprocess.run(
        ['bash', HELPER, str(expected), command],
        capture_output=True, text=True, timeout=10
    )
    return result.returncode, result.stdout, result.stderr


class TestHelperPass:
    """Tests where helper should PASS (exit 0)."""

    def test_expected_0_got_0(self):
        """Expected 0, command returns 0 → PASS."""
        rc, out, err = run_helper(0, 'true')
        assert rc == 0, f"Expected exit 0, got {rc}: {out}"
        assert 'PASS' in out

    def test_expected_1_got_1(self):
        """Expected 1, command returns 1 → PASS."""
        rc, out, err = run_helper(1, 'exit 1')
        assert rc == 0, f"Expected exit 0, got {rc}"
        assert 'PASS' in out


class TestHelperFail:
    """Tests where helper should FAIL (exit 1)."""

    def test_expected_1_got_0(self):
        """Expected 1, command returns 0 → FAIL."""
        rc, out, err = run_helper(1, 'true')
        assert rc == 1, f"Expected exit 1, got {rc}"
        assert 'FAIL' in out

    def test_expected_0_got_1(self):
        """Expected 0, command returns 1 → FAIL."""
        rc, out, err = run_helper(0, 'exit 1')
        assert rc == 1, f"Expected exit 1, got {rc}"
        assert 'FAIL' in out

    def test_command_not_found(self):
        """Command does not exist → FAIL."""
        rc, out, err = run_helper(0, '/nonexistent/command_xyz_123')
        assert rc == 1, f"Expected exit 1, got {rc}"

    def test_expected_1_got_2(self):
        """Expected 1, got 2 → FAIL."""
        rc, out, err = run_helper(1, 'exit 2')
        assert rc == 1, f"Expected exit 1, got {rc}"
        assert 'FAIL' in out

    def test_missing_arguments(self):
        """No arguments → FAIL."""
        result = subprocess.run(
            ['bash', HELPER],
            capture_output=True, text=True, timeout=10
        )
        assert result.returncode == 1, f"Expected exit 1, got {result.returncode}"

    def test_invalid_expected_code(self):
        """Non-numeric expected code → FAIL."""
        result = subprocess.run(
            ['bash', HELPER, 'abc', 'true'],
            capture_output=True, text=True, timeout=10
        )
        assert result.returncode == 1, f"Expected exit 1, got {result.returncode}"


class TestHelperOutput:
    """Tests for correct output format."""

    def test_output_contains_expected_actual(self):
        """Output shows expected and actual exit codes."""
        rc, out, err = run_helper(1, 'exit 1')
        assert 'EXPECTED EXIT CODE: 1' in out
        assert 'ACTUAL EXIT CODE: 1' in out

    def test_output_contains_command(self):
        """Output shows the command being tested."""
        rc, out, err = run_helper(0, 'true')
        assert 'COMMAND: true' in out


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v', '--tb=short'])
