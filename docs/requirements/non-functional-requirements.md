# Non-Functional Requirements

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Availability

| ID | Statement | Rationale | Metric | Target | Status |
| -- | --------- | --------- | ------ | ------ | ------ |
| NFR-001 | System shall maintain defined availability for egress paths | Service continuity | Uptime percentage | UNKNOWN — OWNER DECISION REQUIRED | OWNER REVIEW REQUIRED |
| NFR-002 | Single egress failure shall not cause total service loss if alternative exists | Resilience | Failover time | UNKNOWN — OWNER DECISION REQUIRED | OWNER REVIEW REQUIRED |

## Performance

| ID | Statement | Rationale | Metric | Target | Status |
| -- | --------- | --------- | ------ | ------ | ------ |
| NFR-010 | System shall process traffic classification within acceptable latency | User experience | Classification latency | UNKNOWN — OWNER DECISION REQUIRED | OWNER REVIEW REQUIRED |
| NFR-011 | Tunnel throughput shall meet operational requirements | Capacity planning | Mbps per egress | UNKNOWN — OWNER DECISION REQUIRED | OWNER REVIEW REQUIRED |
| NFR-012 | System shall support expected number of concurrent sessions | Capacity planning | Concurrent sessions | UNKNOWN — OWNER DECISION REQUIRED | OWNER REVIEW REQUIRED |

## Capacity

| ID | Statement | Rationale | Metric | Target | Status |
| -- | --------- | --------- | ------ | ------ | ------ |
| NFR-020 | Router resources shall accommodate peak load with headroom | Resource planning | CPU/RAM utilization | UNKNOWN — OWNER DECISION REQUIRED | OWNER REVIEW REQUIRED |
| NFR-021 | VPS resources shall accommodate peak throughput with headroom | Resource planning | CPU/RAM/bandwidth | UNKNOWN — OWNER DECISION REQUIRED | OWNER REVIEW REQUIRED |

## Reliability

| ID | Statement | Rationale | Metric | Target | Status |
| -- | --------- | --------- | ------ | ------ | ------ |
| NFR-030 | Tunnel connections shall auto-recover from transient failures | Resilience | Recovery time | UNKNOWN — OWNER DECISION REQUIRED | OWNER REVIEW REQUIRED |
| NFR-031 | DNS resolution shall remain available during single resolver failure | Resilience | Failover time | UNKNOWN — OWNER DECISION REQUIRED | OWNER REVIEW REQUIRED |

## Auditability

| ID | Statement | Rationale | Metric | Target | Status |
| -- | --------- | --------- | ------ | ------ | ------ |
| NFR-040 | All configuration changes shall be traceable to Git commits | Audit trail | 100% of changes | MUST | OWNER REVIEW REQUIRED |
| NFR-041 | Stage evidence shall be independently verifiable | External audit | Evidence completeness | MUST | OWNER REVIEW REQUIRED |

## Maintainability

| ID | Statement | Rationale | Metric | Target | Status |
| -- | --------- | --------- | ------ | ------ | ------ |
| NFR-050 | Configuration shall be documented in sanitized templates | Operator clarity | Documentation coverage | MUST | OWNER REVIEW REQUIRED |
| NFR-051 | Rollback procedures shall be documented and tested | Operational safety | Tested procedures | SHOULD | OWNER REVIEW REQUIRED |

## Documentation Quality

| ID | Statement | Rationale | Metric | Target | Status |
| -- | --------- | --------- | ------ | ------ | ------ |
| NFR-060 | All architectural decisions shall be recorded as ADRs | Traceability | ADR per decision | MUST | OWNER REVIEW REQUIRED |
| NFR-061 | All requirements shall be traceable to source and verification method | Auditability | Traceability matrix | MUST | OWNER REVIEW REQUIRED |
