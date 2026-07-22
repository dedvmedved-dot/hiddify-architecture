# Stakeholders

**Status:** DRAFT — OWNER REVIEW REQUIRED

| ID | Stakeholder | Role | Interests | Responsibilities | Approval Authority | Inputs Required | Risks If Not Consulted |
| -- | ----------- | ---- | --------- | ---------------- | ------------------ | --------------- | ---------------------- |
| STK-001 | Owner | Sponsor / infrastructure owner | Business continuity, secure access, cost control, legal compliance | Business and production authorization | YES — all production changes | Scope definition, traffic policy, risk acceptance, budget | Requirements mismatch, blocked deployment, unauthorized changes |
| STK-002 | ChatGPT | Architect / external auditor | Auditable design, traceable decisions, verifiable quality | Requirements and stage acceptance | YES — stage acceptance and architecture approval | Stage evidence, commit SHAs, reports | Unverified work, uncontrolled scope creep |
| STK-003 | Hermes | Implementor | Clear task definition, verifiable evidence, safe boundaries | Documentation, evidence collection, configuration creation | NO | Task definitions, environment data, credentials (sanitized) | Blocked implementation, incomplete evidence |
| STK-004 | Network administrator | Operator | Reliable operation, actionable alerts, documented procedures | Operations, troubleshooting, maintenance | NO (recommendations only) | Operational constraints, monitoring preferences, maintenance windows | Unmaintainable system, operational blind spots |
| STK-005 | End users | Consumers | Available service, acceptable performance, clear routing behavior | Use of network access | NO | User scenarios, traffic patterns, critical destinations | Unsuitable design, user bypass attempts |
| STK-006 | VPS provider | External dependency | SLA compliance, resource availability | Hosting and networking | NO | Resource limits, API capabilities, regional availability | Insufficient capacity, platform incompatibility |
| STK-007 | ISP | External dependency | Bandwidth, contract terms | Internet connectivity | NO | Addressing, filtering constraints, CGNAT status | Asymmetric routing, blocked traffic, unexpected NAT |
