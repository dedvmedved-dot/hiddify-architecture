# Certificate Architecture

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Scope

This document addresses TLS/SSL certificates for:

1. Administrative access (HTTPS management interfaces)
2. VPN/Tunnel authentication (if PKI-based)
3. Monitoring endpoints
4. Reverse proxy (if deployed)

## Certificate Sources

| Use Case | Source | Renewal | Status |
|----------|--------|---------|--------|
| Management HTTPS | Self-signed or internal CA | Manual | TO BE DECIDED |
| VPN authentication | Self-generated keys (WireGuard) or PKI (OpenVPN) | Per protocol | TO BE DECIDED |
| Monitoring endpoint | Self-signed or Let's Encrypt | Automated | TO BE DECIDED |
| Reverse proxy | Let's Encrypt or commercial CA | Automated | TO BE EVALUATED |

## Key Management

Per SEC-005, SEC-006, SEC-007:
- Private keys never stored in Git
- Key rotation schedule defined in operations procedures
- Backup keys stored securely, separate from configuration backups

## Certificate Monitoring

Per OPS-015:
- Certificate expiration monitored
- Advance warning before expiry
- Renewal procedures documented
