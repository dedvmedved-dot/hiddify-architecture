# Open Questions

**Status:** DRAFT — OWNER REVIEW REQUIRED

## BLOCKING Questions

| ID | Question | Why needed | Blocks |
| -- | -------- | ---------- | ------ |
| OQ-001 | What is the exact MikroTik model? | Determines feature availability and performance | Router configuration, inventory |
| OQ-002 | What RouterOS version is installed? | Determines available features and limitations | Feature selection, validation |
| OQ-003 | What are the router specifications (RAM, CPU, storage)? | Determines capacity for rules, tunnels, monitoring | Sizing, performance |
| OQ-004 | What interfaces and throughput are available? | Determines WAN/LAN topology and capacity | Network design |
| OQ-005 | Is hardware offload available for routing/encryption? | Significant performance impact | Tunnel protocol selection |
| OQ-006 | What local networks exist (subnets, VLANs, clients)? | Determines traffic sources and classification | Routing policy, network design |
| OQ-007 | Which client categories are in scope? | Determines classification granularity | Traffic classification |
| OQ-008 | What is the expected throughput (Mbps)? | Determines VPS and tunnel sizing | Capacity planning |
| OQ-009 | How many concurrent clients and connections? | Determines rule and session capacity | Sizing |
| OQ-010 | Which traffic classes go through RU egress? | Core routing requirement | Routing policy |
| OQ-011 | Which traffic classes go through INT egress? | Core routing requirement | Routing policy |
| OQ-012 | What is the default route behavior for unmatched traffic? | Determines fail behavior | Routing policy |
| OQ-013 | Fail-open or fail-closed for egress failure? | Critical security and availability decision | Architecture, security |
| OQ-014 | What happens when VPS1 fails? | Operational continuity | Fallback design |
| OQ-015 | What happens when VPS3 fails? | Operational continuity | Fallback design |
| OQ-016 | Is direct internet bypass permitted for any traffic? | Security boundary decision | Routing policy |
| OQ-017 | Is IPv6 required? | Determines scope of routing and DNS design | Addressing, routing |

## HIGH Priority Questions

| ID | Question | Why needed | Blocks |
| -- | -------- | ---------- | ------ |
| OQ-020 | What OS and version runs on VPS1? | Determines available software and configuration | VPS configuration |
| OQ-021 | What OS and version runs on VPS3? | Determines available software and configuration | VPS configuration |
| OQ-022 | What are the VPS specifications (CPU, RAM, disk, bandwidth limits)? | Determines proxy/VPN capacity | Sizing |
| OQ-023 | What DNS resolvers should be used per egress? | Core DNS requirement | DNS architecture |
| OQ-024 | Where should DNS queries be resolved (router vs VPS vs external)? | Architecture decision | DNS design |
| OQ-025 | What administrative access methods are permitted (SSH, Winbox, API)? | Operational security | Access design |
| OQ-026 | What monitoring platform is preferred? | Operational requirement | Monitoring design |
| OQ-027 | What alert channels are permitted (Telegram, email, etc.)? | Operational requirement | Alerting design |
| OQ-028 | What are the RTO and RPO targets? | Backup and DR planning | Backup design |

## MEDIUM Priority Questions

| ID | Question | Why needed | Blocks |
| -- | -------- | ---------- | ------ |
| OQ-040 | What are ISP-imposed restrictions or filters? | Determines tunnel protocol compatibility | Tunnel selection |
| OQ-041 | What are VPS provider restrictions? | Determines software and port availability | VPS configuration |
| OQ-042 | What are the legal or regulatory constraints? | Compliance requirement | Architecture, jurisdiction |
| OQ-043 | What budget is available for infrastructure? | Determines VPS tier and bandwidth | Sizing |
| OQ-044 | What planned maintenance windows are acceptable? | Operational planning | Deployment procedures |
| OQ-045 | What are the logging retention requirements? | Storage and compliance | Logging design |
