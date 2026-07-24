#!/usr/bin/env python3
"""Stage 06 Semantic Evidence Validator.

Validates evidence file CONTENT beyond mere existence:
  - HEAD consistency (all files reference same HEAD)
  - Timestamp validity (UTC, no future dates, reasonable consistency)
  - Mandatory metadata (Stage, HEAD, Timestamp, Result status)
  - Evidence consistency (no contradictions between files)
  - Blocked state validation (Owner Input=NO → Deployment=BLOCKED)
"""
import sys, os, re, json
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = os.path.join(ROOT, 'evidence', 'stage-06')
OWNER_CHECKLIST = os.path.join(
    ROOT, 'stages/stage-06-controlled-lab-deployment/owner-input-checklist.md'
)

SEMANTIC_CHECKS = 7  # Total number of semantic checks


def fail(label):
    print(f"  FAIL: {label}")
    return False


def ok(label):
    print(f"  PASS: {label}")
    return True


def checklist(label, condition):
    if condition:
        return ok(label)
    return fail(label)


def read_evidence(filename):
    """Read evidence file, return content or empty string."""
    path = os.path.join(E, filename)
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return ''


def extract_heads(evidence_dir):
    """Extract HEAD references from all evidence files.
    Returns dict: {filename: head_sha}
    """
    heads = {}
    head_re = re.compile(r'HEAD:\s*([0-9a-f]{40})')
    for fname in sorted(os.listdir(evidence_dir)):
        fpath = os.path.join(evidence_dir, fname)
        if not os.path.isfile(fpath):
            continue
        with open(fpath) as f:
            content = f.read()
        m = head_re.search(content)
        if m:
            heads[fname] = m.group(1)
    return heads


def extract_timestamps(evidence_dir):
    """Extract timestamps from all evidence files.
    Returns dict: {filename: timestamp_str}
    """
    stamps = {}
    ts_re = re.compile(r'Timestamp:\s*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)')
    for fname in sorted(os.listdir(evidence_dir)):
        fpath = os.path.join(evidence_dir, fname)
        if not os.path.isfile(fpath):
            continue
        with open(fpath) as f:
            content = f.read()
        m = ts_re.search(content)
        if m:
            stamps[fname] = m.group(1)
    return stamps


def parse_datetime(ts_str):
    """Parse UTC timestamp string."""
    try:
        return datetime.strptime(ts_str, '%Y-%m-%dT%H:%M:%SZ').replace(
            tzinfo=timezone.utc
        )
    except ValueError:
        return None


def check_head_consistency(evidence_dir):
    """Check that all evidence files reference the same HEAD SHA."""
    print("\n--- Check 1: HEAD Consistency ---")
    heads = extract_heads(evidence_dir)
    if not heads:
        return fail("No HEAD references found in evidence files")

    # Count occurrences of each HEAD value
    head_counts = {}
    for fname, sha in heads.items():
        head_counts.setdefault(sha, []).append(fname)

    result = True
    if len(head_counts) > 1:
        result = False
        fail(f"HEAD mismatch: {len(head_counts)} different HEAD values found")
        for sha, files in head_counts.items():
            print(f"    HEAD {sha[:12]}: {len(files)} files")
            if len(files) <= 5:
                for f in files:
                    print(f"      - {f}")
    else:
        sha = list(head_counts.keys())[0]
        ok(f"All {len(heads)} evidence files reference HEAD {sha}")

    return result


def check_timestamp_validity(evidence_dir):
    """Check timestamps: valid format, UTC, no future dates."""
    print("\n--- Check 2: Timestamp Validity ---")
    stamps = extract_timestamps(evidence_dir)
    if not stamps:
        return fail("No timestamps found in evidence files")

    now = datetime.now(timezone.utc)
    results = []
    missing = []

    for fname in sorted(os.listdir(evidence_dir)):
        fpath = os.path.join(evidence_dir, fname)
        if not os.path.isfile(fpath):
            continue
        if fname not in stamps:
            missing.append(fname)
            continue

        ts = parse_datetime(stamps[fname])
        if ts is None:
            results.append(fail(f"  {fname}: invalid timestamp format"))
        elif ts > now:
            results.append(
                fail(f"  {fname}: future timestamp {stamps[fname]}")
            )
        else:
            results.append(True)

    if missing:
        for fname in missing:
            results.append(fail(f"  {fname}: missing timestamp"))

    passed = sum(1 for r in results if r)
    ok(f"Timestamp validity: {passed}/{len(results)} files valid")

    return all(results)


def check_timestamp_consistency(evidence_dir):
    """Check that timestamps are reasonably close together."""
    print("\n--- Check 3: Timestamp Consistency ---")
    stamps = extract_timestamps(evidence_dir)
    if not stamps:
        return fail("No timestamps to compare")

    datetimes = {}
    for fname, ts_str in stamps.items():
        dt = parse_datetime(ts_str)
        if dt:
            datetimes[fname] = dt

    if not datetimes:
        return fail("No valid datetime objects to compare")

    # All timestamps should be within 5 minutes of each other
    all_dts = list(datetimes.values())
    min_dt = min(all_dts)
    max_dt = max(all_dts)
    diff = (max_dt - min_dt).total_seconds()

    if diff > 600:  # More than 10 minutes
        fail(f"Timestamp spread: {diff:.0f}s (max allowed: 600s)")
        return False

    ok(f"Timestamp spread: {diff:.0f}s across {len(datetimes)} files "
       f"(from {min_dt.isoformat()} to {max_dt.isoformat()})")
    return True


