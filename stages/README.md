# Project Stages

This directory contains all stage artifacts: tasks, reports, acceptance records, and evidence indexes.

## Stage Structure

Each stage follows this structure:

```text
stages/stage-NN-name/
  task.md           - Stage requirements (from ChatGPT)
  report.md         - Implementation report (from Hermes)
  acceptance.md     - Audit result (from ChatGPT)
  evidence-index.md - Index of evidence files
```

## Stage Naming Convention

```text
stage-NN-short-name
```

Examples:

- `stage-00-repository-baseline`
- `stage-01-requirements-analysis`
- `stage-02-architecture-design`

## Current Stage

**Stage 00 — Repository Baseline and Governance Structure**

See: `stage-00-repository-baseline/`

## Templates

Stage templates are available in `stages/templates/`:

- `task-template.md`
- `report-template.md`
- `acceptance-template.md`
- `evidence-index-template.md`

## Stage Status

Check each stage's `acceptance.md` for current status:

- NOT STARTED
- IN PROGRESS
- READY FOR EXTERNAL AUDIT
- FAILED
- CONDITIONAL PASS
- PASSED
- CONNECTOR VERIFIED
