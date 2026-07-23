# Configuration Schema

**Status:** DRAFT — Stage 04 OFFLINE SKELETON

## Schema Location

`iac/schemas/config-schema.json` — JSON Schema (draft 2020-12)

## Enforced Constraints

- `deployment_enabled`: const false
- `production_mode`: const false
- `allow_remote_execution`: const false
- `allow_network_changes`: const false
- `allow_secret_material`: const false

## Additional Validation

- Required fields: environment, safety_flags
- Deployment mode enum: offline-skeleton only
- Host addresses: documentation IPs only
- Domain names: example.invalid pattern

## Test IDs

S04-CFG-001 through S04-CFG-005
