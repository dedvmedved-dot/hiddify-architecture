# Network Segmentation

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Segment Overview

| Segment | CIDR | VLAN | Purpose | Firewall Zone |
|---------|------|------|---------|---------------|
| LAN | <INTERNAL_SUBNET_A> | <VLAN_ID> | Client devices | Internal |
| Router WAN | <ROUTER_WAN_SUBNET> | N/A | ISP uplink | External |
| Tunnel RU | <TUNNEL_RU_SUBNET> | N/A | Router-VPS1 tunnel | Tunnel |
| Tunnel INT | <TUNNEL_INT_SUBNET> | N/A | Router-VPS3 tunnel | Tunnel |
| VPS1 Public | <VPS1_PUBLIC_SUBNET> | N/A | RU egress | DMZ-Egress |
| VPS3 Public | <VPS3_PUBLIC_SUBNET> | N/A | INT egress | DMZ-Egress |
| Management | <MGMT_SUBNET> | <MGMT_VLAN> | Admin access | Management |

## Routing Between Segments

| From | To | Allowed | Condition |
|------|----|---------|-----------|
| LAN | Tunnel RU | Yes | Traffic classified for RU egress |
| LAN | Tunnel INT | Yes | Traffic classified for INT egress |
| LAN | Router WAN | Conditional | Default/unclassified traffic (TO BE DECIDED) |
| LAN | Management | No | Isolated |
| Management | Router | Yes | Authorized sources only |
| Management | VPS1 | Yes | Via tunnel or management path |
| Management | VPS3 | Yes | Via tunnel or management path |

## Segmentation Enforcement

- Router firewall enforces cross-segment rules
- VPS firewalls enforce DMZ-Egress rules
- Tunnel encryption prevents cross-segment leaks
- DNS queries follow segment egress path (DNS-001)
