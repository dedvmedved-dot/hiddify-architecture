# Stage 04 Traceability

**Status:** DRAFT — Stage 04 OFFLINE SKELETON

| Req ID | Arch Doc | ADR | Stage 03 Design | Stage 04 Artifact | Test ID | Acceptance | Status |
|--------|----------|-----|-----------------|-------------------|---------|------------|--------|
| FR-001 | logical-architecture | ADR-003 | deployment-sequence | config.example.yml | S04-UT-003 | Schema validates | SKELETON |
| FR-010 | routing-architecture | ADR-003 | deployment-sequence | config.example.yml | S04-UT-001 | Config loads | SKELETON |
| FR-020 | vpn-architecture | ADR-002 | deployment-sequence | config.example.yml | S04-UT-001 | Tunnel params present | SKELETON |
| FR-030 | dns-architecture | ADR-004 | deployment-sequence | config.example.yml | S04-UT-003 | DNS placeholders | SKELETON |
| SEC-008 | vpn-architecture | ADR-002 | deployment-sequence | safety_guard.py | S04-UT-013 | Forbidden scan | VALIDATED |
| SEC-005 | secrets-handling-design | ADR-005 | secrets-inventory | safety_guard.py | S04-UT-012 | Private key detected | VALIDATED |
| SEC-010 | security-architecture | ADR-005 | deployment-sequence | config-schema.json | S04-UT-008 | Prod mode blocked | VALIDATED |
| CON-007 | constraints-architecture | ADR-005 | secrets-inventory | safety_guard.py | S04-UT-011 | Secret detected | VALIDATED |
| OPS-010 | recovery-concept | ADR-009 | rollback-strategy | rollback-model.example.yml | S04-IT-002 | Rollback model present | SKELETON |
| NFR-001 | physical-architecture | ADR-009 | implementation-roadmap | config-schema.json | S04-UT-006 | Required params checked | SKELETON |
