# ADR-006 — Trust Model

- **Status:** PROPOSED
- **Date:** 2026-07-22
- **Decision-maker:** ChatGPT

## Context

The architecture spans multiple trust domains: internal network, VPS nodes,
and public internet.

## Decision

Adopt a **Zero-Trust Network Architecture** approach:

1. No implicit trust between zones
2. All cross-zone communication explicitly authorized
3. Authentication required for all administrative access
4. Encryption required for all cross-zone data in transit
5. Each component assumes compromise of adjacent zones

## Trust Levels

| Zone | Trust | Authentication | Encryption |
|------|-------|----------------|------------|
| Management | Highest | Key-based + source IP | Required |
| Internal LAN | High | Implicit (physical) | Not required internally |
| Tunnel | Encrypted | VPN keys | Always |
| DMZ-Egress | Low | Tunnel auth only | Always (public side) |
| Internet | Zero | N/A | Always |

## Consequences

- No component trusts any other by default
- Firewall rules must be explicit allow lists
- Key management critical for tunnel security
- Administrative access requires strong authentication
