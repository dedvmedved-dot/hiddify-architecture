# Smoke Test Plan

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Purpose

Quick validation after each deployment step to confirm basic functionality
before proceeding to the next step.

## Smoke Test Suite

### ST-01 — Administrative Access

- **Test:** SSH to router, VPS1, VPS3
- **Expected:** Connection succeeds with key authentication
- **Phase:** Post Phase 1, 2

### ST-02 — Basic Connectivity

- **Test:** Ping from router to VPS1, VPS3 public IPs
- **Expected:** ICMP response
- **Phase:** Post Phase 2

### ST-03 — Tunnel Establishment

- **Test:** Ping through tunnel (router ↔ VPS)
- **Expected:** ICMP response through tunnel interface
- **Phase:** Post Phase 3

### ST-04 — DNS Resolution

- **Test:** DNS query for known domain from LAN client
- **Expected:** Resolution succeeds; response from correct egress resolver
- **Phase:** Post Phase 4

### ST-05 — RU Egress

- **Test:** HTTP request to RU-classified destination from LAN
- **Expected:** Connection succeeds; source IP is VPS1 public IP
- **Phase:** Post Phase 5

### ST-06 — INT Egress

- **Test:** HTTP request to INT-classified destination from LAN
- **Expected:** Connection succeeds; source IP is VPS3 public IP
- **Phase:** Post Phase 5

### ST-07 — Default Traffic

- **Test:** Traffic to unclassified destination
- **Expected:** Routed per default policy (TO BE DECIDED)
- **Phase:** Post Phase 5

### ST-08 — Health Checks

- **Test:** Monitoring system reports all components healthy
- **Expected:** All health checks green
- **Phase:** Post Phase 6

## Failure Response

Any smoke test failure:

1. Do NOT proceed to next step
2. Diagnose failure
3. Fix or rollback the current step
4. Re-run smoke tests for current and previous steps
