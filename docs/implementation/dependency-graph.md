# Deployment Dependency Graph

**Status:** DRAFT — OWNER REVIEW REQUIRED

```text
Phase 0 ──► Phase 1 (Router) ──► Phase 3a (RU Tunnel) ──┐
         │                                               │
         ├──► Phase 2a (VPS1) ──► Phase 3a (RU Tunnel) ──┤
         │                                               ├──► Phase 4 (DNS) ──► Phase 5 (Routing) ──► Phase 6 (Validation)
         ├──► Phase 2b (VPS3) ──► Phase 3b (INT Tunnel) ─┤
         │                                               │
         └──► (Owner data: traffic categories, DNS resolvers) ──────────┘
```

## Parallelization Opportunities

| Tasks | Can Run In Parallel |
|-------|---------------------|
| Phase 2a (VPS1) + Phase 2b (VPS3) | Yes — independent VPS instances |
| Phase 3a (RU Tunnel) + Phase 3b (INT Tunnel) | Yes — independent tunnels |
| Phase 1 (Router) → Phase 2a/2b | Router before VPS (VPS firewalls can allow router IP once known) |

## Critical Path

Phase 0 → Phase 1 → Phase 3 (both) → Phase 4 → Phase 5 → Phase 6

Estimated critical path duration: 5-6 days.

## Blocking Dependencies

| Dependency | Blocks | Owner Action Required |
|------------|--------|-----------------------|
| Router model/specs | Phase 1 | Provide inventory data (OQ-001 to OQ-005) |
| VPS access credentials | Phase 2 | Provide SSH access (OQ-020, OQ-021) |
| Traffic categories | Phase 5 | Define RU/INT traffic classes (OQ-010, OQ-011) |
| DNS resolver preferences | Phase 4 | Specify resolvers (OQ-023) |
| Fail-open/fail-closed decision | Phase 5 | Owner decision (OQ-013) |
