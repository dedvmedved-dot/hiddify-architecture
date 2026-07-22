# Risk Register — Stage 01

**Status:** DRAFT — OWNER REVIEW REQUIRED

| Risk ID | Description | Cause | Consequence | Likelihood | Impact | Rating | Mitigation candidate | Owner decision | Status |
| ------- | ----------- | ----- | ----------- | ---------- | ------ | ------ | -------------------- | -------------- | ------ |
| RISK-01-001 | Insufficient MikroTik hardware resources | Unknown model/specs | Cannot support required rules, tunnels, or throughput | HIGH | HIGH | HIGH | Model verification before architecture commitment | REQUIRED | UNMITIGATED |
| RISK-01-002 | Unsupported RouterOS version | Unknown version | Required features unavailable | MEDIUM | HIGH | HIGH | Version check; upgrade path evaluation | REQUIRED | UNMITIGATED |
| RISK-01-003 | Insufficient tunnel throughput | Router or VPS limits | Traffic congestion, user impact | MEDIUM | HIGH | HIGH | Throughput testing; capacity planning | REQUIRED | UNMITIGATED |
| RISK-01-004 | DNS leakage to unintended resolver | Incorrect routing/dns configuration | Privacy/security breach, egress policy bypass | MEDIUM | HIGH | HIGH | DNS leak testing; policy verification | REQUIRED | UNMITIGATED |
| RISK-01-005 | Traffic leakage through default ISP route | Routing misconfiguration | Traffic bypasses egress policy | MEDIUM | HIGH | HIGH | Routing policy validation; leak testing | REQUIRED | UNMITIGATED |
| RISK-01-006 | Asymmetric routing | Incorrect return path configuration | Broken sessions, performance issues | MEDIUM | MEDIUM | MEDIUM | Connection tracking; policy routing verification | REQUIRED | UNMITIGATED |
| RISK-01-007 | Single point of failure | Router or egress nodes single-instance | Total service loss on component failure | HIGH | HIGH | HIGH | Redundancy evaluation; failover design | REQUIRED | UNMITIGATED |
| RISK-01-008 | VPS provider outage | External dependency | Egress path unavailable | LOW | HIGH | MEDIUM | Multi-provider evaluation; failover planning | REQUIRED | UNMITIGATED |
| RISK-01-009 | Geographic or ISP blocking | External filtering | Tunnel establishment failure | LOW | MEDIUM | LOW | Protocol diversity; fallback mechanisms | OPTIONAL | UNMITIGATED |
| RISK-01-010 | VPS provider traffic limits exceeded | Unknown bandwidth caps | Throttling or additional charges | UNKNOWN | MEDIUM | UNKNOWN | Bandwidth monitoring; provider review | REQUIRED | UNMITIGATED |
| RISK-01-011 | Credential compromise | Weak access controls | Unauthorized infrastructure access | LOW | CRITICAL | HIGH | Key-based auth; access restriction; rotation | REQUIRED | UNMITIGATED |
| RISK-01-012 | Technology candidate unsupported | Hiddify or proxy platform limitations | Rearchitecture required | MEDIUM | HIGH | HIGH | Technology evaluation before commitment | REQUIRED | UNMITIGATED |
| RISK-01-013 | Incomplete monitoring | Missing metrics or alerts | Undetected failures or performance issues | MEDIUM | MEDIUM | MEDIUM | Comprehensive monitoring design; health checks | REQUIRED | UNMITIGATED |
| RISK-01-014 | Rollback failure | Untested or incomplete backup | Cannot recover from failed change | LOW | HIGH | MEDIUM | Backup testing; rollback procedures | REQUIRED | UNMITIGATED |
| RISK-01-015 | Incorrect domain/IP classification | Stale or incomplete address lists | Traffic misrouted to wrong egress | MEDIUM | MEDIUM | MEDIUM | Address list maintenance; validation | REQUIRED | UNMITIGATED |
| RISK-01-016 | Stale domain address lists | Dynamic IP changes | Classification rules outdated | MEDIUM | MEDIUM | MEDIUM | DNS-based address lists; periodic refresh | REQUIRED | UNMITIGATED |
| RISK-01-017 | IPv6 traffic bypass | IPv6 routing not controlled | Traffic leaks around egress policy | UNKNOWN | HIGH | UNKNOWN | IPv6 routing policy; disable if not required | REQUIRED | UNMITIGATED |
| RISK-01-018 | Configuration drift | Uncontrolled changes | Unexpected behavior, security gaps | MEDIUM | MEDIUM | MEDIUM | Configuration monitoring; drift detection | OPTIONAL | UNMITIGATED |
| RISK-01-019 | Insufficient Owner input | Lack of required decisions | Blocked architecture progression | HIGH | HIGH | HIGH | Structured question list; escalation process | REQUIRED | UNMITIGATED |
| RISK-01-020 | Legal or policy restrictions | Unknown regulatory constraints | Limited architecture options | UNKNOWN | HIGH | UNKNOWN | Legal review; jurisdictional analysis | REQUIRED | UNMITIGATED |
