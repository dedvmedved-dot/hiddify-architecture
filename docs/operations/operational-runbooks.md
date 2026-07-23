# Operational Runbooks

**Status:** DRAFT — OWNER REVIEW REQUIRED

## RB-01 — Daily Health Check

1. Verify all tunnel interfaces are up
2. Check monitoring dashboard for alerts
3. Review system logs for errors
4. Verify DNS resolution through each egress
5. Check backup status (last successful backup)

## RB-02 — Tunnel Status Check

1. SSH to router
2. Run: `/interface print where name~"tun"`
3. Verify status = "R" (running) for all tunnel interfaces
4. Ping through each tunnel: `/ping <remote-tunnel-ip> count=3`
5. If tunnel is down, see RB-05

## RB-03 — DNS Verification

1. From LAN client: `nslookup <RU-test-domain>`
2. From LAN client: `nslookup <INT-test-domain>`
3. Verify responses come from correct resolver
4. Run DNS leak test: capture on WAN interface, verify no DNS traffic

## RB-04 — Backup Execution

1. SSH to router
2. Run: `/export file=backup-$(date +%Y%m%d)`
3. Download backup file
4. Verify backup integrity (checksum)
5. Store in backup location
6. Repeat for VPS1, VPS3 configurations

## RB-05 — Tunnel Recovery

1. Identify failed tunnel (RU or INT)
2. Check both endpoints:
   - Router: `/interface print`
   - VPS: `wg show` or `ipsec status`
3. Restart tunnel interface
4. If not restored, verify:
   - Public IPs reachable
   - Keys match on both endpoints
   - Firewall rules allow tunnel traffic
5. Escalate if not resolved within 15 minutes

## RB-06 — Adding Traffic Category

1. Receive new category from Owner
2. Update address list on router
3. Add policy routing rule
4. Test routing for new category
5. Update documentation
6. Commit sanitized config to Git

## RB-07 — Certificate Renewal

1. Check certificate expiry dates (monitoring should alert)
2. Generate new certificate/key pair
3. Deploy to affected component
4. Restart affected service
5. Verify service functionality
6. Document renewal
