# Stage-Gate Process

**Status:** DRAFT

## Stage Statuses

| Status | Description |
|--------|-------------|
| `NOT STARTED` | Stage defined but work not begun |
| `IN PROGRESS` | Hermes actively working on the stage |
| `READY FOR EXTERNAL AUDIT` | Work complete, awaiting ChatGPT review |
| `FAILED` | Critical issues found, requires rework |
| `CONDITIONAL PASS` | Minor issues found, can proceed with fixes |
| `PASSED` | Approved by ChatGPT external auditor |
| `CONNECTOR VERIFIED` | Verified via GitHub connector by ChatGPT |

## Stage Transition Rules

### To begin a stage:

1. Previous stage must be `PASSED` or `CONNECTOR VERIFIED`
2. Stage task document must be available
3. Owner must transfer the task to Hermes

### To complete a stage:

1. All required artifacts must be created
2. Evidence must be collected and indexed
3. Stage report must be written with commit hash
4. All tests must pass
5. Secret scan must be clean
6. Commit must be pushed to GitHub

### To receive PASSED status:

1. ChatGPT must review the commit via GitHub connector
2. All blocking findings must be resolved
3. ChatGPT must explicitly assign PASSED status

## Hermes + Qwen Limitations

```text
Hermes + Qwen не имеет права самостоятельно присваивать стадии статус PASSED.
```

This rule is absolute and cannot be overridden by Hermes.

## Stage Structure

Each stage follows:

```text
stages/stage-NN-name/
  task.md           - Stage requirements (from ChatGPT)
  report.md         - Implementation report (from Hermes)
  acceptance.md     - Audit result (from ChatGPT)
  evidence-index.md - Index of evidence files
```

## Evidence Requirements

Every stage must provide:
- Command outputs showing work performed
- Validation results
- Secret scan results
- File listings
- Checksums where applicable

## Rollback

Every stage must document:
- What was changed
- How to reverse the changes
- Git revert/restore commands

## Escalation

If Hermes encounters:
- **Technical blocker:** Document in report, notify Owner
- **Ambiguity in task:** Ask Owner for clarification (via ChatGPT)
- **Security concern:** Stop immediately, document, notify Owner
- **Scope question:** Check task.md, if unclear, ask Owner
