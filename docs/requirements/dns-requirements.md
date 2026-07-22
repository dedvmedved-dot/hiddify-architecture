# DNS Requirements

**Status:** DRAFT — OWNER REVIEW REQUIRED

## DNS Objectives

Ensure DNS resolution is consistent with traffic routing policy, preventing leakage and maintaining availability.

## Key Decision Required

> Должны ли DNS-запросы для каждого traffic class выходить через тот же egress, что и последующий пользовательский трафик?

**Status:** OWNER DECISION REQUIRED

## Requirements

| ID | Requirement | Priority | Source | Status |
| -- | ----------- | -------- | ------ | ------ |
| DNS-001 | DNS resolver selection shall align with traffic egress policy | MUST | Routing requirements | OWNER REVIEW REQUIRED |
| DNS-002 | DNS queries shall not leak to unintended resolver through default route | MUST | Security requirements | OWNER REVIEW REQUIRED |
| DNS-003 | System shall support split DNS with configurable domain-to-resolver mapping | SHOULD | Derived | OWNER REVIEW REQUIRED |
| DNS-004 | DNS caching shall be supported with configurable TTL values | SHOULD | Derived | OWNER REVIEW REQUIRED |
| DNS-005 | DNS fallback behavior shall be defined for resolver failure | MUST | Derived | OWNER REVIEW REQUIRED |
| DNS-006 | DNS failure mode shall not cause traffic to bypass egress policy | MUST | Security requirements | OWNER REVIEW REQUIRED |
| DNS-007 | DNS resolver transport protocol shall be defined (UDP, TCP, DoT, DoH) | MUST | TO BE DECIDED | OWNER REVIEW REQUIRED |
| DNS-008 | DNS logging shall capture resolution events without query content where privacy-constrained | SHOULD | Operations requirements | OWNER REVIEW REQUIRED |
| DNS-009 | DNS resolver health shall be monitored and reported | SHOULD | Monitoring requirements | OWNER REVIEW REQUIRED |

## Open Questions

| ID | Question | Priority | Blocks |
| -- | -------- | -------- | ------ |
| DNS-OQ-01 | Should DNS use same egress path as subsequent traffic? | BLOCKING | DNS architecture, routing policy |
| DNS-OQ-02 | Which DNS resolvers should be used per egress? | HIGH | DNS configuration |
| DNS-OQ-03 | Is encrypted DNS (DoT/DoH) required? | MEDIUM | DNS transport selection |
| DNS-OQ-04 | Should client DNS queries be intercepted or configured? | HIGH | Client configuration |
| DNS-OQ-05 | What DNS caching strategy is preferred? | MEDIUM | DNS performance |
