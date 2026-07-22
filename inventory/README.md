# Inventory

This directory contains sanitized technical specifications for all infrastructure nodes.

## Structure

```text
inventory/
  templates/       - Inventory templates
  mikrotik/        - MikroTik router specifications
  vps1/            - VPS1 (Russian egress) specifications
  vps3/            - VPS3 (International egress) specifications
```

## Rules

1. **No real secrets** — Sanitize all sensitive information
2. **Technical specs only** — Hardware, software, network details
3. **Placeholders** — Use `<REPLACE_WITH_SECRET>` for credentials
4. **Up to date** — Keep inventory current with actual infrastructure

## Information to Include

- Hostname / IP address (sanitized if sensitive)
- OS version
- Installed software versions
- Network interfaces
- Resource specifications (CPU, RAM, disk)
- Service configurations (sanitized)
