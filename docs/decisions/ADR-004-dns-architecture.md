# ADR-004 — DNS Architecture

- **Status:** PROPOSED (pending DNS-OQ-01 Owner decision)
- **Date:** 2026-07-22
- **Decision-maker:** ChatGPT + Owner

## Context

DNS queries must be resolved through the same egress path as subsequent
user traffic to prevent DNS leakage and maintain routing consistency.

## Decision

Adopt **Per-Egress DNS Resolution:**

1. Router forwards DNS queries based on traffic classification
2. RU-classified DNS queries routed through VPS1 tunnel
3. INT-classified DNS queries routed through VPS3 tunnel
4. DNS caching on router with per-egress separation
5. No DNS fallback to default ISP resolver

## Alternatives Considered

| Alternative | Rejected Because |
|-------------|------------------|
| Single resolver for all traffic | DNS leakage; inconsistent with routing policy |
| Client-configured DNS | Bypassable; no central control |
| DoH/DoT only | Adds complexity; TO BE EVALUATED separately |

## Consequences

- DNS queries follow same path as traffic (consistency)
- DNS leak prevention requires correct router configuration
- Each egress path needs a functioning DNS resolver
- DNS failure handling required per DNS-005, DNS-006
