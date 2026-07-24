#!/usr/bin/env python3
"""Unit tests for Stage 06 Semantic Evidence Validator.

Tests cover:
  - Valid package (all checks pass)
  - Wrong HEAD (HEAD mismatch detection)
  - Wrong timestamp (future date detection)
  - Missing metadata (mandatory field absence)
  - Inconsistent deployment state
  - Inconsistent owner state
  - Inconsistent runtime inventory
  - Stage inconsistency
"""
import sys, os, json, tempfile, shutil
from datetime import datetime, timezone, timedelta
from pathlib import Path

import pytest

# Add scripts/ to path to import the validator functions
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'scripts'))

import validate_stage06_semantic as sem


def make_evidence_dir(tmp_path, files):
    """Create a temporary evidence directory with given file contents.
    files: dict of {filename: content}
    """
    edir = tmp_path / 'evidence' / 'stage-06'
    edir.mkdir(parents=True, exist_ok=True)
    for fname, content in files.items():
        (edir / fname).write_text(content)
    return edir


def make_owner_checklist(tmp_path, approval='NO', received='NO'):
    """Create a temporary owner input checklist."""
    stages = tmp_path / 'stages' / 'stage-06-controlled-lab-deployment'
    stages.mkdir(parents=True, exist_ok=True)
    content = (
        f"# Owner Input Checklist\n"
        f"Owner input received: {received}\n"
        f"Deployment approval: {approval}\n"
        f"Deployment status: {'BLOCKED' if approval == 'NO' else 'APPROVED'}\n"
        f"NOT production: {'YES' if approval == 'YES' else 'NO'}\n"
    )
    (stages / 'owner-input-checklist.md').write_text(content)
    return stages / 'owner-input-checklist.md'


HEAD_VALID = 'a' * 40
HEAD_WRONG = 'b' * 40
TS_VALID = '2026-01-01T00:00:00Z'
TS_FUTURE = '2099-12-31T23:59:59Z'


class TestHeadConsistency:
    """HEAD consistency checks."""

    def test_valid_all_same(self, tmp_path):
        """All files have the same HEAD — should PASS."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': f'HEAD: {HEAD_VALID}\nTimestamp: {TS_VALID}\n',
            'b.txt': f'HEAD: {HEAD_VALID}\nTimestamp: {TS_VALID}\n',
            'c.txt': f'HEAD: {HEAD_VALID}\nTimestamp: {TS_VALID}\n',
        })
        assert sem.check_head_consistency(str(edir)) is True

    def test_wrong_head_mismatch(self, tmp_path):
        """Files have different HEAD values — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': f'HEAD: {HEAD_VALID}\nTimestamp: {TS_VALID}\n',
            'b.txt': f'HEAD: {HEAD_WRONG}\nTimestamp: {TS_VALID}\n',
        })
        assert sem.check_head_consistency(str(edir)) is False

    def test_no_head_references(self, tmp_path):
        """No HEAD references at all — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': 'No HEAD here\n',
        })
        assert sem.check_head_consistency(str(edir)) is False


class TestTimestampValidity:
    """Timestamp validity checks."""

    def test_valid_timestamps(self, tmp_path):
        """All timestamps valid and in the past — should PASS."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': f'HEAD: {HEAD_VALID}\nTimestamp: {TS_VALID}\n',
        })
        assert sem.check_timestamp_validity(str(edir)) is True

    def test_future_timestamp(self, tmp_path):
        """Future timestamp — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': f'HEAD: {HEAD_VALID}\nTimestamp: {TS_FUTURE}\n',
        })
        assert sem.check_timestamp_validity(str(edir)) is False

    def test_invalid_format(self, tmp_path):
        """Invalid timestamp format — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': f'HEAD: {HEAD_VALID}\nTimestamp: not-a-timestamp\n',
        })
        result = sem.check_timestamp_validity(str(edir))
        # This file won't match the timestamp regex, so it'll be "missing"
        assert result is False

    def test_missing_timestamp(self, tmp_path):
        """File with no timestamp — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': f'HEAD: {HEAD_VALID}\nNo timestamp\n',
        })
        # No regex match → considered "missing timestamp"
        result = sem.check_timestamp_validity(str(edir))
        assert result is False


class TestTimestampConsistency:
    """Timestamp consistency checks."""

    def test_close_timestamps(self, tmp_path):
        """Timestamps within 10 minutes — should PASS."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': f'HEAD: {HEAD_VALID}\nTimestamp: 2026-01-01T00:00:00Z\n',
            'b.txt': f'HEAD: {HEAD_VALID}\nTimestamp: 2026-01-01T00:05:00Z\n',
        })
        assert sem.check_timestamp_consistency(str(edir)) is True

    def test_spread_too_wide(self, tmp_path):
        """Timestamps more than 10 minutes apart — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': f'HEAD: {HEAD_VALID}\nTimestamp: 2026-01-01T00:00:00Z\n',
            'b.txt': f'HEAD: {HEAD_VALID}\nTimestamp: 2026-01-01T01:00:00Z\n',
        })
        assert sem.check_timestamp_consistency(str(edir)) is False


class TestMandatoryMetadata:
    """Mandatory metadata field checks."""

    def test_all_present(self, tmp_path):
        """All mandatory fields present — should PASS."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': (
                'Stage: 06\n'
                f'HEAD: {HEAD_VALID}\n'
                'Timestamp: 2026-01-01T00:00:00Z\n'
            ),
        })
        assert sem.check_mandatory_metadata(str(edir)) is True

    def test_missing_head(self, tmp_path):
        """Missing HEAD field — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': 'Stage: 06\nTimestamp: 2026-01-01T00:00:00Z\n',
        })
        assert sem.check_mandatory_metadata(str(edir)) is False

    def test_missing_timestamp(self, tmp_path):
        """Missing Timestamp field — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': 'Stage: 06\nHEAD: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n',
        })
        assert sem.check_mandatory_metadata(str(edir)) is False

    def test_missing_stage(self, tmp_path):
        """Missing Stage field — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': (
                f'HEAD: {HEAD_VALID}\nTimestamp: 2026-01-01T00:00:00Z\n'
            ),
        })
        assert sem.check_mandatory_metadata(str(edir)) is False


class TestEvidenceConsistency:
    """Evidence consistency checks between files."""

    def test_consistent_blocked(self, tmp_path, monkeypatch):
        """Owner not received + deployment blocked — should PASS."""
        edir = make_evidence_dir(tmp_path, {
            'deployment-phase-summary.txt': 'Deployment: BLOCKED\n',
            'owner-input-validation.txt': 'Owner input: NOT RECEIVED\nDeployment: BLOCKED\n',
            'environment-access-declaration.txt': 'Deployment performed: NO\n',
            'safety-gate-summary.txt': 'Safety gate: BLOCKED\n',
        })
        # Override the evidence dir path for consistency check
        monkeypatch.setattr(sem, 'E', str(edir))
        assert sem.check_evidence_consistency() is True

    def test_inconsistent_owner_received_not_blocked(self, tmp_path, monkeypatch):
        """Owner NOT received but deployment not BLOCKED — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'deployment-phase-summary.txt': 'Deployment: ACTIVE\n',
            'owner-input-validation.txt': 'Owner input: NOT RECEIVED\n',
            'environment-access-declaration.txt': 'Deployment performed: NO\n',
            'safety-gate-summary.txt': 'Safety gate: PASS\n',
        })
        monkeypatch.setattr(sem, 'E', str(edir))
        assert sem.check_evidence_consistency() is False


