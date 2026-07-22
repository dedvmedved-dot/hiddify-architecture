# Secrets Inventory

**Status:** DRAFT — PLACEHOLDERS ONLY — NO REAL SECRETS

## WARNING

This file contains PLACEHOLDERS ONLY. No real secrets, keys, tokens,
or credentials are stored in this repository.

## Router Credentials

| ID | Secret Type | Placeholder | Storage Location | Rotation |
|----|-------------|-------------|------------------|----------|
| SEC-R01 | RouterOS admin password | <ROUTER_ADMIN_PASSWORD> | External vault / env | 90 days |
| SEC-R02 | Router SSH private key | <ROUTER_SSH_PRIVATE_KEY> | External vault | 90 days |
| SEC-R03 | Router SSH public key | <ROUTER_SSH_PUBLIC_KEY> | Deployed to router | With private key |

## VPS Credentials

| ID | Secret Type | Placeholder | Storage Location | Rotation |
|----|-------------|-------------|------------------|----------|
| SEC-V01 | VPS1 SSH private key | <VPS1_SSH_PRIVATE_KEY> | External vault | 90 days |
| SEC-V02 | VPS1 SSH public key | <VPS1_SSH_PUBLIC_KEY> | Deployed to VPS1 | With private key |
| SEC-V03 | VPS3 SSH private key | <VPS3_SSH_PRIVATE_KEY> | External vault | 90 days |
| SEC-V04 | VPS3 SSH public key | <VPS3_SSH_PUBLIC_KEY> | Deployed to VPS3 | With private key |

## Tunnel Keys

| ID | Secret Type | Placeholder | Storage Location | Rotation |
|----|-------------|-------------|------------------|----------|
| SEC-T01 | Router↔VPS1 WireGuard private key | <WG_RU_ROUTER_PRIVKEY> | External vault | 90 days |
| SEC-T02 | Router↔VPS1 WireGuard preshared key | <WG_RU_PSK> | External vault | 90 days |
| SEC-T03 | Router↔VPS3 WireGuard private key | <WG_INT_ROUTER_PRIVKEY> | External vault | 90 days |
| SEC-T04 | Router↔VPS3 WireGuard preshared key | <WG_INT_PSK> | External vault | 90 days |

## Monitoring/Access Tokens

| ID | Secret Type | Placeholder | Storage Location | Rotation |
|----|-------------|-------------|------------------|----------|
| SEC-M01 | Monitoring API token | <MONITORING_API_TOKEN> | External vault | 30 days |
| SEC-M02 | Alert webhook URL | <ALERT_WEBHOOK_URL> | External vault | On change |

## Git Credentials

| ID | Secret Type | Placeholder | Storage Location | Rotation |
|----|-------------|-------------|------------------|----------|
| SEC-G01 | GitHub PAT | <GITHUB_PAT> | Git credential helper | Per policy |

## Access Control

- All secrets stored outside Git repository
- Access restricted to authorized administrators
- Rotation schedule defined in security requirements (SEC-007)
- Compromise response defined in incident response procedures
