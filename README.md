# Hiddify Architecture Project

**Status:** DRAFT

**⚠️ WARNING:** This repository is in active development. The architecture has NOT been approved. No implementation work should begin until Stage 01 is marked PASSED by external auditor.

## Project Goal

Design and document a secure, auditable network access architecture using Russian and international egress points. The solution must support split routing, maintain security boundaries, and provide comprehensive testing and rollback capabilities.

## Current Stage

**Stage 00 — Repository Baseline and Governance Structure**

This stage establishes the foundational repository structure, governance processes, and documentation templates. No architectural decisions have been made.

## Roles

### ChatGPT
- Lead architect and critic
- Task definition and assignment
- External auditor
- Stage acceptance authority

### Hermes + Qwen 3.7 Max
- Implementation
- Evidence collection
- Configuration creation
- Testing
- Report generation
- Git commit and push

### Owner
- Provides access and credentials
- Transfers tasks to Hermes
- Provides source data
- Transfers commit hashes
- Makes business decisions
- Authorizes production changes

**Important:** Hermes + Qwen does NOT have authority to assign PASSED status to any stage.

## Stage-Gate Process

Each stage follows this workflow:

1. **NOT STARTED** → Stage defined but work not begun
2. **IN PROGRESS** → Hermes actively working
3. **READY FOR EXTERNAL AUDIT** → Work complete, awaiting review
4. **FAILED** → Critical issues found, requires rework
5. **CONDITIONAL PASS** → Minor issues, can proceed with fixes
6. **PASSED** → Approved by ChatGPT external auditor
7. **CONNECTOR VERIFIED** → Verified via GitHub connector

Transition to next stage requires: **PASSED** or **CONNECTOR VERIFIED**

## Repository Structure

```
docs/              - Project documentation (DRAFT until approved)
stages/            - Stage tasks, reports, and acceptance records
configs/           - Templates and sanitized configurations
scripts/           - Executable scripts for deployment and testing
inventory/         - Sanitized technical specifications
tests/             - Test scenarios and automation
evidence/          - Immutable proof of stage completion
reports/           - Summary and audit reports
diagrams/          - Architecture diagrams (source and rendered)
tools/             - Linting and validation tools
.github/           - GitHub Actions workflows and templates
```

## Rules for Stage Progression

1. Complete all required artifacts for current stage
2. Generate comprehensive evidence
3. Create stage report with commit hash
4. Submit for external audit (ChatGPT)
5. Address any blocking findings
6. Receive PASSED status
7. Only then begin next stage

## Starting Point

This project begins with an initial concept document stored in `docs/audit/initial-concept.md`. This document is **NOT** an approved architecture — it is a starting point for analysis and refinement.

The repository name "hiddify-architecture" does not commit us to using Hiddify. All technology choices remain open until evaluated and approved through the stage-gate process.

## Stage 00 Report

See: `stages/stage-00-repository-baseline/report.md`

## License

MIT License (subject to owner review and approval)
