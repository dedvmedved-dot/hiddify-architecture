# ADR-002 — VPN/Tunnel Technology

- **Status:** PROPOSED (pending Owner input)
- **Date:** 2026-07-22
- **Decision-maker:** ChatGPT + Owner

## Context

The architecture requires encrypted transport between the router and
egress nodes (VPS1, VPS3). Multiple VPN/tunnel technologies are candidates.

## Decision

Select **WireGuard** as the primary tunnel protocol, with **OpenVPN**
as the fallback option.

This decision is **conditional** on:

1. RouterOS version supports WireGuard (requires v7+)
2. ISP does not block WireGuard traffic
3. No regulatory or policy restrictions on WireGuard

## Alternatives Considered

| Alternative | Assessment |
|-------------|------------|
| WireGuard | Simple, high-performance, kernel-level, low overhead. Recommended. |
| OpenVPN | Mature, flexible, PKI support. Higher overhead. Good fallback. |
| IPsec/IKEv2 | Standards-based. More complex. Evaluate if hardware offload available. |
| Hiddify-managed | Platform-dependent. Evaluate after Hiddify decision. |

## Consequences

- WireGuard is stateless — auto-recovery on tunnel drop
- No built-in PKI — key rotation must be managed procedurally
- RouterOS v6 does not support WireGuard — upgrade may be required
- OpenVPN fallback provides compatibility with older RouterOS or restricted networks
