# System Context

**Status:** DRAFT

## Overview

This document describes the system context — the boundaries of the system and its interactions with external entities.

## System Boundary

```text
┌─────────────────────────────────────────┐
│          Network Access System           │
│                                          │
│  ┌──────────┐  ┌──────┐  ┌──────┐      │
│  │ MikroTik │──│ VPS1 │  │ VPS3 │      │
│  │ Router   │  │(RU)  │  │(INT) │      │
│  └──────────┘  └──────┘  └──────┘      │
│       │                                  │
└───────┼──────────────────────────────────┘
        │
   ┌────┴────┐
   │ Clients │
   └─────────┘
```

## External Entities

| Entity | Description | Interface |
|--------|-------------|-----------|
| Clients | End-user devices | VPN/Proxy connection |
| ISP | Internet service provider | Physical/network link |
| DNS Providers | External DNS services | DNS protocol |
| Target Services | Internet resources | HTTP/HTTPS/TCP |

## Context Diagram

*To be created during architecture stage.*

---

*This document is a placeholder. Full system context will be developed during the architecture stage.*
