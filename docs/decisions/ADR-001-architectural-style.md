# ADR-001 — Architectural Style

- **Status:** PROPOSED
- **Date:** 2026-07-22
- **Decision-maker:** ChatGPT (external auditor approval pending)

## Context

The project requires a network access architecture with traffic classification,
multi-egress routing, and encrypted tunnels. The system spans a local router
and remote VPS nodes.

## Decision

Adopt a **Layered + Segmented** architectural style:

- **Layer 1:** Client (end-user devices)
- **Layer 2:** Classification (MikroTik router)
- **Layer 3:** Transport (encrypted tunnels)
- **Layer 4:** Egress (VPS nodes)
- **Layer 5:** Management (monitoring, backup, admin access)

Each layer has clear security boundaries and controlled communication paths.

## Alternatives Considered

| Alternative | Rejected Because |
|-------------|------------------|
| Monolithic (all on router) | No egress diversity; single point of failure |
| Mesh (all-to-all tunnels) | Unnecessary complexity for 2 egress nodes |
| Cloud-only (VPN service) | Owner infrastructure preferences; MikroTik already in place |

## Consequences

- Clear separation of concerns
- Each layer independently securable
- Future HA additions fit within layered model
- Requires documented interfaces between layers
