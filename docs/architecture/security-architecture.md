# Security Architecture

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Security Zones

| Zone | Components | Trust Level | Inbound Policy | Outbound Policy |
|------|-----------|-------------|----------------|-----------------|
| External | Internet, ISP | Untrusted | Default-deny | Controlled |
| DMZ-Egress | VPS1, VPS3 public IPs | Semi-trusted | Tunnel only + health checks | Forwarding traffic |
| Internal | LAN clients, Router LAN side | Trusted | From LAN only | Classified + routed |
| Management | Admin access points | Restricted | Authorized sources only | Limited |
| Tunnel | Router-VPS encrypted links | Encrypted | Tunnel endpoints only | Encrypted traffic only |

## Trust Boundaries

```text
                   ┌─────────────────────────────┐
                   │        INTERNET (Untrusted)  │
                   └──────────┬──────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │                               │
     ┌────────▼────────┐           ┌──────────▼──────────┐
     │   VPS1 (DMZ)    │           │   VPS3 (DMZ)        │
     │   Trust: Low    │           │   Trust: Low        │
     └────────┬────────┘           └──────────┬──────────┘
              │ Tunnel                         │ Tunnel
              │ Encrypted                      │ Encrypted
     ┌────────▼────────────────────────────────▼──────────┐
     │              Router (Classification)                │
     │              Trust: Medium                          │
     └────────┬──────────────────────────────┬────────────┘
              │ LAN                          │ Management
     ┌────────▼────────┐           ┌─────────▼───────────┐
     │  LAN (Trusted)  │           │  Admin (Restricted) │
     │  Trust: High    │           │  Trust: Highest     │
     └─────────────────┘           └─────────────────────┘
```

## Security Controls

| Control | Implementation | Reference |
|---------|---------------|-----------|
| Encryption in transit | Tunnel protocol | SEC-008 |
| Default-deny firewall | All components | SEC-010 |
| Least privilege access | Admin restrictions | SEC-001 |
| Key-based authentication | SSH for admin | SEC-002 |
| Audit logging | Administrative actions | SEC-018 |
| Configuration integrity | Git + checksums | SEC-013 |
| Secret management | External to repository | SEC-005, SEC-006 |
| DNS leak prevention | Per-egress DNS | SEC-019 |
| Traffic isolation | Policy routing | SEC-020 |
