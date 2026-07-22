# Initial Concept

**Status:** DRAFT — NOT AN APPROVED ARCHITECTURE

**⚠️ IMPORTANT:** This document represents the starting concept for the project. It is NOT an approved architecture. All technology choices, designs, and approaches described here are subject to evaluation, refinement, and potential rejection during the stage-gate process.

## Concept Summary

The initial concept involves creating a network access system with the following characteristics:

### Goals

- Secure network access through multiple egress points
- Split routing based on traffic classification rules
- Russian and international egress for geographic diversity
- Centralized management and monitoring

### Initial Technology Candidates

- **Hiddify** — Proxy/VPN management platform (to be evaluated)
- **MikroTik** — Router for traffic classification and routing
- **VPS** — Cloud servers for egress points

### High-Level Architecture Idea

```text
Clients → MikroTik (classification) → VPS1 (RU egress)
                                    → VPS3 (INT egress)
```

### Key Considerations

- Security of tunnel connections
- DNS consistency with routing
- Failover between egress points
- Monitoring and alerting
- Configuration management

## Disclaimer

This concept is a starting point only. The final architecture may:

- Use different technologies
- Have a different topology
- Implement different routing strategies
- Include additional or fewer components

The repository name "hiddify-architecture" does not commit the project to using Hiddify. All technology choices will be evaluated through the stage-gate process.

---

*This document is preserved as-is for audit trail purposes. Do not edit.*
