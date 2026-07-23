# Deployment Sequence

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Pre-Deployment Checklist

Before starting deployment, verify:

- [ ] Router model and RouterOS version confirmed (OQ-001, OQ-002)
- [ ] VPS1 and VPS3 accessible via SSH (OQ-020, OQ-021)
- [ ] All public IPs confirmed
- [ ] Administrative access credentials available
- [ ] Backup strategy agreed
- [ ] Maintenance window approved by Owner
- [ ] Rollback triggers defined

## Sequence

### Step 1 — Router Baseline (Phase 1)

1. Connect to router via management interface
2. Verify current configuration
3. Create configuration backup (export)
4. Configure administrative access restrictions
5. Configure firewall (default-deny with management allow)
6. Configure NTP for accurate logging
7. Test administrative access
8. Commit and backup

### Step 2 — VPS1 Baseline (Phase 2a)

1. SSH to VPS1
2. Update OS packages
3. Configure firewall (UFW/iptables/nftables)
4. Create service user
5. Deploy SSH authorized_keys
6. Install monitoring agent (TO BE DECIDED)
7. Test SSH access
8. Document as-deployed configuration

### Step 3 — VPS3 Baseline (Phase 2b)

Same as Step 2 for VPS3.

### Step 4 — RU Tunnel (Phase 3a)

1. Generate WireGuard/OpenVPN keys (outside Git)
2. Deploy tunnel configuration to router
3. Deploy tunnel configuration to VPS1
4. Start tunnel
5. Verify tunnel status (both endpoints)
6. Test ICMP through tunnel
7. Configure health check

### Step 5 — INT Tunnel (Phase 3b)

Same as Step 4 for VPS3.

### Step 6 — DNS Configuration (Phase 4)

1. Configure DNS forwarder on router
2. Configure per-egress DNS routing
3. Deploy DNS resolver on VPS1 (if Option B)
4. Deploy DNS resolver on VPS3 (if Option B)
5. Test DNS resolution from LAN through each egress
6. Test DNS leak prevention

### Step 7 — Routing Policy (Phase 5)

1. Deploy address lists (from Owner-provided data)
2. Configure policy routing rules
3. Test classification for each traffic category
4. Test default route behavior
5. Test session persistence
6. Verify no traffic leaks

### Step 8 — Validation (Phase 6)

1. Execute smoke tests (see smoke-test-plan.md)
2. Execute integration tests (see integration-test-plan.md)
3. Verify monitoring and alerts
4. Document as-deployed state
5. Update runbooks with actual values

## Rollback Points

After each step, a rollback point is established by saving the configuration
state. See `docs/implementation/rollback-strategy.md`.
