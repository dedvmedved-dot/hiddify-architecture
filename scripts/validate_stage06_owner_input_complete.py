#!/usr/bin/env python3
"""Stage 06 Owner Input Completeness Validator."""
import sys, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKLIST = os.path.join(ROOT, 'stages', 'stage-06-controlled-lab-deployment', 'owner-input-checklist.md')

REQUIRED_FIELDS = [
    'Router type/model', 'VPS count', 'SSH usernames',
    'Deployment approval', 'NOT production', 'No real users',
    'Lab environment identifier', 'Router management address',
    'VPS public IPs', 'Domain names', 'VPN port assignments',
    'Maintenance window', 'Rollback window',
]

def main():
    if not os.path.exists(CHECKLIST):
        print(json.dumps({'result': 'FAIL', 'reason': 'checklist missing'}))
        sys.exit(1)

    with open(CHECKLIST) as f:
        content = f.read()

    received_count = content.count('| YES')
    total_required = content.count('| YES |')

    # Count NO fields
    no_count = content.count('| NO |')

    found = sum(1 for f in REQUIRED_FIELDS if f in content)
    all_required = content.count('| YES | YES')  # fields marked YES in Required AND Received

    print("=" * 60)
    print("Stage 06 Owner Input Completeness Validator")
    print("=" * 60)
    print(f"  Required fields present: {found}/{len(REQUIRED_FIELDS)}")
    print(f"  Total YES in Required column: {total_required}")
    print(f"  Received YES: {received_count}")
    print(f"  Still NO: {no_count}")
    print(f"  Fully received (YES|YES): {all_required}")

    complete = all_required >= 20

    report = {
        'required_fields_in_doc': found,
        'total_required': total_required,
        'received_yes': received_count,
        'still_no': no_count,
        'fully_received': all_required,
        'owner_input_complete': complete,
        'result': 'PASS' if complete else 'BLOCKED — OWNER INPUT INCOMPLETE'
    }
    print(json.dumps(report, indent=2))
    sys.exit(0 if complete else 1)

if __name__ == '__main__':
    main()
