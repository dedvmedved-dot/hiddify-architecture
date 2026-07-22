# Architecture Risks

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Inherited from Stage 01

Refer to `docs/requirements/requirements-risks.md` for full risk register (RISK-01-001 to RISK-01-020).

## Architecture-Specific Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|------------|--------|------------|
| ARC-RISK-01 | Router cannot support required throughput | UNKNOWN | HIGH | Performance testing before deployment |
| ARC-RISK-02 | Selected VPN protocol incompatible with RouterOS version | MEDIUM | HIGH | Verify RouterOS version; fallback protocol |
| ARC-RISK-03 | VPS provider blocks tunnel protocol | LOW | HIGH | Protocol diversity; test before deployment |
| ARC-RISK-04 | DNS architecture causes leakage | MEDIUM | HIGH | DNS leak testing before production |
| ARC-RISK-05 | Policy routing rules exceed router capacity | UNKNOWN | MEDIUM | Rule count estimation; optimization |
| ARC-RISK-06 | Single router failure causes total outage | LOW | HIGH | Backup/restore procedures; future HA |
| ARC-RISK-07 | Architecture assumes capabilities not confirmed by Owner | HIGH | HIGH | All assumptions documented; Owner validation required |
