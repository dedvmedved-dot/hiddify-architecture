# GitHub Actions Workflow Status — Stage 00 Re-Audit

**Checked**: 2026-07-22 02:01 UTC
**Commit**: `70691a1f6b9467af1c1f11acee6e471689b8ff3b`
**Branch**: `fix/stage-00-audit-findings`

## Latest PR-triggered Runs

| Workflow | Run ID | Conclusion | Status | Created |
|----------|--------|------------|--------|---------|
| Markdown Lint | 29883806956 | **failure** | completed | 2026-07-22T01:41:57Z |
| ShellCheck | 29883806984 | success | completed | 2026-07-22T01:41:57Z |
| Secret Scan | 29883806954 | success | completed | 2026-07-22T01:41:57Z |
| Repository Validation | 29883806955 | success | completed | 2026-07-22T01:41:57Z |

## Failure Details

### Markdown Lint (Run 29883806956)

- **Error**: 4 × MD034/no-bare-urls
- **File**: `evidence/stage-00-correction-01/ci-status.md`
- **Lines**: 11, 12, 13, 14 — bare URLs in markdown table
- **Fix applied**: URLs wrapped in `<...>`, status updated to PARTIAL PASS
- **Root cause**: This file was added in commit `70691a1` and its bare URLs caused its own CI failure

## Earlier workflow_dispatch Runs (commit `4df664c`)

All 4 workflows passed on commit `4df664c` via `workflow_dispatch`:
- Markdown Lint: success (Run 29883661641)
- ShellCheck: success (Run 29883713821)
- Secret Scan: success (Run 29883661597)
- Repository Validation: success (Run 29883662484)
