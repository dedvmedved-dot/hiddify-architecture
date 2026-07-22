# Security Policy

## Prohibited Content

The following must **NEVER** be committed to this repository:

- Passwords and passphrases
- API tokens and keys
- Private keys (SSH, TLS, WireGuard)
- SSH host keys
- Cookies and session tokens
- `.env` files with real values
- MikroTik backup files (`.backup`, `.backup.*`)
- Private MikroTik scripts (`.rsc.private`)
- Secret files (`*.secret`, `*.secrets`)
- Credentials directories (`credentials/`, `secrets/`, `private/`)

## Sanitization Requirements

All configuration examples must use placeholders:

```yaml
# WRONG - DO NOT COMMIT

password: SuperSecret123!
api_key: sk-1234567890abcdef

# CORRECT - USE PLACEHOLDERS

password: <REPLACE_WITH_SECRET>
api_key: <REPLACE_WITH_SECRET>
```

Acceptable placeholder formats:

- `<REPLACE_WITH_SECRET>`
- `<PASSWORD_HERE>`
- `<API_KEY>`
- `CHANGEME`

## Accidental Secret Exposure

If a secret is accidentally committed:

### Immediate Actions:

1. **Rotate the credential immediately** — assume it is compromised
2. **Do NOT delete the repository** — preserve audit trail
3. **Notify the Owner** — coordinate response
4. **Document in stage report** — include incident details

### Remediation Steps:

1. Remove from Git history using `git filter-branch` or `BFG Repo-Cleaner`
2. Force push cleaned history (coordinate with team)
3. Add pattern to `.gitignore` to prevent recurrence
4. Verify no cached copies exist (CI/CD, mirrors, forks)

### Post-Incident:

1. Review how the secret was exposed
2. Update validation scripts to catch similar patterns
3. Add to secret scanning rules
4. Update this SECURITY.md if needed

## Evidence Security

Evidence files may contain sensitive information:

- IP addresses (OK if from test environments)
- Hostnames (OK if generic or test systems)
- Usernames (OK if test accounts)
- Timestamps (OK)
- Command outputs (sanitize secrets before saving)

**Never include:**

- Production credentials
- Personal data (PII)
- Real customer information
- Internal network maps with real IPs (use sanitized versions)

## Allowed Content

### Configuration Templates

- Sanitized `.rsc` files (MikroTik templates)
- Example configurations with placeholders
- Test environment configs (no production secrets)

### Scripts

- Deployment scripts (must not hardcode secrets)
- Validation scripts
- Test automation
- Backup/restore scripts (must sanitize output)

### Documentation

- Architecture diagrams
- Network flow descriptions
- Test plans and results
- Audit reports

## Secret Scanning

This repository uses automated secret scanning:

- GitHub Actions workflow: `.github/workflows/secret-scan.yml`
- Gitleaks or equivalent scanner
- Runs on every commit
- Blocks merges if secrets detected

### Local Scanning

Before committing, run:

```bash
make scan-secrets
```

Or manually:

```bash
grep -RniE --exclude-dir=.git \
  '(BEGIN [A-Z ]*PRIVATE KEY|password[[:space:]]*=|token[[:space:]]*=|secret[[:space:]]*=|api[_-]?key[[:space:]]*=)' \
  . || true
```

## Reporting Security Issues

If you discover a security issue in this repository:

1. **Do NOT open a public issue**
2. Contact the Owner directly
3. Provide details of the exposure
4. Coordinate remediation

## Compliance

This project follows security best practices:

- Principle of least privilege
- Defense in depth
- Secure by default
- Audit trail preservation
- Incident response procedures

All contributors must adhere to these policies.