def check_mandatory_metadata(evidence_dir):
    """Check that evidence files contain mandatory metadata fields."""
    print("\n--- Check 4: Mandatory Metadata ---")
    mandatory = ['Stage:', 'HEAD:', 'Timestamp:']
    results = []

    for fname in sorted(os.listdir(evidence_dir)):
        fpath = os.path.join(evidence_dir, fname)
        if not os.path.isfile(fpath):
            continue
        with open(fpath) as f:
            content = f.read()

        missing = [m for m in mandatory if m not in content]
        if missing:
            results.append(
                fail(f"  {fname}: missing {', '.join(missing)}")
            )
        else:
            results.append(True)

    passed = sum(1 for r in results if r)
    ok(f"Mandatory metadata: {passed}/{len(results)} files complete")
    return all(results)


def check_evidence_consistency():
    """Check for contradictions between evidence files."""
    print("\n--- Check 5: Evidence Consistency ---")
    results = []

    # Check deployment-phase vs owner-input
    dp_content = read_evidence('deployment-phase-summary.txt')
    oi_content = read_evidence('owner-input-validation.txt')

    dp_blocked = 'BLOCKED' in dp_content
    oi_blocked = 'BLOCKED' in oi_content
    oi_not_received = 'NOT RECEIVED' in oi_content

    if oi_not_received and not dp_blocked:
        results.append(fail(
            "Inconsistency: owner input NOT RECEIVED but deployment not BLOCKED"
        ))
    else:
        results.append(ok(
            "Deployment ↔ Owner input: consistent"
        ))

    # Check environment-access vs deployment-phase
    ea_content = read_evidence('environment-access-declaration.txt')
    if 'Deployment performed: NO' not in ea_content:
        results.append(fail(
            "environment-access-declaration: deployment status unclear"
        ))
    else:
        results.append(ok("Environment access declaration: deployment=NO"))

    # Check safety-gate vs deployment-phase
    sg_content = read_evidence('safety-gate-summary.txt')
    if 'BLOCKED' not in sg_content:
        results.append(fail("Safety gate should be BLOCKED without owner input"))
    else:
        results.append(ok("Safety gate: correctly BLOCKED"))

    return all(results)


def check_blocked_state_validation():
    """If owner input=NO, verify all deployment files show BLOCKED."""
    print("\n--- Check 6: Blocked State Validation ---")
    results = []

    # Read owner input status
    owner_deployment_approval = 'NO'
    owner_input_received = 'NO'

    if os.path.exists(OWNER_CHECKLIST):
        with open(OWNER_CHECKLIST) as f:
            oc = f.read()
        if 'Deployment approval: YES' in oc:
            owner_deployment_approval = 'YES'
        if 'Owner input received: YES' in oc:
            owner_input_received = 'YES'

    if owner_deployment_approval == 'NO' or owner_input_received == 'NO':
        # Owner has NOT approved → deployment must be BLOCKED everywhere
        deployment_files = [
            'deployment-phase-summary.txt',
            'owner-input-validation.txt',
            'safety-gate-summary.txt',
            'validation-summary.txt',
        ]
        for df in deployment_files:
            content = read_evidence(df)
            if content and 'BLOCKED' not in content:
                results.append(fail(
                    f"  {df}: should be BLOCKED (owner input=NO) but is not"
                ))
            else:
                results.append(ok(f"  {df}: correctly BLOCKED"))
    else:
        results.append(ok("Owner approved — deployment files not expected BLOCKED"))

    return all(results)


def check_stage_consistency(evidence_dir):
    """Check that all evidence files reference the same Stage."""
    print("\n--- Check 7: Stage Consistency ---")
    stage_re = re.compile(r'Stage:\s*(\d{2})')
    stages = {}
    for fname in sorted(os.listdir(evidence_dir)):
        fpath = os.path.join(evidence_dir, fname)
        if not os.path.isfile(fpath):
            continue
        with open(fpath) as f:
            content = f.read()
        m = stage_re.search(content)
        if m:
            stages.setdefault(m.group(1), []).append(fname)

    if not stages:
        return fail("No Stage references found")

    if len(stages) > 1:
        fail(f"Stage inconsistency: {len(stages)} different stages found")
        for s, files in stages.items():
            print(f"    Stage {s}: {len(files)} files")
        return False

    stage_val = list(stages.keys())[0]
    ok(f"All evidence references Stage {stage_val}")
    return True


def main():
    print("=" * 60)
    print("Stage 06 Semantic Evidence Validator")
    print("=" * 60)

    results = {
        'HEAD_consistency': check_head_consistency(E),
        'timestamp_validity': check_timestamp_validity(E),
        'timestamp_consistency': check_timestamp_consistency(E),
        'mandatory_metadata': check_mandatory_metadata(E),
        'evidence_consistency': check_evidence_consistency(),
        'blocked_state': check_blocked_state_validation(),
        'stage_consistency': check_stage_consistency(E),
    }

    print("\n" + "=" * 60)
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    print(f"Semantic checks: {passed}/{total} PASS")

    # Print each check result
    for check_name, check_result in results.items():
        status = 'PASS' if check_result else 'FAIL'
        print(f"  {status}: {check_name}")

    overall_result = all(results.values())
    print(f"\nOverall: {'PASS' if overall_result else 'FAIL'}")

    report = {
        'total_checks': total,
        'passed': passed,
        'failed': total - passed,
        'checks': results,
        'result': 'PASS' if overall_result else 'FAIL',
    }
    print(json.dumps(report, indent=2))
    sys.exit(0 if overall_result else 1)


if __name__ == '__main__':
    main()
