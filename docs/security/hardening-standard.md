# Hardening Standard

**Status:** DRAFT

## Overview

This document defines the security hardening standards for all system components.

## Linux VPS Hardening

1. SSH hardening (key-only, non-standard port, AllowUsers)
2. Firewall (default deny, minimal open ports)
3. Fail2ban / SSHGuard
4. Automatic security updates
5. Minimal installed packages
6. Disabled unused services
7. File permission hardening
8. Kernel parameter hardening (sysctl)

## MikroTik Hardening

1. Strong authentication
2. Service minimization
3. Firewall rules
4. Logging configuration
5. Management access restriction

## Network Hardening

1. Encrypted tunnels between all nodes
2. DNS security (DNSSEC, DoH/DoT)
3. Certificate management
4. Traffic monitoring

---

*Hardening standards will be refined during security implementation stages.*
