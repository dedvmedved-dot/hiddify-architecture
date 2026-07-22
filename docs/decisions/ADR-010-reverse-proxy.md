# ADR-010 — Reverse Proxy Architecture

- **Status:** PROPOSED
- **Date:** 2026-07-22
- **Decision-maker:** ChatGPT

## Context

Traffic arriving at egress nodes may need forwarding to final destinations.
A reverse proxy may be required depending on the chosen VPN/tunnel architecture.

## Decision

**Defer reverse proxy decision** until VPN technology is selected.

If WireGuard is selected: Traffic is routed at IP layer; no application-level
proxy required. Router policy routes packets through tunnel; VPS forwards
natively.

If OpenVPN is selected: Similar — IP-layer routing.

If Hiddify or application-level proxy is selected: Reverse proxy may be
required for traffic forwarding. Evaluate Nginx or HAProxy at that time.

## Current Recommendation

IP-layer routing (WireGuard or OpenVPN) with direct forwarding on VPS.
No reverse proxy needed for initial architecture.

## Consequences

- Simpler architecture without additional proxy layer
- Less processing overhead on VPS
- No TLS termination at proxy (end-to-end encryption preserved)
- If application-level proxy needed later, reverse proxy can be added
