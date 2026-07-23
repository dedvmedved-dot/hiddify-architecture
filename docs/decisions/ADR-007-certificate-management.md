# ADR-007 — Certificate Management

- **Status:** PROPOSED
- **Date:** 2026-07-22
- **Decision-maker:** ChatGPT

## Context

TLS certificates are needed for management interfaces, monitoring endpoints,
and potentially reverse proxy services. VPN keys are managed separately.

## Decision

1. **Management interfaces:** Self-signed certificates acceptable for
   internal administrative access (restricted network).
2. **Public endpoints:** Let's Encrypt for any publicly accessible
   monitoring or proxy endpoints.
3. **VPN keys:** Managed per protocol (WireGuard: static key pairs;
   OpenVPN: PKI with internal CA).

## Alternatives Considered

| Alternative | Rejected Because |
|-------------|------------------|
| Commercial CA for everything | Unnecessary cost for internal services |
| No TLS for management | Unacceptable for administrative access |
| Manual certificate only | Automation preferred for public endpoints |

## Consequences

- Self-signed certs require manual trust on admin workstations
- Let's Encrypt requires automated renewal (certbot or similar)
- VPN key rotation must be procedurally managed
