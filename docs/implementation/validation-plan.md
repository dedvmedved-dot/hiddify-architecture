# Validation Plan

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Validation Gates

| Gate | Phase | Criteria | Owner |
|------|-------|----------|-------|
| VG-1 | Post-Phase 2 | All nodes accessible via management | Administrator |
| VG-2 | Post-Phase 3 | Tunnels established and passing health checks | Administrator |
| VG-3 | Post-Phase 4 | DNS resolution correct per egress path | Administrator |
| VG-4 | Post-Phase 5 | Traffic classified and routed correctly | Administrator |
| VG-5 | Post-Phase 6 | All tests passed; Owner acceptance | Owner |

## Per-Component Validation

### Router Validation

- [ ] Management access restricted to authorized sources
- [ ] Firewall default-deny verified (port scan from LAN)
- [ ] NTP synchronized
- [ ] Configuration backup exported and verified
- [ ] Policy routing rules active
- [ ] Address lists populated
- [ ] Tunnel interfaces up

### VPS Validation

- [ ] SSH accessible only with keys (password auth disabled)
- [ ] Firewall default-deny verified
- [ ] OS packages updated
- [ ] Tunnel endpoint active
- [ ] DNS resolver responding
- [ ] Monitoring agent reporting

### Tunnel Validation

- [ ] Tunnel interface up on both endpoints
- [ ] ICMP through tunnel (both directions)
- [ ] Tunnel re-establishes after disruption
- [ ] Tunnel bandwidth meets requirements

### DNS Validation

- [ ] RU DNS queries resolved through RU egress
- [ ] INT DNS queries resolved through INT egress
- [ ] No DNS leakage to default ISP resolver
- [ ] DNS caching functional

### Routing Validation

- [ ] RU-classified IP reaches destination via VPS1
- [ ] INT-classified IP reaches destination via VPS3
- [ ] Default traffic handled per policy
- [ ] Session persistence maintained
- [ ] No cross-egress leakage
