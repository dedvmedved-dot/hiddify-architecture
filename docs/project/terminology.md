# Terminology

**Status:** DRAFT

## Project-Specific Terms

| Term | Definition |
|------|------------|
| **Stage** | A discrete phase of work with defined inputs and outputs |
| **Stage-Gate** | Process controlling transition between stages |
| **Evidence** | Immutable proof of work performed (logs, outputs, screenshots) |
| **ADR** | Architecture Decision Record — documents a significant decision |
| **External Audit** | Review performed by ChatGPT via GitHub connector |
| **Sanitized** | Configuration with all secrets replaced by placeholders |
| **Egress** | Exit point for network traffic (VPS server) |
| **Ingress** | Entry point for network traffic (MikroTik router) |

## Technical Terms

| Term | Definition |
|------|------------|
| **MikroTik** | RouterOS-based network device used for routing and firewall |
| **VPS** | Virtual Private Server — cloud-hosted server instance |
| **Hiddify** | A proxy/VPN management platform (candidacy not confirmed) |
| **Split Routing** | Routing traffic through different egress based on rules |
| **WireGuard** | Modern VPN protocol (candidacy not confirmed) |
| **nftables** | Linux packet filtering framework |
| **Policy-Based Routing** | Routing decisions based on traffic attributes beyond destination |

## Status Terms

| Status | Meaning |
|--------|---------|
| `DRAFT` | Not yet approved, subject to change |
| `NOT STARTED` | Stage defined, work not begun |
| `IN PROGRESS` | Active work on the stage |
| `READY FOR EXTERNAL AUDIT` | Work complete, awaiting review |
| `FAILED` | Critical issues found |
| `CONDITIONAL PASS` | Minor issues, can proceed |
| `PASSED` | Approved by external auditor |
| `CONNECTOR VERIFIED` | Verified via GitHub connector |

## Infrastructure Identifiers

| Identifier | Description |
|------------|-------------|
| `VPS1` | First VPS egress node (location TBD) |
| `VPS3` | Second VPS egress node (location TBD) |
| `MikroTik` | Primary router/firewall device |

## Abbreviations

| Abbreviation | Full Form |
|--------------|-----------|
| ADR | Architecture Decision Record |
| PBR | Policy-Based Routing |
| DNS | Domain Name System |
| TLS | Transport Layer Security |
| VPN | Virtual Private Network |
| VPS | Virtual Private Server |
| NAT | Network Address Translation |
| CIDR | Classless Inter-Domain Routing |
