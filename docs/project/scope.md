# Project Scope

**Status:** DRAFT

## In Scope

1. Network architecture design (MikroTik, VPS, routing)
2. VPN/proxy configuration (technology TBD)
3. DNS architecture
4. Security hardening of all components
5. Monitoring and alerting setup
6. Backup and restore procedures
7. Comprehensive testing strategy
8. Documentation of all decisions and configurations
9. Incident response procedures

## Out of Scope

1. Client application development
2. End-user documentation
3. Commercial deployment or SaaS offering
4. Mobile application development
5. Hardware procurement
6. ISP relationship management

## Boundaries

### Included Infrastructure

- MikroTik router(s)
- VPS1 (egress node)
- VPS3 (egress node)
- Associated networking (DNS, routing, firewall)

### Excluded Infrastructure

- End-user devices
- ISP equipment
- Third-party cloud services beyond specified VPS instances

## Deliverables

For each stage, deliverables include:

- Documentation in `docs/`
- Configurations in `configs/`
- Scripts in `scripts/`
- Test artifacts in `tests/`
- Evidence in `evidence/`
- Stage report in `stages/`
