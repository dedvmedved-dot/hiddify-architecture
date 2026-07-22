# Functional Requirements

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Traffic Classification

| ID | Requirement | Priority | Source | Status |
| -- | ----------- | -------- | ------ | ------ |
| FR-001 | System shall classify traffic by destination IP address | MUST | Initial concept | OWNER REVIEW REQUIRED |
| FR-002 | System shall classify traffic by destination domain name | SHOULD | Derived | OWNER REVIEW REQUIRED |
| FR-003 | System shall maintain address lists for classification rules | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-004 | System shall classify traffic by protocol and port | COULD | Derived | OWNER REVIEW REQUIRED |
| FR-005 | System shall support explicit exception rules overriding classification | SHOULD | Derived | OWNER REVIEW REQUIRED |
| FR-006 | System shall define default route behavior for unclassified traffic | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-007 | System shall support manual policy overrides by authorized administrator | SHOULD | Derived | OWNER REVIEW REQUIRED |

## Egress Selection

| ID | Requirement | Priority | Source | Status |
| -- | ----------- | -------- | ------ | ------ |
| FR-010 | System shall route classified traffic through Russian egress (VPS1) | MUST | Initial concept | OWNER REVIEW REQUIRED |
| FR-011 | System shall route classified traffic through international egress (VPS3) | MUST | Initial concept | OWNER REVIEW REQUIRED |
| FR-012 | System shall define default egress for unclassified traffic | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-013 | System shall detect unreachable egress and execute fallback behavior | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-014 | System shall prevent asymmetric routing for stateful connections | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-015 | System shall preserve session persistence across egress selection | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-016 | System shall ensure return traffic follows the same egress path | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-017 | System shall enforce policy precedence when multiple rules match | MUST | Derived | OWNER REVIEW REQUIRED |

## Tunnel/Proxy Management

| ID | Requirement | Priority | Source | Status |
| -- | ----------- | -------- | ------ | ------ |
| FR-020 | System shall provide secure transport between router-side component and egress node | MUST | Initial concept | OWNER REVIEW REQUIRED |
| FR-021 | The transport mechanism shall be technology-neutral in requirements | MUST | Project governance | OWNER REVIEW REQUIRED |
| FR-022 | Tunnel state shall be monitored and reported | MUST | Derived | OWNER REVIEW REQUIRED |

## DNS

| ID | Requirement | Priority | Source | Status |
| -- | ----------- | -------- | ------ | ------ |
| FR-030 | System shall resolve DNS queries through resolver aligned with traffic egress | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-031 | System shall prevent DNS leakage to unintended resolver | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-032 | System shall support split DNS where different domains resolve via different paths | COULD | Derived | OWNER REVIEW REQUIRED |
| FR-033 | DNS fallback behavior shall be defined for resolver failure | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-034 | DNS caching shall be supported with configurable TTL | SHOULD | Derived | OWNER REVIEW REQUIRED |

## Monitoring

| ID | Requirement | Priority | Source | Status |
| -- | ----------- | -------- | ------ | ------ |
| FR-040 | System shall monitor tunnel state and report changes | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-041 | System shall monitor egress reachability via health checks | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-042 | System shall measure and report latency per egress path | SHOULD | Derived | OWNER REVIEW REQUIRED |
| FR-043 | System shall measure and report packet loss per egress path | SHOULD | Derived | OWNER REVIEW REQUIRED |
| FR-044 | System shall monitor DNS resolver availability | SHOULD | Derived | OWNER REVIEW REQUIRED |
| FR-045 | System shall detect routing policy misconfiguration | SHOULD | Derived | OWNER REVIEW REQUIRED |
| FR-046 | System shall report resource utilization (CPU, RAM, bandwidth) | SHOULD | Derived | OWNER REVIEW REQUIRED |
| FR-047 | System shall detect configuration drift from known baseline | COULD | Derived | OWNER REVIEW REQUIRED |
| FR-048 | System shall deliver alerts through configured channels | MUST | Derived | OWNER REVIEW REQUIRED |

## Backup and Rollback

| ID | Requirement | Priority | Source | Status |
| -- | ----------- | -------- | ------ | ------ |
| FR-050 | System shall support automated configuration export | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-051 | Exported configurations shall be sanitized before storage | MUST | Security policy | OWNER REVIEW REQUIRED |
| FR-052 | Backups shall be retained according to defined policy | SHOULD | Derived | OWNER REVIEW REQUIRED |
| FR-053 | Backup integrity shall be verifiable via checksums | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-054 | System shall support configuration restore from backup | MUST | Derived | OWNER REVIEW REQUIRED |
| FR-055 | Rollback shall be testable without affecting production | SHOULD | Derived | OWNER REVIEW REQUIRED |
| FR-056 | Rollback trigger conditions shall be defined | MUST | Derived | OWNER REVIEW REQUIRED |
