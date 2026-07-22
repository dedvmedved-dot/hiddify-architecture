# Routing Architecture

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Architecture Decision

**ADR-003** addresses routing architecture. See `docs/decisions/ADR-003-routing-architecture.md`.

## Routing Model

```text
                    ┌──────────────────────┐
                    │   Traffic enters     │
                    │   from LAN           │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │  Classification      │
                    │  (Address lists,     │
                    │   domains, ports)    │
                    └──────────┬───────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
   ┌────────▼────────┐ ┌───────▼───────┐ ┌───────▼────────┐
   │ RU Egress Rule  │ │ INT Egress    │ │ Default Rule   │
   │ → Tunnel RU     │ │ → Tunnel INT  │ │ → TO BE DECIDED│
   └────────┬────────┘ └───────┬───────┘ └───────┬────────┘
            │                  │                  │
   ┌────────▼────────┐ ┌───────▼───────┐          │
   │ VPS1 (RU IP)    │ │ VPS3 (INT IP) │          │
   └─────────────────┘ └───────────────┘          │
                                          ┌───────▼────────┐
                                          │ ISP Default    │
                                          │ (if bypass OK) │
                                          └────────────────┘
```

## Policy Structure

| Priority | Traffic Class | Match | Route | Fallback |
|----------|---------------|-------|-------|----------|
| 1 | RU-specific | Owner-defined IPs/domains | VPS1 tunnel | TO BE DECIDED |
| 2 | INT-specific | Owner-defined IPs/domains | VPS3 tunnel | TO BE DECIDED |
| 3 | Explicit bypass | Owner-defined exceptions | Direct ISP | N/A |
| 999 | Default | All unmatched | TO BE DECIDED | N/A |

## Connection Tracking

Per FR-014, FR-015:

- Router tracks all connections
- Return traffic automatically routed through correct interface
- Connection table size must accommodate peak concurrent sessions (OQ-009)

## Session Persistence

- All packets of an established connection follow the same egress path
- Policy changes do not break existing connections (new connections use updated policy)
- Connection timeout aligned with application requirements
