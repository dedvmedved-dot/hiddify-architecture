# ADR-008 — Logging and Monitoring

- **Status:** PROPOSED (pending Owner platform choice)
- **Date:** 2026-07-22
- **Decision-maker:** ChatGPT + Owner

## Context

The architecture requires observability for tunnel state, egress reachability,
DNS availability, and security events.

## Decision

Adopt a **Minimal Viable Monitoring** approach:

1. Health checks: ICMP/TCP to egress endpoints, DNS resolvers
2. Tunnel state: RouterOS and VPS monitoring of tunnel interfaces
3. Alerting: TO BE DECIDED by Owner (OPS-006)
4. Logging: Administrative actions, tunnel state changes, firewall events
5. Log storage: Local with rotation; remote aggregation optional

## Monitoring Platform

**TO BE DECIDED by Owner** (OQ-026)

Candidates for evaluation:

- Zabbix
- Prometheus + Grafana
- Uptime Kuma
- Healthchecks.io

## Alert Channels

**TO BE DECIDED by Owner** (OQ-027)
