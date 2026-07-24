#!/usr/bin/env python3
"""Stage 06 Placeholder Validator — two modes: offline and deployment.

offline mode (--mode offline):
  exit 0: placeholders PRESENT, deployment BLOCKED — expected state
  Lists all detected placeholders.

deployment mode (--mode deployment):
  exit 1: if ANY placeholder remains — blocks real deployment
"""
import sys, os, re, json, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTOMATION = os.path.join(ROOT, 'automation', 'ansible')

PLACEHOLDER_PATTERNS = [
    ('CHANGE_ME', 'CHANGE_ME placeholder'),
    ('TODO', 'TODO placeholder'),
    ('REPLACE_ME', 'REPLACE_ME placeholder'),
    ('example.invalid', 'example.invalid domain — replace with real domain'),
    ('sub.example.invalid', 'subscription example domain'),
]

DOC_IP_PATTERNS = [
    (r'\b192\.0\.2\.\d{1,3}\b', 'TEST-NET-1 (192.0.2.0/24)'),
    (r'\b198\.51\.100\.\d{1,3}\b', 'TEST-NET-2 (198.51.100.0/24)'),
    (r'\b203\.0\.113\.\d{1,3}\b', 'TEST-NET-3 (203.0.113.0/24)'),
]


def scan_files(directory, report_ips=True):
    """Scan all YAML/YML/J2 files for placeholders."""
    findings = []
    scan_exts = ('.yml', '.yaml', '.j2', '.env')
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for fname in files:
            if not any(fname.endswith(ext) for ext in scan_exts):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath) as f:
                content = f.read()
            rel = os.path.relpath(fpath, ROOT)
            for pattern, desc in PLACEHOLDER_PATTERNS:
                if pattern in content:
                    findings.append({'file': rel, 'type': 'placeholder', 'detail': desc, 'value': pattern})
            if report_ips:
                for pattern, desc in DOC_IP_PATTERNS:
                    if re.search(pattern, content):
                        findings.append({'file': rel, 'type': 'doc_ip', 'detail': desc, 'value': pattern})
    return findings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['offline', 'deployment'], default='offline')
    args = parser.parse_args()

    findings = scan_files(AUTOMATION, report_ips=(args.mode == 'deployment'))

    if args.mode == 'offline':
        print("=" * 60)
        print("Stage 06 Placeholder Validator — OFFLINE MODE")
        print("=" * 60)
        if findings:
            print(f"\nPlaceholders found: {len(findings)}")
            for f_item in findings:
                print(f"  [{f_item['type']}] {f_item['file']}: {f_item['detail']}")
            print(f"\nOFFLINE MODE: PLACEHOLDERS PRESENT — DEPLOYMENT BLOCKED")
            print("This is the EXPECTED state. Replace all placeholders before deployment.")
        else:
            print("\nNo placeholders found — ready for deployment mode validation.")
        report = {
            'mode': 'offline',
            'placeholders_found': len(findings),
            'findings': findings,
            'deployment_blocked': len(findings) > 0,
            'result': 'PASS (offline)'
        }
        print(json.dumps(report, indent=2))
        sys.exit(0)

    elif args.mode == 'deployment':
        print("=" * 60)
        print("Stage 06 Placeholder Validator — DEPLOYMENT MODE")
        print("=" * 60)
        if findings:
            print(f"\nBLOCKING PLACEHOLDERS FOUND: {len(findings)}")
            for f_item in findings:
                print(f"  [{f_item['type']}] {f_item['file']}: {f_item['detail']}")
            print(f"\nDEPLOYMENT BLOCKED: {len(findings)} placeholder(s) must be resolved.")
            report = {
                'mode': 'deployment',
                'placeholders_found': len(findings),
                'findings': findings,
                'deployment_blocked': True,
                'result': 'FAIL (deployment blocked)'
            }
            print(json.dumps(report, indent=2))
            sys.exit(1)
        else:
            print("\nAll clear — no placeholders, no documentation IPs.")
            report = {
                'mode': 'deployment',
                'placeholders_found': 0,
                'deployment_blocked': False,
                'result': 'PASS (deployment ready)'
            }
            print(json.dumps(report, indent=2))
            sys.exit(0)


if __name__ == '__main__':
    main()
