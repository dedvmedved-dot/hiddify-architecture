# Maintenance Procedures

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Scheduled Maintenance

### Pre-Maintenance

1. Notify Owner and users (per maintenance window policy)
2. Create full configuration backup (all components)
3. Verify backup integrity
4. Review planned changes
5. Prepare rollback procedures

### During Maintenance

1. Execute changes per deployment sequence
2. After each step: verify smoke tests pass
3. Document as-deployed configuration
4. Monitor for unexpected behavior for 15 minutes post-change

### Post-Maintenance

1. Run full smoke test suite
2. Verify monitoring is green
3. Update documentation and runbooks
4. Commit sanitized configurations to Git
5. Notify Owner of completion

## Unscheduled Maintenance (Emergency)

1. Notify Owner immediately
2. Create emergency backup if possible
3. Execute fix
4. Verify with smoke tests
5. Document incident
6. Schedule root cause analysis

## OS Package Updates

### Router (RouterOS)

1. Check current version and release notes
2. Download update (do not install yet)
3. Create backup
4. Schedule maintenance window
5. Install update
6. Reboot if required
7. Verify all services

### VPS (Linux)

1. Check available updates: `apt list --upgradable`
2. Review changelogs for security patches
3. Create backup/snapshot
4. Apply updates: `apt upgrade`
5. Reboot if kernel updated
6. Verify services restart correctly

## Tunnel Key Rotation

1. Generate new key pair (outside Git)
2. Schedule maintenance window
3. Deploy new public key to remote endpoint
4. Update local endpoint with new key pair
5. Restart tunnel
6. Verify tunnel establishes
7. Remove old keys after verification
8. Document rotation
