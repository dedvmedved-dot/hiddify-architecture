#!/usr/bin/env python3
"""Stage 04 Safety Guard — prevents production execution."""
import sys, os, re

FORBIDDEN = [
    r'terraform\s+apply', r'terraform\s+destroy',
    r'ansible-playbook(?!.*(--syntax-check|--check))',
    r'\bssh\b(?!-V|--version)', r'\bscp\b', r'\brsync\b.*:',
    r'kubectl\s+apply', r'helm\s+(install|upgrade)',
    r'systemctl\s+(start|stop|restart|enable)',
    r'iptables\s+-[ADIR]', r'nft\s+add',
    r'ip\s+(route|addr)\s+add', r'resolvconf',
    r'curl\s+.*https?://(?!github\.com)',
]

def scan_file(path):
    issues = []
    with open(path) as f:
        for i, line in enumerate(f, 1):
            for pat in FORBIDDEN:
                if re.search(pat, line, re.IGNORECASE):
                    issues.append(f"{path}:{i}: FORBIDDEN pattern: {pat}")
    return issues

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    all_issues = []
    for dirpath, _, filenames in os.walk(os.path.join(root, 'iac')):
        for fn in filenames:
            if fn.endswith(('.sh', '.yml', '.yaml', '.tf', '.py')):
                all_issues.extend(scan_file(os.path.join(dirpath, fn)))
    for dirpath, _, filenames in os.walk(os.path.join(root, 'automation')):
        for fn in filenames:
            if fn.endswith(('.sh', '.yml', '.yaml', '.tf', '.py')):
                all_issues.extend(scan_file(os.path.join(dirpath, fn)))
    if all_issues:
        for issue in all_issues:
            print(f"SAFETY VIOLATION: {issue}", file=sys.stderr)
        sys.exit(1)
    print("SAFETY GUARD: PASS — no forbidden commands found")
    sys.exit(0)

if __name__ == '__main__':
    main()
