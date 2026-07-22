# Parameter Catalogue

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Router Parameters

| ID | Parameter | Placeholder | Required | Source |
|----|-----------|-------------|----------|--------|
| PAR-R01 | Router management IP | <MIKROTIK_MANAGEMENT_IP> | YES | Owner |
| PAR-R02 | Router WAN IP | <ROUTER_WAN_IP> | YES | Owner |
| PAR-R03 | LAN subnet | <INTERNAL_SUBNET_A> | YES | Owner |
| PAR-R04 | RouterOS admin username | <ROUTER_USERNAME> | YES | Owner |
| PAR-R05 | SSH port (mgmt) | <ROUTER_SSH_PORT> | YES | Default: 22 |
| PAR-R06 | Winbox port (mgmt) | <ROUTER_WINBOX_PORT> | NO | Default: 8291 |

## Tunnel Parameters

| ID | Parameter | Placeholder | Required | Source |
|----|-----------|-------------|----------|--------|
| PAR-T01 | RU tunnel subnet | <TUNNEL_RU_SUBNET> | YES | TO BE ALLOCATED |
| PAR-T02 | INT tunnel subnet | <TUNNEL_INT_SUBNET> | YES | TO BE ALLOCATED |
| PAR-T03 | Router tunnel RU IP | <ROUTER_TUN_RU_IP> | YES | From PAR-T01 |
| PAR-T04 | VPS1 tunnel IP | <VPS1_TUN_IP> | YES | From PAR-T01 |
| PAR-T05 | Router tunnel INT IP | <ROUTER_TUN_INT_IP> | YES | From PAR-T02 |
| PAR-T06 | VPS3 tunnel IP | <VPS3_TUN_IP> | YES | From PAR-T02 |

## VPS Parameters

| ID | Parameter | Placeholder | Required | Source |
|----|-----------|-------------|----------|--------|
| PAR-V01 | VPS1 public IP | <VPS1_PUBLIC_IP> | YES | Owner |
| PAR-V02 | VPS3 public IP | <VPS3_PUBLIC_IP> | YES | Owner |
| PAR-V03 | VPS1 SSH port | <VPS1_SSH_PORT> | YES | Default: 22 |
| PAR-V04 | VPS3 SSH port | <VPS3_SSH_PORT> | YES | Default: 22 |
| PAR-V05 | VPS service username | <VPS_SERVICE_USER> | YES | TO BE CREATED |

## DNS Parameters

| ID | Parameter | Placeholder | Required | Source |
|----|-----------|-------------|----------|--------|
| PAR-D01 | RU upstream DNS | <DNS_RESOLVER_RU> | YES | Owner (OQ-023) |
| PAR-D02 | INT upstream DNS | <DNS_RESOLVER_INT> | YES | Owner (OQ-023) |
| PAR-D03 | Default upstream DNS | <DNS_RESOLVER_DEFAULT> | YES | Owner (OQ-023) |

## Monitoring Parameters

| ID | Parameter | Placeholder | Required | Source |
|----|-----------|-------------|----------|--------|
| PAR-M01 | Monitoring platform | <MONITORING_PLATFORM> | YES | Owner (OQ-026) |
| PAR-M02 | Alert channel | <ALERT_CHANNEL> | YES | Owner (OQ-027) |
