# Lab Environment Contract

**Status:** Stage 05 — LAB ONLY, NO PRODUCTION

## Purpose
Define isolated laboratory environment for future deployment testing.

## Lab Classification
- environment: lab-example
- production_environment: false
- deployment_enabled: false
- remote_execution_enabled: false

## Host Roles
| Role | Count | Min CPU | Min RAM | Min Disk |
|------|-------|---------|---------|----------|
| traffic-classifier | 1 | 1 | 256MB | 128MB |
| ru-egress | 1 | 1 | 512MB | 10GB |
| int-egress | 1 | 1 | 512MB | 10GB |

## Network Zones (RFC 5737 only)
| Zone | CIDR |
|------|------|
| mgmt | 192.0.2.0/24 |
| tunnel-ru | 192.0.2.240/30 |
| tunnel-int | 198.51.100.240/30 |
| egress-ru | 198.51.100.0/24 |
| egress-int | 203.0.113.0/24 |

## DNS
- Domain: example.invalid
- Resolvers: 192.0.2.53, 198.51.100.53

## Prohibited
- Real IPs, production credentials, remote execution
- Deployment without explicit Stage 06 authorization
