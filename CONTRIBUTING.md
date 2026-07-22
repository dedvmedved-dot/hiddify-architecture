# Contributing to Hiddify Architecture Project

## Branch Naming Convention

Use the following patterns:

- `stage/NN-short-name` — Stage implementation work
- `fix/short-description` — Bug fixes and corrections
- `docs/short-description` — Documentation updates

Examples:
- `stage/01-requirements-analysis`
- `fix/correct-typo-in-readme`
- `docs/add-network-diagram`

## Commit Messages

Follow conventional commits:

```text
type(scope): brief description

Longer explanation if needed.

Refs: #issue-number (if applicable)
```

Types:
- `feat` — New features
- `fix` — Bug fixes
- `docs` — Documentation changes
- `style` — Formatting, no code change
- `refactor` — Code restructuring
- `test` — Adding tests
- `chore` — Maintenance tasks
- `stage` — Stage-specific work

Examples:
```
chore(repo): establish project baseline and governance structure
docs(architecture): add initial system context diagram
stage(01): complete requirements analysis
```

## Security Rules

### NEVER commit:

- Passwords, tokens, or API keys
- Private keys (SSH, WireGuard, TLS)
- SSH host keys
- Cookies or session files
- `.env` files (except `.env.example` with placeholders)
- MikroTik backup files
- Configuration exports containing secrets
- Database connection strings with credentials

### Safe placeholders:

Use `<REPLACE_WITH_SECRET>` for all secret values.

Example:
```yaml
api_key: <REPLACE_WITH_SECRET>
password: <REPLACE_WITH_SECRET>
private_key: <REPLACE_WITH_SECRET>
```

### If you accidentally commit a secret:

1. **Immediately** rotate the compromised credential
2. Remove from Git history (requires force push — coordinate with team)
3. Document incident in stage report
4. Add pattern to `.gitignore`

## Evidence Rules

Every stage must include evidence in `evidence/stage-NN/`:

- Command outputs
- Test results
- Validation logs
- Screenshots (if applicable)
- Checksums of critical files

Evidence must be:
- Timestamped (UTC)
- Reproducible
- Sanitized (no secrets)
- Indexed in `evidence-index.md`

## Architecture Changes

All architectural decisions must:

1. Be documented in ADR (Architecture Decision Record)
2. Include context, decision, and consequences
3. Be reviewed by ChatGPT architect
4. Be approved before implementation
5. Reference supporting evidence

Do NOT make architectural changes outside the stage-gate process.

## External Audit Requirement

Before starting any new stage:

1. Current stage must be marked **PASSED** by ChatGPT
2. All blocking findings must be resolved
3. Evidence must be complete and accessible
4. Commit must be available via GitHub

Hermes + Qwen cannot self-approve stages.

## Stage 00 Exception

Stage 00 commits directly to `main` because the repository is empty.

Starting from Stage 01, use feature branches and pull requests when technically possible.

## Questions?

Direct questions to the Owner, who will coordinate with ChatGPT architect.
