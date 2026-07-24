# Acceptance Checklist

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Pre-Deployment Acceptance

- [ ] All blocking open questions resolved (OQ-001 to OQ-017)
- [ ] Router model and specs confirmed
- [ ] VPS access confirmed
- [ ] Traffic categories defined by Owner
- [ ] DNS resolver preferences confirmed
- [ ] Fail-open/fail-closed decision made
- [ ] Monitoring platform selected
- [ ] Alert channels configured
- [ ] Maintenance windows approved

## Phase Completion Acceptance

### Phase 1 — Router Baseline

- [ ] Administrative access restricted
- [ ] Firewall default-deny verified
- [ ] Configuration backup created
- [ ] Smoke test ST-01 passed

### Phase 2 — VPS Baseline

- [ ] VPS1 and VPS3 accessible
- [ ] OS hardened
- [ ] Firewall active
- [ ] Monitoring agent deployed
- [ ] Smoke test ST-02 passed

### Phase 3 — Tunnels

- [ ] RU tunnel active
- [ ] INT tunnel active
- [ ] Health checks passing
- [ ] Smoke test ST-03 passed

### Phase 4 — DNS

- [ ] RU DNS resolution correct
- [ ] INT DNS resolution correct
- [ ] DNS leak test passed
- [ ] Smoke test ST-04 passed

### Phase 5 — Routing

- [ ] RU traffic routed correctly
- [ ] INT traffic routed correctly
- [ ] Default traffic handled per policy
- [ ] No traffic leaks detected
- [ ] Smoke tests ST-05, ST-06, ST-07 passed

### Phase 6 — Final Validation

- [ ] All integration tests passed
- [ ] All smoke tests passed
- [ ] Monitoring green
- [ ] Runbooks updated
- [ ] Configurations committed to Git
- [ ] Owner acceptance received

## Owner Acceptance

- [ ] System meets defined requirements
- [ ] Documentation complete
- [ ] Rollback tested
- [ ] Operations team trained
- [ ] Stage 03 accepted

**Owner signature:** ________________  **Date:** ________________
