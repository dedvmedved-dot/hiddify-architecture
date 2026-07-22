# Configurations

This directory contains sanitized configuration templates and generated configurations.

## Structure

```text
configs/
  mikrotik/        - MikroTik RouterOS configurations
    templates/     - Configuration templates with placeholders
    generated/     - Generated (sanitized) configurations
  vps1/            - VPS1 (Russian egress) configurations
    templates/
    generated/
  vps3/            - VPS3 (International egress) configurations
    templates/
    generated/
  nftables/        - nftables firewall rules
  routing/         - Routing configuration
  dns/             - DNS configuration
  systemd/         - systemd service files
  monitoring/      - Monitoring configuration
```

## Rules

1. **No real secrets** — Use `<REPLACE_WITH_SECRET>` placeholders
2. **Templates only** — Store parameterized templates
3. **Generated configs** — Sanitized generated configurations
4. **No production backups** — Never commit `.backup` files
5. **Version control** — All changes tracked in Git

## Placeholder Format

```text
<REPLACE_WITH_SECRET>
```

## MikroTik Files

- `.rsc` files are allowed (sanitized templates)
- `.rsc.private` files are forbidden
- `.backup` files are forbidden
