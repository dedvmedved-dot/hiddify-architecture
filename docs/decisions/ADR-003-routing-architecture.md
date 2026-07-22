# ADR-003 — Routing Architecture

- **Status:** PROPOSED
- **Date:** 2026-07-22
- **Decision-maker:** ChatGPT

## Context

Traffic must be classified and routed to appropriate egress paths.
The architecture must support policy-based routing with connection tracking.

## Decision

Adopt **Policy-Based Routing (PBR)** on the MikroTik router:

1. Traffic classified by destination IP, domain, or port
2. Address lists maintain classification rules
3. Policy routes direct traffic to appropriate tunnel interface
4. Connection tracking ensures return traffic follows correct path
5. Default route handles unmatched traffic (TO BE DECIDED)

## Alternatives Considered

| Alternative | Rejected Because |
|-------------|------------------|
| Static routing only | Cannot classify by domain or application |
| BGP | Unnecessary complexity for single-router topology |
| Client-side proxy | Requires client configuration; bypass risk |

## Consequences

- Requires RouterOS policy routing features (mangle, routing marks)
- Address list maintenance required for domain-based classification
- Connection tracking consumes router memory
- Policy changes require careful testing to avoid traffic leaks
