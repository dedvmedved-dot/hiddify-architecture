# Stage 06 Acceptance

**Status:** PENDING — DEPLOYMENT BLOCKED
**Timestamp:** 2026-07-24T03:15:00Z

Blocking: Owner input not received.
Cannot proceed to deployment without lab environment parameters.

## Semantic Validation Framework

Stage 06 now includes a semantic evidence validator that checks beyond file existence:

1. **HEAD Consistency** — all evidence files must reference the same HEAD SHA
2. **Timestamp Validity** — UTC timestamps must be valid, no future dates
3. **Timestamp Consistency** — all evidence timestamps within 10 minutes of each other
4. **Mandatory Metadata** — every evidence file must include Stage, HEAD, and Timestamp
5. **Evidence Consistency** — no contradictions between deployment, owner input, and environment state
6. **Blocked State Validation** — if owner input=NO, all deployment files must show BLOCKED
7. **Stage Consistency** — all evidence files must reference Stage 06

## CI Safety Gate

The safety gate `|| true` masking has been removed and replaced with `continue-on-error: true`
to preserve exit code visibility while allowing downstream evidence collection.

## Unit Tests

- Semantic validator: 18 tests covering valid/invalid HEAD, timestamps, metadata, consistency, blocked state, stage references
- Safety gate: 8 tests covering blocked/approved states, exit codes, and no-masking verification
