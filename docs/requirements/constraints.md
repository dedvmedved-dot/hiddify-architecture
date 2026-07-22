# Constraints

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Confirmed Constraints

| ID | Constraint | Source | Impact | Status |
| -- | ---------- | ------ | ------ | ------ |
| CON-001 | MikroTik is considered as router component for traffic classification | Initial concept | RouterOS-specific features required | OWNER REVIEW REQUIRED |
| CON-002 | VPS1 is considered as Russian egress node | Initial concept | RU IP and jurisdiction required | OWNER REVIEW REQUIRED |
| CON-003 | VPS3 is considered as international egress node | Initial concept | International IP required | OWNER REVIEW REQUIRED |
| CON-004 | Hiddify is a candidate technology, not approved | README.md | Technology evaluation required before adoption | CONFIRMED |
| CON-005 | Architecture is not approved | README.md | No implementation without approval | CONFIRMED |
| CON-006 | Production changes require Owner authorization | Project governance | Deployment gate | CONFIRMED |
| CON-007 | Secrets shall not be stored in Git | SECURITY.md | Sanitization required for all configs | CONFIRMED |
| CON-008 | Evidence shall be sanitized before commit | SECURITY.md | Placeholder usage required | CONFIRMED |
| CON-009 | Stage progression requires external audit by ChatGPT | CONTRIBUTING.md | Cannot self-approve stages | CONFIRMED |
| CON-010 | Technology choices shall be reversible and testable | Project governance | Rollback procedures required | CONFIRMED |

## Potential Constraints — UNKNOWN

| ID | Constraint | Why potentially applicable | Status |
| -- | ---------- | ------------------------- | ------ |
| CON-020 | RouterOS version may limit available features | RouterOS capabilities vary by version | UNKNOWN |
| CON-021 | Hardware performance may limit throughput or rule count | MikroTik model unknown | UNKNOWN |
| CON-022 | ISP may filter or throttle tunnel protocols | Common ISP practice | UNKNOWN |
| CON-023 | VPS provider may restrict tunnel types or bandwidth | Provider-specific | UNKNOWN |
| CON-024 | Public IPv4 availability may be limited | Market conditions | UNKNOWN |
| CON-025 | IPv6 availability may vary by provider | Infrastructure-dependent | UNKNOWN |
| CON-026 | CGNAT may prevent direct inbound connections | ISP-dependent | UNKNOWN |
| CON-027 | Legal or regulatory restrictions may apply | Jurisdiction-dependent | UNKNOWN |
| CON-028 | Budget constraints may limit VPS or bandwidth options | Owner-dependent | UNKNOWN |
