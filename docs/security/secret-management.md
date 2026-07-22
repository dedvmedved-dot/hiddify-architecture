# Secret Management

**Status:** DRAFT

## Overview

This document describes how secrets are managed in this project.

## Principles

1. **No secrets in Git** — Secrets are NEVER committed to the repository
2. **Use placeholders** — All examples use `<REPLACE_WITH_SECRET>`
3. **External storage** — Secrets stored in secure vaults or environment variables
4. **Rotation** — Secrets rotated regularly and on any exposure
5. **Audit** — All secret access is logged

## Placeholder Format

```text
<REPLACE_WITH_SECRET>
```

## Secret Storage (TBD)

Options to evaluate:

- HashiCorp Vault
- Environment variables on target hosts
- Encrypted files (SOPS, age)
- Cloud provider secret managers

## Rotation Schedule

| Secret Type | Rotation Period | Method |
|-------------|----------------|--------|
| SSH keys | 90 days | Manual |
| VPN keys | 90 days | Automated |
| API tokens | 30 days | Automated |
| Passwords | 90 days | Manual |

---

*Secret management strategy will be refined during security stages.*
