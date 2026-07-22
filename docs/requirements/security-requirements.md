# Security Requirements

**Status:** DRAFT — OWNER REVIEW REQUIRED

| ID | Requirement | Priority | Source | Status |
| -- | ----------- | -------- | ------ | ------ |
| SEC-001 | System shall implement least-privilege access to all components | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-002 | Administrative access shall use secure authentication (key-based or strong password) | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-003 | Administrative access shall be restricted to authorized networks or IPs | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-004 | Administrative access shall be logged with timestamps | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-005 | Secrets shall not be stored in Git repository | MUST | SECURITY.md | OWNER REVIEW REQUIRED |
| SEC-006 | Secrets shall use placeholders in all committed configurations | MUST | SECURITY.md | OWNER REVIEW REQUIRED |
| SEC-007 | Encryption keys shall have defined rotation procedures | SHOULD | Security policy | OWNER REVIEW REQUIRED |
| SEC-008 | All tunnel traffic shall be encrypted in transit | MUST | Initial concept | OWNER REVIEW REQUIRED |
| SEC-009 | Management-plane traffic shall be isolated from user-plane traffic | SHOULD | Security policy | OWNER REVIEW REQUIRED |
| SEC-010 | Firewall shall implement default-deny on all components | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-011 | Firewall rules shall be explicitly documented and audited | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-012 | Logging shall capture security-relevant events without sensitive payloads | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-013 | Configuration integrity shall be verifiable via checksums | MUST | Derived | OWNER REVIEW REQUIRED |
| SEC-014 | Security patches shall be applied according to defined policy | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-015 | Known vulnerabilities shall be tracked and remediated | SHOULD | Security policy | OWNER REVIEW REQUIRED |
| SEC-016 | Backups shall be protected from unauthorized access | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-017 | Incident response procedures shall be defined and documented | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-018 | Audit trail shall be preserved for all administrative actions | MUST | Security policy | OWNER REVIEW REQUIRED |
| SEC-019 | DNS queries shall not leak to unintended resolvers | MUST | Routing requirements | OWNER REVIEW REQUIRED |
| SEC-020 | User traffic shall not bypass egress policy through default route | MUST | Routing requirements | OWNER REVIEW REQUIRED |
| SEC-021 | System shall fail to a defined security state (fail-open vs fail-closed) | MUST | TO BE DECIDED | OWNER REVIEW REQUIRED |
| SEC-022 | Evidence shall be sanitized of credentials and internal identifiers before commit | MUST | SECURITY.md | OWNER REVIEW REQUIRED |
