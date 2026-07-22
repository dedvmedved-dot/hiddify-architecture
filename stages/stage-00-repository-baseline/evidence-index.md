# Stage 00 — Evidence Index

## Evidence Files

| Evidence ID | File | Host | Command/Test | Timestamp UTC | SHA-256 | Sanitized | Description |
| ----------- | ---- | ---- | ------------ | ------------- | ------- | --------- | ----------- |
| EV-00-001 | evidence/stage-00/repository-tree.txt | hermes-agent | find . -type f -not -path './.git/*' -print \| LC_ALL=C sort | PENDING | PENDING | Yes | Complete file listing of repository |
| EV-00-002 | evidence/stage-00/git-status.txt | hermes-agent | git status --short; git status --branch | PENDING | PENDING | Yes | Git working tree status after commit |
| EV-00-003 | evidence/stage-00/git-log.txt | hermes-agent | git log -1 --decorate --stat; git show --summary --format=fuller HEAD | PENDING | PENDING | Yes | Last commit details |
| EV-00-004 | evidence/stage-00/markdown-files.txt | hermes-agent | find . -type f -name '*.md' -not -path './.git/*' -print \| LC_ALL=C sort | PENDING | PENDING | Yes | All Markdown files listing |
| EV-00-005 | evidence/stage-00/secret-scan.txt | hermes-agent | grep -RniE --exclude-dir=.git '(BEGIN.*PRIVATE KEY\|password\|token\|secret\|api[_-]?key)' . | PENDING | PENDING | Yes | Secret scan results |
| EV-00-006 | evidence/stage-00/validation.txt | hermes-agent | bash tools/validation/validate-repository.sh | PENDING | PENDING | Yes | Repository validation results |
| EV-00-007 | evidence/stage-00/checksums.sha256 | hermes-agent | find evidence/stage-00 -type f ! -name 'checksums.sha256' -print0 \| LC_ALL=C sort -z \| xargs -0 sha256sum | PENDING | N/A | Yes | SHA-256 checksums of evidence files |

## Notes

- All evidence collected on hermes-agent host
- Timestamps in UTC
- All evidence sanitized (no secrets)
- Checksums generated after all other evidence files created
