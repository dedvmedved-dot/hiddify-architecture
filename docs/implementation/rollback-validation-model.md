# Rollback Validation Model

**Status:** DRAFT — Stage 04 OFFLINE SKELETON

## Model Overview

Offline rollback model for Stage 04 skeleton. Covers each future deployment step
with pre-checks, triggers, rollback actions, and validation.

## Rollback Steps

| Step ID | Component | Pre-Check | Rollback Action | Test |
|---------|-----------|-----------|-----------------|------|
| RB-01 | Router config | Config export | Restore from backup | S04-IT-002 |
| RB-02 | VPS1 config | Config backup | Revert configuration | S04-IT-002 |
| RB-03 | VPS3 config | Config backup | Revert configuration | S04-IT-002 |
| RB-04 | RU tunnel | Tunnel status check | Disable tunnel interface | S04-IT-002 |
| RB-05 | INT tunnel | Tunnel status check | Disable tunnel interface | S04-IT-002 |
| RB-06 | DNS routing | DNS resolution test | Remove DNS routing rules | S04-IT-002 |
| RB-07 | Policy routing | Routing table export | Remove policy routes | S04-IT-002 |

## Machine-Readable Model

See `iac/tests/fixtures/rollback-model.example.yml`.

## Validation Test

**S04-IT-002** validates completeness of rollback model without executing rollback.
