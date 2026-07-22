# IaC Skeleton Overview

**Status:** DRAFT — Stage 04 OFFLINE SKELETON

## Purpose

This document describes the Infrastructure-as-Code skeleton created in Stage 04.
All artifacts are offline validation skeletons only — no production deployment.

## Structure

```text
iac/
  schemas/config-schema.json    — JSON Schema for configuration validation
  examples/config.example.yml   — Example configuration (RFC 5737 docs IPs only)
  modules/                       — Module skeletons (future)
  validation/                    — Validation rules
  tests/                         — Test fixtures

automation/
  ansible/                       — Ansible skeleton (offline syntax-check only)
  scripts/                       — Automation scripts (validate-only mode)

scripts/
  validate_stage04.py            — Offline validation CLI
  safety_guard.py                — Forbidden command scanner

tests/stage04/                   — Unit tests
```

## Safety Flags

All example configurations enforce safety flags = false:

- deployment_enabled: false
- production_mode: false
- allow_remote_execution: false
- allow_network_changes: false
- allow_secret_material: false

Any configuration with safety flags set to true is rejected by validation.

## Design Decisions

- ADR-001: Layered architecture reflected in module boundaries
- ADR-002: WireGuard tunnel configuration skeleton
- ADR-003: Policy-based routing configuration skeleton
- ADR-005: Security zones reflected in host roles
