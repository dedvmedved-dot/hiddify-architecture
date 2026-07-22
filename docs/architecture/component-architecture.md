# Component Architecture

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Component Specification

### CMP-001 — Traffic Classifier (Router)

- **Role:** Classify all traffic and route to appropriate egress
- **Platform:** RouterOS (MikroTik) — per initial concept
- **Key capabilities required:**
  - Policy-based routing (FR-001 to FR-007)
  - Address lists (FR-003)
  - Firewall with default-deny (SEC-010)
  - Connection tracking (FR-014)
  - DNS forwarding/redirection (FR-030)
  - Health check support (FR-041)
- **Resource requirements:** TO BE DETERMINED from Owner input
- **Interfaces:**
  - WAN: ISP uplink
  - LAN: Internal network(s)
  - Management: Administrative access (isolated)

### CMP-002/003/004 — Tunnel Endpoints

- **Role:** Encrypted transport between router and egress nodes
- **Candidate technologies:**
  - WireGuard (kernel-level, high performance, simple)
  - OpenVPN (mature, flexible, higher overhead)
  - IPsec/IKEv2 (standards-based, hardware offload possible)
- **Selection criteria:** Throughput, latency, RouterOS compatibility, VPS OS support, ISP filtering resistance
- **Status:** TO BE EVALUATED in technology selection stage

### CMP-005/006 — DNS Resolvers

- **Role:** Resolve DNS queries through appropriate egress path
- **Architecture options:**
  - Option A: Router forwards to VPS-based resolver via tunnel
  - Option B: Router uses local resolver with per-egress upstream
  - Option C: VPS runs resolver; clients use VPS directly
- **Selection criteria:** Leak prevention, performance, caching, failure handling
- **Status:** TO BE DECIDED — see DNS-OQ-01

### CMP-007/008/009 — Firewalls

- **Role:** Default-deny on all components
- **Router firewall:**
  - Allow established/related
  - Allow management from authorized sources
  - Allow tunnel traffic to VPS endpoints
  - Drop all other inbound
- **VPS firewall:**
  - Allow tunnel traffic from router
  - Allow egress traffic (forwarding)
  - Allow health checks from monitoring
  - Drop all other inbound

### CMP-013 — Reverse Proxy (Optional)

- **Role:** Forward traffic from egress node to destination
- **When needed:** If tunnel terminates before application-level routing
- **Candidates:** Nginx, HAProxy, built-in proxy of VPN platform
- **Status:** TO BE EVALUATED

## Inter-Component Communication

| From | To | Protocol | Purpose |
|------|----|----------|---------|
| Router | VPS1 | Tunnel protocol | RU egress traffic + DNS |
| Router | VPS3 | Tunnel protocol | INT egress traffic + DNS |
| Monitoring | All | HTTP/ICMP | Health checks |
| Admin | Router | SSH/Winbox | Configuration |
| Admin | VPS | SSH | Configuration |
| Clients | Router | IP | User traffic |
