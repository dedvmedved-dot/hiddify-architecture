#!/usr/bin/env python3
"""Stage 06 Safety Gate — deployment blocked without owner approval."""
import sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    owner_file = os.path.join(ROOT, 'stages/stage-06-controlled-lab-deployment/owner-input-checklist.md')
    deployment_approved = os.environ.get('STAGE06_LAB_DEPLOYMENT_APPROVED', 'NO')
    
    # Default: deployment is BLOCKED
    if deployment_approved != 'YES':
        print("SAFETY GATE: BLOCKED — STAGE06_LAB_DEPLOYMENT_APPROVED is not YES")
        print("Deployment requires: export STAGE06_LAB_DEPLOYMENT_APPROVED=YES")
        sys.exit(1)
    
    # Check owner input
    if os.path.exists(owner_file):
        with open(owner_file) as f:
            content = f.read()
        if 'Deployment approval: YES' not in content:
            print("SAFETY GATE: BLOCKED — Owner deployment approval not YES")
            sys.exit(1)
        if 'NOT production: YES' not in content:
            print("SAFETY GATE: BLOCKED — Environment not confirmed as non-production")
            sys.exit(1)
    
    print("SAFETY GATE: PASS — Deployment authorized for LAB environment only")
    sys.exit(0)

if __name__ == '__main__':
    main()
