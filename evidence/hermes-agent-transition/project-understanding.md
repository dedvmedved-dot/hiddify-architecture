# Project Understanding

## Project Goal

Design and document a secure, auditable network access architecture using Russian and international egress points. The solution must support split routing, maintain security boundaries, and provide comprehensive testing and rollback capabilities.

The project name "hiddify-architecture" does not commit to using Hiddify — all technology choices remain open until evaluated through the stage-gate process.

## Current Stage

**Stage 00 — Repository Baseline and Governance Structure** is complete:
- Status: PASSED, CONNECTOR VERIFIED
- Merge commit: `3ee42503689f17360efd08a956f3b705f825b585`
- Current main HEAD: `dafa6aee1d377393e271879c0463c41359894a58`

**Stage 01 has not been started.**
Its scope must be provided by ChatGPT in a separate assignment.

## Completed Work

- Repository structure created (124 files)
- All required root files (README, LICENSE, CHANGELOG, CONTRIBUTING, SECURITY, .gitignore, .editorconfig, .gitattributes, Makefile)
- Documentation framework in docs/ (project, requirements, architecture, audit, testing, operations, security)
- Stage templates (task, report, acceptance, evidence-index)
- GitHub Actions workflows (markdown-lint, shellcheck, secret-scan, repository-validation)
- Repository validation script (153 PASS, 0 FAIL, 0 WARN)
- Stage 00 artifacts with evidence
- External audit completed, findings addressed, PR #1 merged

## Operational Model

```text
ChatGPT (Architect/Auditor)
    ↓ defines task
Owner (Sponsor)
    ↓ transfers task
Hermes (Implementor)
    ↓ executes, commits, pushes
Owner
    ↓ transfers commit SHA
ChatGPT (Auditor)
    ↓ audits, assigns PASSED/FAILED
Owner
    ↓ decides next action
```

## Roles

- **ChatGPT:** Lead architect, critic, task setter, external auditor, stage acceptance authority
- **Hermes:** Implementation, evidence collection, configuration, testing, reporting, Git operations
- **Owner:** Access provider, task transfer, business decisions, production authorization

Hermes does NOT have authority to assign PASSED status to any stage.

## Evidence Requirements

Every stage must provide evidence in `evidence/stage-NN/`:
- Command outputs showing work performed
- Validation results
- Secret scan results
- File listings
- Checksums
- Evidence index

Evidence must be timestamped (UTC), reproducible, sanitized (no secrets), and indexed.

## Security Rules

- NEVER commit passwords, tokens, keys, SSH host keys, cookies, .env files, MikroTik backups
- Use `<REPLACE_WITH_SECRET>` placeholders
- If secret leaked: rotate immediately, remove from history, document incident
- Automated secret scanning via Gitleaks in CI
- All configs must be sanitized before commit

## Expected Next Step

Stage 01 scope must be provided by ChatGPT. No implementation work should begin until:
1. Current onboarding verification is complete
2. Stage 01 task is defined by ChatGPT
3. Stage 00 remains PASSED/CONNECTOR VERIFIED
