# Traceability Matrix

**Status:** DRAFT — OWNER REVIEW REQUIRED

| Requirement ID | Type | Source | Stakeholder | Use case | Risk | Verification method | Status |
| -------------- | ---- | ------ | ----------- | -------- | ---- | -------------------- | ------ |
| ASM-001 | ASM | Architecture redesign required | STK-001 | UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | Owner confirmation |
| ASM-002 | ASM | Egress pairing incorrect | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | Owner confirmation |
| ASM-003 | ASM | Egress pairing incorrect | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | Owner confirmation |
| ASM-004 | ASM | Cannot deploy to uncontrolled infrastructure | STK-001 | N/A — stage-level requirement | RISK-01-019 | Owner confirmation | Owner confirmation |
| ASM-005 | ASM | Alternative router or approach needed | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | RouterOS version check |
| ASM-006 | ASM | Additional security controls needed | STK-001 | N/A — cross-cutting concern | RISK-01-011 | Access control audit | Router config review |
| ASM-007 | ASM | External monitoring needed | STK-001 | UC-007 | RISK-01-013 | Monitoring check in later stage | Infrastructure review |
| ASM-008 | ASM | Cannot implement backup | STK-001 | UC-008 | RISK-01-014 | Backup/restore test in later stage | Owner confirmation |
| ASM-009 | ASM | External DNS resolver needed | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | RouterOS version check |
| ASM-010 | ASM | Alternative health-check method needed | STK-001 | UC-007 | RISK-01-013 | Monitoring check in later stage | Network test |
| CON-001 | CON | RouterOS-specific features required | STK-001, STK-002 | UC-001, UC-002, UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| CON-002 | CON | RU IP and jurisdiction required | STK-001, STK-002 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| CON-003 | CON | International IP required | STK-001, STK-002 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| CON-004 | CON | Technology evaluation required before adoption | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-019 | Log inspection and audit | CONFIRMED |
| CON-005 | CON | No implementation without approval | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-019 | Owner confirmation or infrastructure review | CONFIRMED |
| CON-006 | CON | Deployment gate | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-019 | Owner confirmation or infrastructure review | CONFIRMED |
| CON-007 | CON | Sanitization required for all configs | STK-001, STK-002 | N/A — governance requirement | RISK-01-011 | Secret scan | CONFIRMED |
| CON-008 | CON | Placeholder usage required | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-019 | Owner confirmation or infrastructure review | CONFIRMED |
| CON-009 | CON | Cannot self-approve stages | STK-001, STK-002 | N/A — governance requirement | RISK-01-019 | Log inspection and audit | CONFIRMED |
| CON-010 | CON | Rollback procedures required | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-019 | Log inspection and audit | CONFIRMED |
| DNS-001 | DNS | Routing requirements | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| DNS-002 | DNS | Security requirements | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| DNS-003 | DNS | Derived | STK-001 | UC-006 | RISK-01-015, RISK-01-016 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| DNS-004 | DNS | Derived | STK-001 | UC-006 | RISK-01-004 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| DNS-005 | DNS | Derived | STK-001 | UC-006 | RISK-01-004 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| DNS-006 | DNS | Security requirements | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| DNS-007 | DNS | TO BE DECIDED | STK-001 | UC-006 | RISK-01-003, RISK-01-012 | Tunnel connectivity test in later stage | OWNER REVIEW REQUIRED |
| DNS-008 | DNS | Operations requirements | STK-001 | UC-006 | RISK-01-004 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| DNS-009 | DNS | Monitoring requirements | STK-004 | UC-006 | RISK-01-004 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| FR-001 | FR | Initial concept | STK-001 | UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| FR-002 | FR | Derived | STK-001 | UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| FR-003 | FR | Derived | STK-001 | UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| FR-004 | FR | Derived | STK-001 | UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| FR-005 | FR | Derived | STK-001 | UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| FR-006 | FR | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| FR-007 | FR | Derived | STK-004 | UC-004 | RISK-01-019 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| FR-010 | FR | Initial concept | STK-001 | UC-001, UC-002, UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| FR-011 | FR | Initial concept | STK-001 | UC-001, UC-002, UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| FR-012 | FR | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| FR-013 | FR | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| FR-014 | FR | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| FR-015 | FR | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| FR-016 | FR | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| FR-017 | FR | Derived | STK-001 | N/A — stage-level requirement | RISK-01-019 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| FR-020 | FR | Initial concept | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| FR-021 | FR | Project governance | STK-001 | UC-001, UC-002 | RISK-01-003, RISK-01-012 | Tunnel connectivity test in later stage | OWNER REVIEW REQUIRED |
| FR-022 | FR | Derived | STK-004 | UC-007 | RISK-01-003, RISK-01-012 | Tunnel connectivity test in later stage | OWNER REVIEW REQUIRED |
| FR-030 | FR | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| FR-031 | FR | Derived | STK-001 | UC-006 | RISK-01-004 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| FR-032 | FR | Derived | STK-001 | UC-006 | RISK-01-015, RISK-01-016 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| FR-033 | FR | Derived | STK-001 | UC-006 | RISK-01-004 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| FR-034 | FR | Derived | STK-001 | UC-006 | RISK-01-004 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| FR-040 | FR | Derived | STK-004 | UC-007 | RISK-01-003, RISK-01-012 | Tunnel connectivity test in later stage | OWNER REVIEW REQUIRED |
| FR-041 | FR | Derived | STK-004 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| FR-042 | FR | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| FR-043 | FR | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| FR-044 | FR | Derived | STK-004 | UC-006 | RISK-01-004 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| FR-045 | FR | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| FR-046 | FR | Derived | STK-001 | N/A — stage-level requirement | RISK-01-001 | Performance test in later stage | OWNER REVIEW REQUIRED |
| FR-047 | FR | Derived | STK-001 | N/A — stage-level requirement | RISK-01-018 | Configuration comparison test | OWNER REVIEW REQUIRED |
| FR-048 | FR | Derived | STK-001 | UC-007 | RISK-01-013 | Monitoring check in later stage | OWNER REVIEW REQUIRED |
| FR-050 | FR | Derived | STK-001 | N/A — stage-level requirement | RISK-01-019 | Backup/restore test in later stage | OWNER REVIEW REQUIRED |
| FR-051 | FR | Security policy | STK-001 | N/A — stage-level requirement | RISK-01-019 | Backup/restore test in later stage | OWNER REVIEW REQUIRED |
| FR-052 | FR | Derived | STK-004 | UC-008 | RISK-01-014 | Backup/restore test in later stage | OWNER REVIEW REQUIRED |
| FR-053 | FR | Derived | STK-004 | UC-008 | RISK-01-014 | Backup/restore test in later stage | OWNER REVIEW REQUIRED |
| FR-054 | FR | Derived | STK-004 | UC-008 | RISK-01-014 | Backup/restore test in later stage | OWNER REVIEW REQUIRED |
| FR-055 | FR | Derived | STK-004 | UC-009 | RISK-01-014 | Rollback procedure test | OWNER REVIEW REQUIRED |
| FR-056 | FR | Derived | STK-004 | UC-009 | RISK-01-014 | Rollback procedure test | OWNER REVIEW REQUIRED |
| NFR-001 | NFR | Uptime percentage | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | UNKNOWN — OWNER DECISION REQUIRED |
| NFR-002 | NFR | Failover time | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | UNKNOWN — OWNER DECISION REQUIRED |
| NFR-010 | NFR | Classification latency | STK-001 | UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | UNKNOWN — OWNER DECISION REQUIRED |
| NFR-011 | NFR | Mbps per egress | STK-004 | UC-001, UC-002 | RISK-01-003, RISK-01-012 | Tunnel connectivity test in later stage | UNKNOWN — OWNER DECISION REQUIRED |
| NFR-012 | NFR | Concurrent sessions | STK-001 | UC-001, UC-002 | RISK-01-019 | Architecture review in later stage | UNKNOWN — OWNER DECISION REQUIRED |
| NFR-020 | NFR | CPU/RAM utilization | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | UNKNOWN — OWNER DECISION REQUIRED |
| NFR-021 | NFR | CPU/RAM/bandwidth | STK-001 | N/A — stage-level requirement | RISK-01-001 | Performance test in later stage | UNKNOWN — OWNER DECISION REQUIRED |
| NFR-030 | NFR | Recovery time | STK-001 | UC-005 | RISK-01-003, RISK-01-012 | Tunnel connectivity test in later stage | UNKNOWN — OWNER DECISION REQUIRED |
| NFR-031 | NFR | Failover time | STK-001 | UC-006 | RISK-01-004 | DNS leak test in later stage | UNKNOWN — OWNER DECISION REQUIRED |
| NFR-040 | NFR | 100% of changes | STK-001 | N/A — stage-level requirement | RISK-01-018 | Architecture review in later stage | MUST |
| NFR-041 | NFR | Evidence completeness | STK-001 | N/A — stage-level requirement | RISK-01-019 | Architecture review in later stage | MUST |
| NFR-050 | NFR | Documentation coverage | STK-001 | N/A — stage-level requirement | RISK-01-019 | Document inspection | MUST |
| NFR-051 | NFR | Tested procedures | STK-004 | UC-009 | RISK-01-014 | Rollback procedure test | SHOULD |
| NFR-060 | NFR | ADR per decision | STK-001 | N/A — stage-level requirement | RISK-01-019 | Architecture review in later stage | MUST |
| NFR-061 | NFR | Traceability matrix | STK-001 | N/A — stage-level requirement | RISK-01-019 | Architecture review in later stage | MUST |
| OPS-001 | OPS | Security requirements | STK-004 | N/A — cross-cutting concern | RISK-01-011 | Access control audit | OWNER REVIEW REQUIRED |
| OPS-002 | OPS | Derived | STK-001 | UC-007 | RISK-01-019 | Monitoring check in later stage | OWNER REVIEW REQUIRED |
| OPS-003 | OPS | Derived | STK-001 | UC-007 | RISK-01-019 | Monitoring check in later stage | OWNER REVIEW REQUIRED |
| OPS-004 | OPS | Monitoring requirements | STK-004 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| OPS-005 | OPS | Derived | STK-001 | UC-007 | RISK-01-013 | Monitoring check in later stage | OWNER REVIEW REQUIRED |
| OPS-006 | OPS | TO BE DECIDED | STK-001 | UC-007 | RISK-01-013 | Monitoring check in later stage | OWNER REVIEW REQUIRED |
| OPS-007 | OPS | Security requirements | STK-001 | N/A — stage-level requirement | RISK-01-018 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| OPS-008 | OPS | Project governance | STK-001 | N/A — stage-level requirement | RISK-01-018 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| OPS-009 | OPS | Derived | STK-001 | UC-011 | RISK-01-019 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| OPS-010 | OPS | Backup requirements | STK-004 | UC-008 | RISK-01-014 | Backup/restore test in later stage | OWNER REVIEW REQUIRED |
| OPS-011 | OPS | Backup requirements | STK-001 | N/A — stage-level requirement | RISK-01-014 | Rollback procedure test | OWNER REVIEW REQUIRED |
| OPS-012 | OPS | Backup requirements | STK-004 | UC-009 | RISK-01-014 | Rollback procedure test | OWNER REVIEW REQUIRED |
| OPS-013 | OPS | Security requirements | STK-001 | UC-010 | RISK-01-019 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| OPS-014 | OPS | Derived | STK-001 | N/A — stage-level requirement | RISK-01-001 | Performance test in later stage | OWNER REVIEW REQUIRED |
| OPS-015 | OPS | Derived | STK-004 | UC-007 | RISK-01-013 | Monitoring check in later stage | OWNER REVIEW REQUIRED |
| OPS-016 | OPS | Derived | STK-001 | N/A — stage-level requirement | RISK-01-008, RISK-01-010 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| OPS-017 | OPS | Derived | STK-004 | N/A — stage-level requirement | RISK-01-018 | Document inspection | OWNER REVIEW REQUIRED |
| RTE-001 | RTE | VPS1 | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | TO BE DECIDED |
| RTE-002 | RTE | VPS3 | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | TO BE DECIDED |
| RTE-003 | RTE | TO BE DECIDED | STK-001 | N/A — stage-level requirement | RISK-01-007 | Architecture review in later stage | TO BE DECIDED |
| RTE-004 | RTE | Local | STK-001 | N/A — stage-level requirement | RISK-01-019 | Architecture review in later stage | N/A |
| RTE-010 | RTE | Derived | STK-001 | UC-003 | RISK-01-015, RISK-01-016 | Routing policy test in later stage | OWNER REVIEW REQUIRED |
| RTE-011 | RTE | Derived | STK-001 | N/A — stage-level requirement | RISK-01-019 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| RTE-012 | RTE | Derived | STK-001 | N/A — stage-level requirement | RISK-01-019 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| RTE-013 | RTE | Initial concept | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| RTE-014 | RTE | Initial concept | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| RTE-015 | RTE | Derived | STK-001 | N/A — stage-level requirement | RISK-01-019 | Document inspection | OWNER REVIEW REQUIRED |
| RTE-016 | RTE | Derived | STK-001 | N/A — stage-level requirement | RISK-01-019 | Document inspection | OWNER REVIEW REQUIRED |
| RTE-017 | RTE | Security requirements | STK-001 | UC-005 | RISK-01-007 | Failover scenario test | OWNER REVIEW REQUIRED |
| RTE-018 | RTE | Derived | STK-001 | UC-001, UC-002 | RISK-01-019 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| RTE-019 | RTE | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| RTE-020 | RTE | Infrastructure | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| RTE-021 | RTE | TO BE DECIDED | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| RTE-022 | RTE | Audit requirements | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| RTE-023 | RTE | Security requirements | STK-001 | UC-004 | RISK-01-019 | Log inspection and audit | OWNER REVIEW REQUIRED |
| RTE-024 | RTE | Derived | STK-001 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| SEC-001 | SEC | Security policy | STK-001, STK-002 | N/A — cross-cutting concern | RISK-01-011 | Access control audit | OWNER REVIEW REQUIRED |
| SEC-002 | SEC | Security policy | STK-001, STK-002 | N/A — cross-cutting concern | RISK-01-011 | Access control audit | OWNER REVIEW REQUIRED |
| SEC-003 | SEC | Security policy | STK-001, STK-002 | N/A — cross-cutting concern | RISK-01-011 | Access control audit | OWNER REVIEW REQUIRED |
| SEC-004 | SEC | Security policy | STK-001, STK-002 | N/A — cross-cutting concern | RISK-01-011 | Access control audit | OWNER REVIEW REQUIRED |
| SEC-005 | SEC | SECURITY.md | STK-001, STK-002 | N/A — governance requirement | RISK-01-011 | Secret scan | OWNER REVIEW REQUIRED |
| SEC-006 | SEC | SECURITY.md | STK-001, STK-002 | N/A — governance requirement | RISK-01-011 | Secret scan | OWNER REVIEW REQUIRED |
| SEC-007 | SEC | Security policy | STK-001, STK-002 | UC-001, UC-002 | RISK-01-003, RISK-01-012 | Tunnel connectivity test in later stage | OWNER REVIEW REQUIRED |
| SEC-008 | SEC | Initial concept | STK-001, STK-002 | UC-001, UC-002 | RISK-01-003, RISK-01-012 | Tunnel connectivity test in later stage | OWNER REVIEW REQUIRED |
| SEC-009 | SEC | Security policy | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-019 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| SEC-010 | SEC | Security policy | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-019 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| SEC-011 | SEC | Security policy | STK-001, STK-002 | N/A — governance requirement | RISK-01-019 | Log inspection and audit | OWNER REVIEW REQUIRED |
| SEC-012 | SEC | Security policy | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-019 | Log inspection and audit | OWNER REVIEW REQUIRED |
| SEC-013 | SEC | Derived | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-019 | Checksum verification | OWNER REVIEW REQUIRED |
| SEC-014 | SEC | Security policy | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-002 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| SEC-015 | SEC | Security policy | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-019 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| SEC-016 | SEC | Security policy | STK-001, STK-002 | UC-008 | RISK-01-014 | Backup/restore test in later stage | OWNER REVIEW REQUIRED |
| SEC-017 | SEC | Security policy | STK-001, STK-002 | UC-010 | RISK-01-019 | Document inspection | OWNER REVIEW REQUIRED |
| SEC-018 | SEC | Security policy | STK-001, STK-002 | N/A — governance requirement | RISK-01-019 | Log inspection and audit | OWNER REVIEW REQUIRED |
| SEC-019 | SEC | Routing requirements | STK-001, STK-002 | UC-006 | RISK-01-004 | DNS leak test in later stage | OWNER REVIEW REQUIRED |
| SEC-020 | SEC | Routing requirements | STK-001, STK-002 | UC-001, UC-002, UC-003 | RISK-01-005, RISK-01-006 | Egress routing test in later stage | OWNER REVIEW REQUIRED |
| SEC-021 | SEC | TO BE DECIDED | STK-001, STK-002 | UC-005 | RISK-01-007 | Failover scenario test | OWNER REVIEW REQUIRED |
| SEC-022 | SEC | SECURITY.md | STK-001, STK-002 | N/A — stage-level requirement | RISK-01-011 | Architecture review in later stage | OWNER REVIEW REQUIRED |
| CON-020 | CON | RouterOS capabilities vary by version | STK-001 | N/A — infrastructure constraint | RISK-01-019 | Owner confirmation | UNKNOWN |
| CON-021 | CON | MikroTik model unknown | STK-001 | N/A — infrastructure constraint | RISK-01-019 | Owner confirmation | UNKNOWN |
| CON-022 | CON | Common ISP practice | STK-001 | N/A — infrastructure constraint | RISK-01-019 | Owner confirmation | UNKNOWN |
| CON-023 | CON | Provider-specific | STK-001 | N/A — infrastructure constraint | RISK-01-019 | Owner confirmation | UNKNOWN |
| CON-024 | CON | Market conditions | STK-001 | N/A — infrastructure constraint | RISK-01-019 | Owner confirmation | UNKNOWN |
| CON-025 | CON | Infrastructure-dependent | STK-001 | N/A — infrastructure constraint | RISK-01-019 | Owner confirmation | UNKNOWN |
| CON-026 | CON | ISP-dependent | STK-001 | N/A — infrastructure constraint | RISK-01-019 | Owner confirmation | UNKNOWN |
| CON-027 | CON | Jurisdiction-dependent | STK-001 | N/A — infrastructure constraint | RISK-01-019 | Owner confirmation | UNKNOWN |
| CON-028 | CON | Owner-dependent | STK-001 | N/A — infrastructure constraint | RISK-01-019 | Owner confirmation | UNKNOWN |
