# Routing Policy Requirements

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Policy Objectives

Define deterministic traffic classification and egress selection ensuring that each traffic category exits through the intended path with predictable fallback behavior.

## Traffic Categories

| Policy ID | Traffic class | Match basis | Preferred egress | Fallback | Fail behavior | Status |
| --------- | ------------- | ----------- | ---------------- | -------- | ------------- | ------ |
| RTE-001 | Russian egress traffic | Owner-defined destinations | VPS1 | TO BE DECIDED | TO BE DECIDED | UNKNOWN |
| RTE-002 | International egress traffic | Owner-defined destinations | VPS3 | TO BE DECIDED | TO BE DECIDED | UNKNOWN |
| RTE-003 | Default/fallback traffic | Unmatched traffic | TO BE DECIDED | TO BE DECIDED | TO BE DECIDED | UNKNOWN |
| RTE-004 | Local/management traffic | Internal networks | Local | N/A | N/A | UNKNOWN |

## Policy Requirements

| ID | Requirement | Priority | Source | Status |
| -- | ----------- | -------- | ------ | ------ |
| RTE-010 | Traffic classification shall be deterministic and reproducible | MUST | Derived | OWNER REVIEW REQUIRED |
| RTE-011 | Policy shall define precedence order when multiple rules match | MUST | Derived | OWNER REVIEW REQUIRED |
| RTE-012 | Default behavior for unmatched traffic shall be explicitly defined | MUST | Derived | OWNER REVIEW REQUIRED |
| RTE-013 | Russian egress candidates shall be explicitly listed | MUST | Initial concept | OWNER REVIEW REQUIRED |
| RTE-014 | International egress candidates shall be explicitly listed | MUST | Initial concept | OWNER REVIEW REQUIRED |
| RTE-015 | Explicit bypass candidates shall be documented if applicable | SHOULD | Derived | OWNER REVIEW REQUIRED |
| RTE-016 | Blocked traffic candidates shall be documented if applicable | COULD | Derived | OWNER REVIEW REQUIRED |
| RTE-017 | Fail-open versus fail-closed decision shall be explicitly documented | MUST | Security requirements | OWNER REVIEW REQUIRED |
| RTE-018 | Session persistence shall be maintained across policy changes | MUST | Derived | OWNER REVIEW REQUIRED |
| RTE-019 | DNS queries shall follow same egress path as corresponding traffic category | MUST | Derived | OWNER REVIEW REQUIRED |
| RTE-020 | IPv4 routing shall be supported | MUST | Infrastructure | OWNER REVIEW REQUIRED |
| RTE-021 | IPv6 routing requirements shall be documented (support or exclusion) | MUST | TO BE DECIDED | OWNER REVIEW REQUIRED |
| RTE-022 | Routing changes shall be logged | MUST | Audit requirements | OWNER REVIEW REQUIRED |
| RTE-023 | Manual override shall require approval and be logged | MUST | Security requirements | OWNER REVIEW REQUIRED |
| RTE-024 | Routing policy shall be testable before production deployment | SHOULD | Derived | OWNER REVIEW REQUIRED |
