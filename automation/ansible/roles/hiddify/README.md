# Hiddify Ansible Role

Installs and configures Hiddify proxy panel in lab environment.

**Execution Mode:** plan_only by default. Requires explicit deployment authorization.

## Requirements
- Ubuntu 22.04+ / Debian 12+
- x86_64 architecture
- 2+ GB RAM, 10+ GB free disk
- Docker runtime
- Owner Input complete
- Safety Gate approved

## Safety
All real installation logic is gated behind:
- `hiddify_deployment_enabled: true`
- `hiddify_remote_execution_enabled: true`
- `STAGE06_LAB_DEPLOYMENT_APPROVED=YES`
