# VPN Architecture

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Overview

VPN/Tunnel layer provides encrypted transport between the classification
point (Router) and egress nodes (VPS1, VPS3).

## Technology Candidates

| Candidate | Strengths | Weaknesses | RouterOS Support | Recommendation |
|-----------|-----------|------------|------------------|----------------|
| WireGuard | High performance, simple config, kernel-level | No built-in PKI, static keys | Yes (v7+) | Primary candidate |
| OpenVPN | Mature, flexible, PKI support | Higher overhead, complex config | Yes | Fallback candidate |
| IPsec/IKEv2 | Standards-based, hardware offload | Complex, NAT issues | Yes | Evaluate if hardware offload available |

## Architecture Decision

**ADR-002** addresses VPN technology selection. See `docs/decisions/ADR-002-vpn-technology.md`.

Current status: All candidates under evaluation. Final selection requires:

1. RouterOS version verification (OQ-002)
2. Router hardware capabilities (OQ-003)
3. ISP filtering assessment (CON-022)
4. VPS OS compatibility (OQ-020, OQ-021)
5. Throughput requirements (OQ-008)

## Tunnel Topology

```text
Router ──── WireGuard/OpenVPN/IPsec ──── VPS1 (RU egress)
   │
   └─────── WireGuard/OpenVPN/IPsec ──── VPS3 (INT egress)
```

## Tunnel Configuration Template

```text
[Router]
Listen: <ROUTER_WAN_IP>
Peer VPS1: <VPS1_PUBLIC_IP>
Peer VPS3: <VPS3_PUBLIC_IP>
Tunnel subnet RU: <TUNNEL_RU_SUBNET>
Tunnel subnet INT: <TUNNEL_INT_SUBNET>

[VPS1]
Listen: <VPS1_PUBLIC_IP>
Peer Router: <ROUTER_WAN_IP>

[VPS3]
Listen: <VPS3_PUBLIC_IP>
Peer Router: <ROUTER_WAN_IP>
```

All IPs are placeholders pending Owner input.
