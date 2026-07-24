#!/usr/bin/env python3
"""Stage 06 Hiddify Rollback Plan Generator — plan_only mode."""
import sys, os, json
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    ts = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    print("=" * 60)
    print("Hiddify Rollback Plan — PLAN ONLY (no execution)")
    print("=" * 60)

    plan = {
        'timestamp': ts,
        'mode': 'plan_only',
        'deployment_blocked': True,
        'steps': [
            {'order': 1, 'action': 'Stop Hiddify service', 'command': 'systemctl stop hiddify-panel'},
            {'order': 2, 'action': 'Disable systemd unit', 'command': 'systemctl disable hiddify-panel'},
            {'order': 3, 'action': 'Stop Docker container', 'command': 'docker compose down'},
            {'order': 4, 'action': 'Restore previous configs', 'command': 'Restore from backup dir'},
            {'order': 5, 'action': 'Restore reverse proxy config', 'command': 'Restore nginx/haproxy config'},
            {'order': 6, 'action': 'Restore firewall rules', 'command': 'Restore iptables/nftables backup'},
            {'order': 7, 'action': 'Restore routing', 'command': 'Restore routing table backup'},
            {'order': 8, 'action': 'Remove temporary DNS artifacts', 'command': 'Clean DNS config'},
            {'order': 9, 'action': 'Restore systemd units', 'command': 'daemon-reload + enable original units'},
            {'order': 10, 'action': 'Restore from backup', 'command': 'Restore /opt/hiddify from backup'},
            {'order': 11, 'action': 'Verify original services', 'command': 'systemctl status <services>'},
            {'order': 12, 'action': 'Record rollback results', 'command': 'Log to evidence'},
        ],
        'prerequisites': [
            'Backup must exist before rollback',
            'Rollback approval from Owner',
            'Maintenance window active',
            'No production traffic on lab',
        ]
    }

    for step in plan['steps']:
        print(f"  Step {step['order']:2d}: {step['action']}")
        print(f"          {step['command']}")

    print(f"\nRollback plan generated: {len(plan['steps'])} steps")
    print("Status: PLAN_ONLY — NO EXECUTION")
    print(json.dumps(plan, indent=2))
    sys.exit(0)

if __name__ == '__main__':
    main()
