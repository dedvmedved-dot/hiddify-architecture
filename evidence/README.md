# Evidence

This directory contains immutable or minimally processed evidence of stage completion.

## Structure

```
evidence/
  stage-00/        - Stage 00 evidence
  stage-01/        - Stage 01 evidence (future)
  ...
```

## Evidence Requirements

Every stage must provide:

1. **Command outputs** — Show work performed
2. **Validation results** — Prove correctness
3. **Timestamps** — UTC timestamps for all evidence
4. **Sanitization** — No secrets in evidence
5. **Indexing** — All evidence indexed in `evidence-index.md`

## Evidence Format

- Plain text preferred (`.txt`, `.md`)
- Screenshots as PNG with descriptive filenames
- Logs with timestamps
- Command output with `$` prompt

## Checksums

For critical evidence files, SHA-256 checksums are provided:

```bash
sha256sum evidence/stage-NN/file.txt
```

## Preservation

Evidence files should not be modified after creation. If correction is needed, create a new file with a version suffix.
