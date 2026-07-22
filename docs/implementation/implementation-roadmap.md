# Implementation Roadmap

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Phase Overview

| Phase | Name | Duration | Dependencies | Deliverables |
|-------|------|----------|--------------|--------------|
| 0 | Pre-deployment verification | 1-2 days | Owner input | Inventory confirmed, requirements validated |
| 1 | Router baseline configuration | 1 day | Phase 0 | Firewall, management access, backup configured |
| 2 | VPS baseline configuration | 1 day | Phase 0 | OS hardening, firewall, SSH keys, monitoring agent |
| 3 | Tunnel establishment | 1 day | Phase 1, 2 | WireGuard/OpenVPN tunnels active and tested |
| 4 | DNS configuration | 0.5 day | Phase 3 | Per-egress DNS resolution verified |
| 5 | Routing policy deployment | 1 day | Phase 3, 4 | Traffic classification and routing active |
| 6 | Validation and smoke testing | 1 day | Phase 5 | All tests passed, monitoring confirmed |
| 7 | Documentation finalization | 0.5 day | Phase 6 | Runbooks updated with actual values |

Total estimated: 6-7 days (sequential, single administrator).

## Milestones

| Milestone | Phase | Success Criteria |
|-----------|-------|------------------|
| M1 — Infrastructure Ready | Phase 2 | All nodes accessible, firewalled, monitored |
| M2 — Connectivity Established | Phase 3 | Tunnels up, health checks pass |
| M3 — Routing Active | Phase 5 | Traffic classified and routed correctly |
| M4 — Production Ready | Phase 6 | All tests pass, runbooks complete |

## Dependencies

See `docs/implementation/dependency-graph.md` for detailed dependency map.