class TestBlockedStateValidation:
    """Blocked state validation when owner input=NO."""

    def test_owner_no_all_blocked(self, tmp_path, monkeypatch):
        """Owner=NO → all deployment files BLOCKED — should PASS."""
        edir = make_evidence_dir(tmp_path, {
            'deployment-phase-summary.txt': 'Deployment: BLOCKED\n',
            'owner-input-validation.txt': 'Owner input: NOT RECEIVED\nDeployment: BLOCKED\n',
            'safety-gate-summary.txt': 'Safety gate: BLOCKED\n',
            'validation-summary.txt': 'Validation: DEPLOYMENT BLOCKED\n',
        })
        monkeypatch.setattr(sem, 'E', str(edir))
        checklist = make_owner_checklist(tmp_path, approval='NO', received='NO')
        monkeypatch.setattr(sem, 'OWNER_CHECKLIST', str(checklist))
        assert sem.check_blocked_state_validation() is True

    def test_owner_no_but_not_blocked(self, tmp_path, monkeypatch):
        """Owner=NO but deployment not BLOCKED — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'deployment-phase-summary.txt': 'Deployment: ACTIVE\n',
            'owner-input-validation.txt': 'Owner input: NOT RECEIVED\nDeployment: BLOCKED\n',
            'safety-gate-summary.txt': 'Safety gate: PASS\n',
            'validation-summary.txt': 'Validation: PASS\n',
        })
        monkeypatch.setattr(sem, 'E', str(edir))
        checklist = make_owner_checklist(tmp_path, approval='NO', received='NO')
        monkeypatch.setattr(sem, 'OWNER_CHECKLIST', str(checklist))
        assert sem.check_blocked_state_validation() is False

    def test_owner_yes_skips_blocked_check(self, tmp_path, monkeypatch):
        """Owner=YES — blocked check skipped gracefully."""
        edir = make_evidence_dir(tmp_path, {
            'deployment-phase-summary.txt': 'Deployment: ACTIVE\n',
            'owner-input-validation.txt': 'Owner input: RECEIVED\nDeployment: APPROVED\n',
            'safety-gate-summary.txt': 'Safety gate: PASS\n',
            'validation-summary.txt': 'Validation: PASS\n',
        })
        monkeypatch.setattr(sem, 'E', str(edir))
        checklist = make_owner_checklist(tmp_path, approval='YES', received='YES')
        monkeypatch.setattr(sem, 'OWNER_CHECKLIST', str(checklist))
        assert sem.check_blocked_state_validation() is True


class TestStageConsistency:
    """Stage consistency checks."""

    def test_all_same_stage(self, tmp_path):
        """All files reference Stage 06 — should PASS."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': 'Stage: 06\nHEAD: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nTimestamp: 2026-01-01T00:00:00Z\n',
            'b.txt': 'Stage: 06\nHEAD: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nTimestamp: 2026-01-01T00:00:00Z\n',
        })
        assert sem.check_stage_consistency(str(edir)) is True

    def test_mixed_stages(self, tmp_path):
        """Mixed stage references — should FAIL."""
        edir = make_evidence_dir(tmp_path, {
            'a.txt': 'Stage: 06\nHEAD: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nTimestamp: 2026-01-01T00:00:00Z\n',
            'b.txt': 'Stage: 05\nHEAD: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nTimestamp: 2026-01-01T00:00:00Z\n',
        })
        assert sem.check_stage_consistency(str(edir)) is False
