# Assumptions

**Status:** DRAFT — OWNER REVIEW REQUIRED

| ID | Assumption | Reason | Impact if false | Validation method | Owner decision | Status |
| -- | ---------- | ------ | --------------- | ----------------- | -------------- | ------ |
| ASM-001 | MikroTik remains the traffic-classification point | Initial concept specifies MikroTik | Architecture redesign required | Owner confirmation | REQUIRED | UNVALIDATED |
| ASM-002 | VPS1 is intended for Russian egress | Initial concept naming convention | Egress pairing incorrect | Owner confirmation | REQUIRED | UNVALIDATED |
| ASM-003 | VPS3 is intended for international egress | Initial concept naming convention | Egress pairing incorrect | Owner confirmation | REQUIRED | UNVALIDATED |
| ASM-004 | Owner controls both VPS instances | Required for configuration deployment | Cannot deploy to uncontrolled infrastructure | Owner confirmation | REQUIRED | UNVALIDATED |
| ASM-005 | Router can support required policy routing features | RouterOS generally supports policy routing | Alternative router or approach needed | RouterOS version check | REQUIRED | UNVALIDATED |
| ASM-006 | Administrative access can be restricted to authorized sources | Standard security practice | Additional security controls needed | Router config review | REQUIRED | UNVALIDATED |
| ASM-007 | Monitoring endpoint can be deployed on or near infrastructure | Operational requirement | External monitoring needed | Infrastructure review | REQUIRED | UNVALIDATED |
| ASM-008 | Configuration backup is permitted by Owner | Operational safety | Cannot implement backup | Owner confirmation | REQUIRED | UNVALIDATED |
| ASM-009 | DNS behavior can be controlled at router level | RouterOS DNS features | External DNS resolver needed | RouterOS version check | REQUIRED | UNVALIDATED |
| ASM-010 | Public endpoints can be health-checked from monitoring location | Monitoring requirement | Alternative health-check method needed | Network test | REQUIRED | UNVALIDATED |
