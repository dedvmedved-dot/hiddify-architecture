# Scripts

This directory contains executable and library scripts for the project.

## Structure

```text
scripts/
  bootstrap/       - Initial setup scripts
  deploy/          - Deployment scripts
  validation/      - Validation and testing scripts
  testing/         - Test automation
  rollback/        - Rollback procedures
  inventory/       - Inventory collection
  security/        - Security scanning and hardening
```

## Script Requirements

Every shell script must:

1. Use `#!/usr/bin/env bash` shebang
2. Use `set -Eeuo pipefail` where possible
3. Return non-zero exit code on error
4. Include a comment describing its purpose
5. Pass ShellCheck validation

## Running Scripts

```bash
# Validate all scripts

make lint-shell

# Run specific script

bash scripts/deploy/deploy-vps1.sh
```

## Security

- Scripts must not hardcode secrets
- Use environment variables or config files
- Sanitize all output before logging
