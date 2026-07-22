# Assumptions

**Status:** DRAFT

## Infrastructure Assumptions

1. VPS1 and VPS3 have stable network connectivity
2. MikroTik router supports required features (policy-based routing, firewall)
3. VPS instances run modern Linux (Ubuntu/Debian)
4. Sufficient bandwidth is available on all links

## Process Assumptions

1. ChatGPT provides timely architectural review
2. Owner transfers tasks and commit hashes promptly
3. Hermes has SSH access to all infrastructure
4. GitHub repository is accessible to all parties

## Technical Assumptions

1. WireGuard or similar modern VPN protocol will be evaluated
2. DNS can be managed through standard tools
3. nftables or iptables available on VPS instances
4. Systemd is the init system on VPS instances

## Timeline Assumptions

1. Stages proceed sequentially
2. Each stage may take multiple sessions
3. Evidence collection adds overhead to each stage

---

*Assumptions to be validated during Stage 01.*
