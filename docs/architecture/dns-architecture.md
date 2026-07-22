# DNS Architecture

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Architecture Decision

**ADR-004** addresses DNS architecture. See `docs/decisions/ADR-004-dns-architecture.md`.

## Key Question

> Should DNS queries use the same egress path as subsequent user traffic?

**DNS-OQ-01:** OWNER DECISION REQUIRED

## Proposed Model: Per-Egress DNS

Each egress path has a dedicated DNS resolver:

```text
RU-classified traffic → DNS via RU egress → RU DNS resolver
INT-classified traffic → DNS via INT egress → INT DNS resolver
Default traffic → DNS via default path (TO BE DECIDED)
```

## Resolver Architecture

| Resolver | Location | Upstream | Egress Path | Status |
|----------|----------|----------|-------------|--------|
| DNS-RU | Router or VPS1 | <DNS_RESOLVER_RU> | VPS1 | TO BE CONFIGURED |
| DNS-INT | Router or VPS3 | <DNS_RESOLVER_INT> | VPS3 | TO BE CONFIGURED |
| DNS-Default | Router | <DNS_RESOLVER_DEFAULT> | Default | TO BE CONFIGURED |

## Implementation Options

**Option A — Router-side forwarding:**
Router runs DNS forwarder; forwards to VPS-based resolver via tunnel.
Pros: Central control, simple client config. Cons: Adds router load.

**Option B — VPS-side resolver:**
Each VPS runs DNS resolver; clients query VPS directly.
Pros: Offloads router. Cons: Tunnel dependency for DNS.

**Option C — External resolvers:**
Router forwards to external DNS (8.8.8.8, 1.1.1.1) via policy routing.
Pros: Simple. Cons: Less control, external dependency.

## DNS Leak Prevention

Per DNS-001, DNS-002, SEC-019:
- Router policy routes DNS traffic through correct tunnel
- No DNS fallback to default ISP resolver
- DNS caching on router with per-egress cache separation
