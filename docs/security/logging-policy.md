# Logging Policy

**Status:** DRAFT

## Overview

This document defines the logging policy for audit trail and security monitoring.

## Log Categories

| Category | Source | Retention | Purpose |
|----------|--------|-----------|---------|
| Authentication | sshd, PAM | 90 days | Security audit |
| Firewall | iptables/nftables | 30 days | Intrusion detection |
| Application | VPN/Proxy service | 30 days | Operational monitoring |
| System | syslog, journal | 30 days | Troubleshooting |

## Log Format Requirements

- Timestamp in UTC (ISO 8601)
- Source host identification
- Event classification
- Sanitized (no secrets in logs)

## Log Storage

*To be defined during security implementation stage.*

---

*This document is a placeholder. Logging policy will be developed during security stages.*
