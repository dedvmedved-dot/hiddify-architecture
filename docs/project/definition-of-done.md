# Definition of Done

**Status:** DRAFT

A stage is considered complete when ALL of the following criteria are met:

## File Requirements

- [ ] All files are located at the specified paths
- [ ] All required files exist and are non-empty
- [ ] Empty directories are preserved with `.gitkeep`
- [ ] No files exist outside the agreed structure without justification

## Content Requirements

- [ ] Documents do not contradict each other
- [ ] All documents have explicit status (DRAFT or approved)
- [ ] Configurations contain no real secrets
- [ ] All placeholders use `<REPLACE_WITH_SECRET>` format

## Testing Requirements

- [ ] Tests are reproducible
- [ ] Test results are documented in evidence
- [ ] Validation scripts pass successfully

## Evidence Requirements

- [ ] Evidence is available in `evidence/stage-NN/`
- [ ] Evidence is indexed in `evidence-index.md`
- [ ] SHA-256 checksums created where applicable
- [ ] Evidence is sanitized (no secrets)

## Report Requirements

- [ ] Stage report references evidence
- [ ] Report includes commit hash
- [ ] Report includes UTC timestamps
- [ ] Report documents any deviations
- [ ] Report includes rollback information
- [ ] Secret scan results are included

## Git Requirements

- [ ] Commit is available through GitHub
- [ ] Commit message follows conventions
- [ ] Working tree is clean after commit
- [ ] No force push was used
- [ ] History was not rewritten

## Audit Requirements

- [ ] External audit is completed by ChatGPT
- [ ] All blocking findings are resolved
- [ ] Stage is marked PASSED by ChatGPT

## Security Requirements

- [ ] No secrets in any committed files
- [ ] Secret scan returns clean results
- [ ] Security policies are followed
- [ ] `.gitignore` properly configured
