# Integration Test Plan

**Status:** DRAFT — OWNER REVIEW REQUIRED

## IT-01 — End-to-End RU Egress

- **Precondition:** RU tunnel active, routing policy deployed
- **Steps:** Client → DNS resolve RU domain → TCP connection → verify egress IP
- **Expected:** Connection completes; source IP = VPS1; DNS via RU resolver
- **Verification:** Check connection logs, traceroute, IP check service

## IT-02 — End-to-End INT Egress

- **Precondition:** INT tunnel active, routing policy deployed
- **Steps:** Client → DNS resolve INT domain → TCP connection → verify egress IP
- **Expected:** Connection completes; source IP = VPS3; DNS via INT resolver
- **Verification:** Check connection logs, traceroute, IP check service

## IT-03 — DNS Leak Prevention

- **Precondition:** All tunnels and DNS configured
- **Steps:** Capture DNS traffic on router WAN interface
- **Expected:** No DNS queries to ISP resolver; all DNS through tunnels
- **Verification:** Packet capture on WAN interface

## IT-04 — Traffic Leak Prevention

- **Precondition:** Routing policy deployed
- **Steps:** Send RU-classified traffic; capture on WAN and INT tunnel
- **Expected:** No RU traffic on WAN or INT tunnel
- **Verification:** Packet capture, connection tracking

## IT-05 — Session Persistence

- **Precondition:** Long-lived connection through RU egress
- **Steps:** Establish connection; verify all packets use same path
- **Expected:** All packets of session follow same egress
- **Verification:** Connection tracking table

## IT-06 — Tunnel Failover

- **Precondition:** RU tunnel active
- **Steps:** Disable RU tunnel; send RU-classified traffic
- **Expected:** Behavior per failover policy (TO BE DECIDED)
- **Verification:** Traffic path observation

## IT-07 — DNS Failover

- **Precondition:** DNS configured
- **Steps:** Disable primary DNS resolver; send DNS query
- **Expected:** Fallback resolver used; resolution succeeds or fails per policy
- **Verification:** DNS query logs

## IT-08 — Concurrent Sessions

- **Precondition:** All systems operational
- **Steps:** Generate N concurrent connections through each egress
- **Expected:** All connections succeed within performance targets
- **Verification:** Connection counters, resource utilization
