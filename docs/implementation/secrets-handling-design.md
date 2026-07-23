# Secrets Handling Design

**Status:** DRAFT — Stage 04 OFFLINE SKELETON

## Secrets Inventory

See `docs/implementation/secrets-inventory.md` for full placeholder inventory.

## Storage Policy

1. **No secrets in Git** — all committed files use placeholders only
2. **External vault** — production secrets stored outside repository
3. **Environment variables** — acceptable for CI (never committed)
4. **Key rotation** — per SEC-007 schedule

## Future Secret Types

| Type | Placeholder | Storage | Rotation |
|------|-------------|---------|----------|
| RouterOS password | <ROUTER_ADMIN_PASSWORD> | External vault | 90 days |
| SSH private keys | <SSH_PRIVATE_KEY> | External vault | 90 days |
| WireGuard keys | <WG_PRIVKEY> | External vault | 90 days |
| API tokens | <API_TOKEN> | External vault | 30 days |

## Validation

`safety_guard.py` scans for:

- Private key blocks (BEGIN PRIVATE KEY)
- Access tokens (ghp_, github_pat_, etc.)
- Passwords in config files
- Bearer tokens

## Incident Response

See SEC-017 and DR-06 for key compromise procedures.
