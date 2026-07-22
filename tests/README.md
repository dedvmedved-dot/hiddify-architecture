# Tests

This directory contains test scenarios and test automation.

## Structure

```text
tests/
  static/          - Static analysis tests
  functional/      - Functional tests
  integration/     - Integration tests
  performance/     - Performance tests
  resilience/      - Resilience and failover tests
  security/        - Security tests
  acceptance/      - Acceptance tests
```

## Running Tests

```bash
# Run all tests
make validate

# Run specific test category
bash tests/static/run-all.sh
```

## Test Framework

- Shell scripts use Bats (Bash Automated Testing System) where applicable
- Python tests use pytest
- Static analysis uses markdownlint, shellcheck, gitleaks

## Test Requirements

1. All tests must be reproducible
2. Test data must not contain real secrets
3. Tests must document expected results
4. Failed tests must provide clear error messages
