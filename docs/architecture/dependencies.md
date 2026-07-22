# Architecture Dependencies

**Status:** DRAFT — OWNER REVIEW REQUIRED

## Internal Dependencies

| Component | Depends On | Type | Criticality |
|-----------|------------|------|-------------|
| Traffic classification | Router hardware, RouterOS | Hard | Critical |
| RU egress | VPS1, RU tunnel | Hard | High |
| INT egress | VPS3, INT tunnel | Hard | High |
| DNS resolution | DNS resolvers, tunnels | Hard | High |
| Monitoring | All components, network | Soft | Medium |
| Backup | Router/VPS access, storage | Soft | Medium |

## External Dependencies

| Dependency | Provider | Impact if Unavailable | Status |
|------------|----------|-----------------------|--------|
| ISP connectivity | ISP | All traffic blocked | UNKNOWN |
| VPS1 hosting | VPS provider | RU egress unavailable | UNKNOWN |
| VPS3 hosting | VPS provider | INT egress unavailable | UNKNOWN |
| DNS upstream resolvers | External | DNS resolution failure | UNKNOWN |
| GitHub (config storage) | GitHub | Configuration changes blocked | Known |

## Version Dependencies

| Software | Min Version | Reason | Status |
|----------|-------------|--------|--------|
| RouterOS | 7.x (TBC) | WireGuard, policy routing | UNKNOWN |
| VPS OS (VPS1) | TBC | VPN software | UNKNOWN |
| VPS OS (VPS3) | TBC | VPN software | UNKNOWN |
