# Rollback Strategy

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Rollback Philosophy

Every deployment step must be independently reversible. Rollback restores
the configuration to the state captured before that step.

## Step-Level Rollback

| Step | Rollback Method | Time Estimate |
|------|----------------|---------------|
| Router config change | Restore from backup export | 5-15 min |
| VPS config change | Restore from backup or revert file | 5-15 min |
| Tunnel establishment | Disable tunnel interface | 2 min |
| DNS configuration | Remove DNS routing rules | 5 min |
| Routing policy | Remove policy routes; restore default | 5 min |

## Full Rollback

Complete system rollback to pre-deployment state:

1. Disable routing policies
2. Disable tunnel interfaces
3. Remove tunnel configurations
4. Restore router to pre-deployment backup
5. Restore VPS to pre-deployment state (revert or re-image)
6. Verify baseline connectivity

Estimated full rollback time: 30-60 minutes.

## Rollback Triggers

Per FR-055, FR-056:

- Any step produces unexpected behavior
- Traffic leakage detected (traffic going through wrong egress)
- DNS leakage detected
- Performance degradation below acceptable threshold
- Security incident during deployment
- Owner requests rollback

## Rollback Governance

- Rollback decision: Network administrator or Owner
- Rollback execution: Network administrator
- Post-rollback verification: Smoke test suite
- Rollback documentation: Logged with timestamp and reason

## Rollback Testing

Before production deployment:
1. Execute rollback in test/lab environment (if available)
2. Verify rollback procedures are complete and correct
3. Time each rollback step for planning

If test environment unavailable:
1. Document procedures with exact commands
2. Owner acknowledges increased rollback risk
