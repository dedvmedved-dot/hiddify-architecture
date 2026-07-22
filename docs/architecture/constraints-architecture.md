# Architecture Constraints

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Inherited from Stage 01

Refer to `docs/requirements/constraints.md` for the full constraint list (CON-001 to CON-028).

## Architecture-Specific Constraints

| ID | Constraint | Impact | Source |
|----|-----------|--------|--------|
| ARC-CON-01 | Single router — no hardware redundancy | All traffic flows through single device | Physical limitation |
| ARC-CON-02 | Single VPS per egress path | No automatic egress failover | Current infrastructure |
| ARC-CON-03 | RouterOS feature set unknown | May limit VPN and routing options | OQ-001, OQ-002 |
| ARC-CON-04 | VPS OS unknown | May limit software options | OQ-020, OQ-021 |
| ARC-CON-05 | ISP may filter tunnel protocols | Protocol selection must account for filtering | CON-022 |
| ARC-CON-06 | No production access for testing | Architecture validated through documentation only | Project governance |
| ARC-CON-07 | All configs must be sanitized in Git | Secrets managed externally | SEC-005, SEC-006 |
