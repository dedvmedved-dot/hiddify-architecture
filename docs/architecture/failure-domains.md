# Failure Domains

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Domain Identification

| Domain | Components | Failure Impact | Recovery | Status |
|--------|-----------|----------------|----------|--------|
| FD-01 | Router (MikroTik) | Total service loss | Manual restore from backup | Single point of failure |
| FD-02 | VPS1 (RU egress) | RU traffic blocked | Failover behavior TO BE DECIDED | Single instance |
| FD-03 | VPS3 (INT egress) | INT traffic blocked | Failover behavior TO BE DECIDED | Single instance |
| FD-04 | VPS1 tunnel | RU path unavailable | Tunnel re-establishment | Auto-recovery expected |
| FD-05 | VPS3 tunnel | INT path unavailable | Tunnel re-establishment | Auto-recovery expected |
| FD-06 | ISP uplink | All external traffic blocked | ISP-dependent | External dependency |
| FD-07 | VPS1 provider | RU egress unavailable | Provider-dependent | External dependency |
| FD-08 | VPS3 provider | INT egress unavailable | Provider-dependent | External dependency |
| FD-09 | DNS resolver (RU) | RU DNS unavailable | Fallback resolver | TO BE CONFIGURED |
| FD-10 | DNS resolver (INT) | INT DNS unavailable | Fallback resolver | TO BE CONFIGURED |

## Critical Single Points of Failure

1. **Router:** Single hardware instance. Mitigation: configuration backup (FR-050), documented restore (FR-054)
2. **VPS1:** Single RU egress. Mitigation: failover behavior (TO BE DECIDED)
3. **VPS3:** Single INT egress. Mitigation: failover behavior (TO BE DECIDED)

## Failure Mode Decision Required

**OQ-013:** Fail-open vs fail-closed for egress failure — OWNER DECISION REQUIRED

| Mode | Behavior | Risk |
|------|----------|------|
| Fail-open | Traffic flows through default ISP route | Traffic leakage outside egress policy |
| Fail-closed | Traffic blocked until egress restored | Service unavailability |
