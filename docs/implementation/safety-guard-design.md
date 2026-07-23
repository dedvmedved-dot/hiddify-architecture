# Safety Guard Design

**Status:** DRAFT — Stage 04 OFFLINE SKELETON

## Purpose

Prevent accidental production execution from Stage 04 artifacts.

## Implementation

`scripts/safety_guard.py` scans all IaC and automation files for forbidden patterns:

- terraform apply / destroy
- ansible-playbook (without syntax-check/check)
- ssh to remote hosts
- scp / rsync
- kubectl apply / helm install
- systemctl start/stop/restart
- iptables/nftables modifications
- ip route/addr modifications
- curl to non-GitHub external endpoints

## Exit Codes

- 0: No forbidden commands found
- 1: Forbidden commands detected (BLOCKS execution)

## CI Integration

Safety guard runs as a required CI check on every commit.
Failure blocks PR progression.
