# Physical Architecture

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Physical Components

| Component | Role | Location | Specs | Status |
|-----------|------|----------|-------|--------|
| Router | Traffic classification + tunnel endpoint | Owner premises | <MIKROTIK_MODEL>, <ROUTEROS_VERSION>, <MIKROTIK_CPU>, <MIKROTIK_RAM>, <MIKROTIK_STORAGE> | UNKNOWN |
| VPS1 | Russian egress node | <VPS1_REGION>, <VPS1_COUNTRY> | <VPS1_OS>, <VPS1_VCPU>, <VPS1_RAM>, <VPS1_DISK> | UNKNOWN |
| VPS3 | International egress node | <VPS3_REGION>, <VPS3_COUNTRY> | <VPS3_OS>, <VPS3_VCPU>, <VPS3_RAM>, <VPS3_DISK> | UNKNOWN |

## Network Connectivity

| Connection | Type | Bandwidth | Status |
|------------|------|-----------|--------|
| Router ↔ ISP | WAN | UNKNOWN | UNKNOWN |
| Router ↔ VPS1 | Tunnel over internet | UNKNOWN | UNKNOWN |
| Router ↔ VPS3 | Tunnel over internet | UNKNOWN | UNKNOWN |
| Router ↔ LAN | Internal | UNKNOWN | UNKNOWN |
| VPS1 ↔ Internet | Public NIC | UNKNOWN | UNKNOWN |
| VPS3 ↔ Internet | Public NIC | UNKNOWN | UNKNOWN |

## Addressing (Sanitized)

| Network | CIDR | Purpose | Status |
|---------|------|---------|--------|
| LAN | <INTERNAL_SUBNET_A> | Client network | UNKNOWN |
| Router WAN | <ROUTER_WAN_IP> | ISP uplink | UNKNOWN |
| VPS1 public | <VPS1_PUBLIC_IP> | RU egress | UNKNOWN |
| VPS3 public | <VPS3_PUBLIC_IP> | INT egress | UNKNOWN |
| Tunnel subnet RU | <TUNNEL_SUBNET_RU> | Router-VPS1 tunnel | TO BE ALLOCATED |
| Tunnel subnet INT | <TUNNEL_SUBNET_INT> | Router-VPS3 tunnel | TO BE ALLOCATED |
| Management | <MGMT_SUBNET> | Administrative access | TO BE ALLOCATED |

## Deployment Model

All components are single-instance in the initial architecture.
High availability is addressed conceptually but not deployed in initial phase.

Redundancy options for future stages:

- Secondary VPS per egress path
- Router failover (if hardware supports)
- Tunnel failover to alternate endpoint
