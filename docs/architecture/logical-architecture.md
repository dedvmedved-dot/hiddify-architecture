# Logical Architecture

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Overview

The logical architecture defines system components and their relationships
without binding to physical deployment or specific technologies.

## Layers

### Layer 1 — Client Layer

End-user devices generating traffic that requires classification and routing
through either Russian or international egress.

**Status:** Technology-agnostic. No specific client configuration mandated.

### Layer 2 — Classification Layer

Traffic classification engine responsible for:

- Matching traffic against policy rules
- Assigning egress path (RU/INT/default)
- Maintaining address lists and domain-based rules
- Handling policy precedence

**Implementation candidate:** MikroTik RouterOS (per initial concept)

**Status:** Router model and version UNKNOWN — see open questions OQ-001 to OQ-005

### Layer 3 — Transport Layer

Secure tunnel between classification point and egress nodes.

**Requirements:**
- Encryption in transit (SEC-008)
- Session persistence (FR-015)
- Monitoring and health checks (FR-040, FR-041)

**Technology candidates for evaluation:**
- WireGuard
- OpenVPN
- IPsec/IKEv2
- Hiddify-managed tunnels

**Status:** Technology NOT selected. All candidates must be evaluated against
NFRs and constraints before selection.

### Layer 4 — Egress Layer

Egress nodes providing exit points for classified traffic.

| Node | Purpose | Status |
|------|---------|--------|
| VPS1 | Russian egress | Candidate — specs UNKNOWN |
| VPS3 | International egress | Candidate — specs UNKNOWN |

Each egress node requires:
- VPN/tunnel endpoint
- DNS resolver aligned with egress path
- Firewall (default-deny)
- Monitoring agent
- Health check endpoint

### Layer 5 — Management Layer

Administrative access and monitoring for all components.

**Components:**
- Monitoring system (platform TO BE DECIDED)
- Alerting (channels TO BE DECIDED)
- Configuration management (Git-based, per project governance)
- Backup/restore (FR-050 to FR-056)

## Component Interactions

```text
Client → Classification → [RU egress tunnel] → VPS1 → Internet (RU IP)
                        → [INT egress tunnel] → VPS3 → Internet (INT IP)
                        → [default path]       → direct (TO BE DECIDED)

Management → all components (via isolated management plane)
Monitoring → all components (health checks, metrics)
DNS queries → aligned with traffic egress path
```

## Logical Component Inventory

| Component ID | Name | Layer | Function | Status |
|-------------|------|-------|----------|--------|
| CMP-001 | Traffic Classifier | Classification | Policy-based routing | Candidate: MikroTik |
| CMP-002 | Tunnel Endpoint (Router) | Transport | Tunnel initiation | TO BE DECIDED |
| CMP-003 | Tunnel Endpoint (VPS1) | Transport | Tunnel termination (RU) | TO BE DECIDED |
| CMP-004 | Tunnel Endpoint (VPS3) | Transport | Tunnel termination (INT) | TO BE DECIDED |
| CMP-005 | DNS Resolver (RU) | DNS | DNS via RU egress | TO BE DECIDED |
| CMP-006 | DNS Resolver (INT) | DNS | DNS via INT egress | TO BE DECIDED |
| CMP-007 | Firewall (Router) | Security | Default-deny, access control | TO BE CONFIGURED |
| CMP-008 | Firewall (VPS1) | Security | Egress node firewall | TO BE CONFIGURED |
| CMP-009 | Firewall (VPS3) | Security | Egress node firewall | TO BE CONFIGURED |
| CMP-010 | Monitoring Agent | Management | Health checks, metrics | TO BE DECIDED |
| CMP-011 | Alert Manager | Management | Alert routing | TO BE DECIDED |
| CMP-012 | Backup Manager | Management | Configuration backup | TO BE DECIDED |
| CMP-013 | Reverse Proxy | Egress | Optional — traffic forwarding | TO BE EVALUATED |
