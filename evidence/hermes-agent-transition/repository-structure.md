# Repository Structure

## Top-Level Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview, status, roles, stage-gate |
| `LICENSE` | MIT license |
| `CHANGELOG.md` | Keep a Changelog format |
| `CONTRIBUTING.md` | Branch naming, commits, security, evidence rules |
| `SECURITY.md` | Prohibited content, sanitization, incident response |
| `.gitignore` | Secrets, keys, backups, logs, IDE files |
| `.editorconfig` | UTF-8, LF, final newline, 2-space indent |
| `.gitattributes` | CRLF handling, text auto-detection |
| `Makefile` | validate, lint-markdown, lint-shell, scan-secrets |

## Directory Structure

| Directory | Purpose | Status |
|-----------|---------|--------|
| `docs/` | Approved project documentation | DRAFT (no architecture approved yet) |
| `docs/project/` | Charter, scope, roles, stage-gates, terminology | Stage 00 |
| `docs/requirements/` | Functional, non-functional, constraints, traceability | Stage 00 (placeholder) |
| `docs/architecture/` | System context, logical, physical, DNS, security | Stage 00 (placeholder) |
| `docs/decisions/` | ADR template | Stage 00 (placeholder) |
| `docs/audit/` | Initial concept document (NOT approved architecture) | Stage 00 |
| `docs/testing/` | Strategy, environments, criteria, templates | Stage 00 (placeholder) |
| `docs/operations/` | Deployment, monitoring, backup, rollback | Stage 00 (placeholder) |
| `docs/security/` | Threat model, secrets, hardening, firewall | Stage 00 (placeholder) |
| `stages/` | Stage tasks, reports, acceptance records | Stage 00 complete |
| `stages/stage-00-repository-baseline/` | Stage 00 artifacts | PASSED, CONNECTOR VERIFIED |
| `stages/templates/` | Templates for future stages | Stage 00 |
| `configs/` | Templates and sanitized configs | Placeholder for future stages |
| `configs/mikrotik/` | MikroTik templates/generated | Placeholder |
| `configs/vps1/` | VPS1 templates/generated | Placeholder |
| `configs/vps3/` | VPS3 templates/generated | Placeholder |
| `scripts/` | Bootstrap, deploy, test, rollback, security | Placeholder |
| `inventory/` | Sanitized technical specifications | Placeholder |
| `tests/` | Static, functional, integration, performance, security | Placeholder |
| `evidence/` | Immutable proof of stage completion | Stage 00 evidence present |
| `evidence/stage-00/` | Baseline Stage 00 evidence | VERIFIED |
| `evidence/stage-00-correction-01/` | Corrective action evidence | VERIFIED |
| `evidence/stage-00-reaudit/` | Re-audit evidence | VERIFIED |
| `evidence/stage-00-post-merge/` | Post-merge verification evidence | VERIFIED |
| `reports/` | Summary and audit reports | Placeholder |
| `diagrams/` | Source (Mermaid, PlantUML) and rendered (SVG/PNG) | Placeholder |
| `tools/` | Linting and validation tools | Stage 00 |
| `tools/validation/` | validate-repository.sh | Stage 00 |
| `.github/` | CODEOWNERS, PR template, workflows | Stage 00 |
