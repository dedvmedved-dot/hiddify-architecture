# Disaster Recovery Runbooks

**Status:** DRAFT — OWNER REVIEW REQUIRED

## DR-01 — Router Failure

**Scenario:** Router hardware failure or bricked configuration.

**Recovery:**
1. Obtain replacement router (if hardware failure)
2. Install RouterOS (version from inventory)
3. Restore configuration from latest backup
4. Verify tunnel establishment (both egresses)
5. Verify routing policy
6. Verify DNS resolution
7. Execute smoke test suite
8. Estimated recovery time: 2-4 hours (with spare hardware)

## DR-02 — VPS1 (RU Egress) Failure

**Scenario:** VPS1 unreachable; RU egress unavailable.

**Recovery:**
1. Verify provider status (check provider dashboard)
2. Attempt SSH; if unreachable, contact provider
3. If provider outage: wait for restoration; execute failover policy
4. If VPS recoverable: restore from backup; re-establish tunnel
5. If VPS unrecoverable: provision new VPS; restore configuration
6. Verify RU egress functionality
7. Estimated recovery time: 1-4 hours (depending on provider)

## DR-03 — VPS3 (INT Egress) Failure

**Scenario:** VPS3 unreachable; INT egress unavailable.

**Recovery:** Same as DR-02 for VPS3.

## DR-04 — ISP Outage

**Scenario:** Router WAN connectivity lost.

**Recovery:**
1. Verify ISP status
2. If ISP outage: wait for restoration; local LAN remains functional
3. If router WAN interface issue: check physical connection; reboot interface
4. After restoration: verify tunnels re-establish; run smoke tests
5. Estimated recovery time: ISP-dependent

## DR-05 — DNS Failure

**Scenario:** DNS resolution failing for one or both egress paths.

**Recovery:**

1. Identify which resolver failed (RU or INT)
2. Check resolver service on affected VPS
3. Restart resolver service
4. If unresolved: switch to fallback resolver
5. Verify DNS resolution
6. Estimated recovery time: 5-15 minutes

## DR-06 — Tunnel Key Compromise

**Scenario:** Tunnel private key exposed or suspected compromised.

**Recovery:**

1. Immediately disable affected tunnel
2. Generate new key pair
3. Deploy new keys to both endpoints
4. Re-establish tunnel
5. Verify functionality
6. Document incident per SEC-017
7. Review key management procedures
