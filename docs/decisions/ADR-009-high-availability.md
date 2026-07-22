# ADR-009 — High Availability Approach

- **Status:** PROPOSED
- **Date:** 2026-07-22
- **Decision-maker:** ChatGPT

## Context

The initial architecture is single-instance. Future stages may require HA.

## Decision

Defer HA implementation to later stages. Initial deployment is single-instance
with documented recovery procedures.

HA design follows these principles (for future implementation):

1. Active-passive for router (VRRP or second device)
2. Active-passive for egress nodes (additional VPS per path)
3. Stateful failover where possible
4. Stateless where stateful not feasible

## Rationale

- Router model and capabilities unknown
- Budget constraints unknown
- HA adds complexity; initial focus on correct single-instance operation
- Recovery procedures provide manual failover capability

## Consequences

- Single router = single point of failure
- Single VPS per egress = no automatic egress failover
- Recovery time bounded by manual restore procedures
- HA can be added incrementally in later stages
