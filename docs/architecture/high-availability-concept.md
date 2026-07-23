# High Availability Concept

**Status:** DRAFT — OWNER REVIEW REQUIRED
**Phase:** Conceptual only — not deployed in initial architecture

## Current Architecture

The initial architecture is single-instance for all components:

- Single router (MikroTik)
- Single VPS per egress path

## HA Candidates for Future Stages

| Component | HA Approach | Prerequisites | Complexity |
|-----------|-------------|---------------|------------|
| Router | VRRP or second router | Second MikroTik device, shared config | Medium |
| VPS1 | Second VPS + tunnel failover | Additional VPS, tunnel switching logic | Medium |
| VPS3 | Second VPS + tunnel failover | Additional VPS, tunnel switching logic | Medium |
| DNS | Multiple resolvers per egress | Additional resolver endpoints | Low |

## Auto-Recovery (Initial Architecture)

- Tunnel auto-reconnection on drop (NFR-030)
- DNS failover to alternate resolver (NFR-031)
- Configuration backup enables manual restore

## Not in Scope for Initial Deployment

- Automatic VPS failover
- Router hardware redundancy
- Load balancing across egress nodes
