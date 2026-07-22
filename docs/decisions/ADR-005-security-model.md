# ADR-005 — Security Model

- **Status:** PROPOSED
- **Date:** 2026-07-22
- **Decision-maker:** ChatGPT

## Context

The architecture must protect infrastructure, prevent traffic leaks,
and maintain auditability.

## Decision

Adopt a **Defense-in-Depth** security model:

1. **Perimeter:** Default-deny firewall on all components
2. **Transport:** Encryption for all inter-component traffic
3. **Access:** Least-privilege administrative access
4. **Data:** Secrets external to Git; sanitized configurations
5. **Audit:** All administrative actions logged
6. **Recovery:** Backup and rollback procedures defined

## Security Zones

- External (Internet): Untrusted
- DMZ-Egress (VPS public IPs): Semi-trusted
- Internal (LAN): Trusted
- Management (Admin): Restricted
- Tunnel (Encrypted links): Encrypted

## Consequences

- All components require firewall configuration
- Administrative access must be restricted and logged
- DNS and traffic leakage prevented by policy routing
- Configuration changes traceable through Git
