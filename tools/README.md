# Tools

This directory contains project-specific tooling.

## Structure

```
tools/
  lint/            - Linting configuration
  validation/      - Repository validation scripts
```

## Validation Script

The main validation script checks repository structure:

```bash
bash tools/validation/validate-repository.sh
```

Or via Make:

```bash
make validate
```

## Lint Configuration

Linting tools configuration files (if needed).
