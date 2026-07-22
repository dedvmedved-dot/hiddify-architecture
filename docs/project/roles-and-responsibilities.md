# Roles and Responsibilities

**Status:** DRAFT

## ChatGPT

**Role:** Lead Architect, Critic, Task Setter, External Auditor, Stage Acceptance Authority

### Responsibilities

- Define architectural direction and standards
- Set tasks for each stage
- Review and critique implementation
- Perform external audit of completed stages
- Assign stage status (PASSED, FAILED, CONDITIONAL PASS)
- Approve Architecture Decision Records
- Identify risks and gaps in the approach

### Authority

- Sole authority to assign PASSED status to stages
- Final say on architectural decisions
- Can block stage progression if criteria not met

## Hermes + Qwen 3.7 Max

**Role:** Implementation Agent

### Responsibilities

- Execute stage tasks as defined by ChatGPT
- Collect evidence of implementation
- Create configurations (sanitized)
- Perform testing
- Generate reports
- Commit and push to GitHub
- Maintain repository structure

### Limitations

- **Hermes + Qwen does NOT have authority to assign PASSED status**
- Cannot make architectural decisions independently
- Must follow stage-gate process strictly
- Cannot begin next stage without PASSED status

## Owner

**Role:** Project Sponsor and Decision Maker

### Responsibilities

- Provide access to infrastructure (SSH, credentials)
- Transfer tasks from ChatGPT to Hermes
- Provide source data and requirements
- Transfer commit hashes between agents
- Make business decisions
- Authorize production changes
- Review and approve project charter

### Authority

- Final business decision maker
- Controls access to production infrastructure
- Can override technical decisions for business reasons

## Interaction Model

```text
ChatGPT (Architect)
    ↓ defines task
Owner (Sponsor)
    ↓ transfers task
Hermes (Implementor)
    ↓ executes, commits
Owner (Sponsor)
    ↓ transfers commit hash
ChatGPT (Auditor)
    ↓ audits, assigns status
Owner (Sponsor)
    ↓ decides next action
```

## Separation of Concerns

| Concern | Responsible | Authority |
|---------|-------------|-----------|
| Architecture | ChatGPT | ChatGPT |
| Implementation | Hermes | ChatGPT (review) |
| Business decisions | Owner | Owner |
| Infrastructure access | Owner | Owner |
| Evidence collection | Hermes | ChatGPT (audit) |
| Stage acceptance | ChatGPT | ChatGPT |
| Production deployment | Owner | Owner |
