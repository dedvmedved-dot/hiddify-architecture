# Offline Validation Design

**Status:** DRAFT — Stage 04 OFFLINE SKELETON

## Entrypoint

`scripts/validate_stage04.py` — single command to run all checks.

## Checks Performed

1. Configuration schema validation (JSON Schema)
2. Placeholder validation (no real IPs/secrets)
3. Safety flag validation (all flags = false)
4. Directory structure validation
5. Unit tests execution

## Requirements

- Python 3.9+
- PyYAML (for config parsing)
- No network access required
- No infrastructure access required

## Exit Codes

- 0: All checks passed
- 1: One or more checks failed
