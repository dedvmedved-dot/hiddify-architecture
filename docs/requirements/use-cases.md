# Use Cases

**Status:** DRAFT — OWNER REVIEW REQUIRED

## UC-001 — Russian Egress Access

- **ID:** UC-001
- **Name:** Russian egress access
- **Actors:** End user (STK-005), MikroTik router, VPS1
- **Preconditions:** Traffic classification policy configured; VPS1 reachable; tunnel/proxy active
- **Trigger:** User initiates traffic matching RU egress policy
- **Main flow:** 1. MikroTik classifies traffic → 2. Traffic routed to VPS1 via secure tunnel → 3. VPS1 forwards traffic to destination → 4. Return traffic flows back through same path
- **Alternative flow:** None
- **Failure flow:** VPS1 unreachable → fallback behavior (TO BE DECIDED)
- **Expected result:** Traffic exits through RU IP; session state preserved
- **Security considerations:** Tunnel encryption; no traffic leakage to default ISP route
- **Observability requirements:** Tunnel state, latency, packet loss, bandwidth utilization
- **Open questions:** Fallback behavior (fail-open to ISP vs fail-closed)

## UC-002 — International Egress Access

- **ID:** UC-002
- **Name:** International egress access
- **Actors:** End user (STK-005), MikroTik router, VPS3
- **Preconditions:** Traffic classification policy configured; VPS3 reachable; tunnel/proxy active
- **Trigger:** User initiates traffic matching INT egress policy
- **Main flow:** 1. MikroTik classifies traffic → 2. Traffic routed to VPS3 via secure tunnel → 3. VPS3 forwards traffic to destination → 4. Return traffic flows back through same path
- **Failure flow:** VPS3 unreachable → fallback behavior (TO BE DECIDED)
- **Expected result:** Traffic exits through INT IP; session state preserved
- **Open questions:** Fallback behavior; interaction with RU egress failure

## UC-003 — Automatic Traffic Classification

- **ID:** UC-003
- **Name:** Automatic traffic classification
- **Actors:** MikroTik router
- **Preconditions:** Classification rules configured; address lists populated
- **Trigger:** Any user traffic
- **Main flow:** MikroTik matches traffic against classification policy → assigns egress route
- **Alternative flow:** Traffic matches no rule → default behavior (TO BE DECIDED)
- **Expected result:** Correct egress selection without user intervention
- **Open questions:** Default behavior; domain-based vs IP-based classification

## UC-004 — Manual Policy Override

- **ID:** UC-004
- **Name:** Manual policy override
- **Actors:** Network administrator (STK-004)
- **Preconditions:** Administrator has access; change approval received
- **Trigger:** Administrator needs to change routing for specific traffic
- **Main flow:** Administrator applies override → traffic routing updated → change logged
- **Expected result:** Traffic rerouted per manual policy
- **Security considerations:** Audit trail required; approval required
- **Open questions:** Override mechanism; approval workflow

## UC-005 — Egress Failure Handling

- **ID:** UC-005
- **Name:** Egress failure handling
- **Actors:** MikroTik router, monitoring system
- **Preconditions:** Health checks configured; alert channels active
- **Trigger:** VPS egress unreachable
- **Main flow:** Health check detects failure → alert generated → fallback activated (TO BE DECIDED) → administrator notified
- **Failure flow:** All egresses fail → system behavior (TO BE DECIDED)
- **Expected result:** Graceful degradation; alert delivered
- **Open questions:** Fail-open vs fail-closed; auto-recovery; alert escalation

## UC-006 — DNS Resolution Consistent with Egress

- **ID:** UC-006
- **Name:** DNS resolution consistent with egress
- **Actors:** DNS resolver, MikroTik router
- **Preconditions:** DNS policy configured
- **Trigger:** DNS query from client
- **Main flow:** DNS query classified → sent through appropriate egress → response returned
- **Expected result:** DNS and subsequent traffic use same egress path
- **Security considerations:** No DNS leakage to unintended resolver
- **Open questions:** Split DNS design; caching behavior

## UC-007 — Monitoring and Alerting

- **ID:** UC-007
- **Name:** Monitoring and alerting
- **Actors:** Monitoring system, network administrator
- **Preconditions:** Monitoring agents deployed; thresholds configured
- **Trigger:** Metric crosses threshold or component fails
- **Main flow:** Metric collected → threshold evaluated → alert triggered → administrator responds
- **Expected result:** Timely detection and notification
- **Open questions:** Monitoring platform; alert channels; thresholds

## UC-008 — Configuration Backup

- **ID:** UC-008
- **Name:** Configuration backup
- **Preconditions:** Backup script available; storage accessible
- **Trigger:** Scheduled or manual backup
- **Main flow:** Configuration exported → sanitized → stored → integrity verified
- **Expected result:** Restorable backup with verified integrity
- **Open questions:** Backup frequency; retention; storage location

## UC-009 — Configuration Rollback

- **ID:** UC-009
- **Name:** Configuration rollback
- **Actors:** Network administrator
- **Preconditions:** Backup available; rollback tested
- **Trigger:** Configuration error or failed change
- **Main flow:** Administrator initiates rollback → configuration restored → services verified
- **Expected result:** System restored to known-good state
- **Open questions:** Rollback trigger; verification procedures

## UC-010 — Security Incident Response

- **ID:** UC-010
- **Name:** Security incident response
- **Actors:** Network administrator, Owner
- **Preconditions:** Incident response procedures defined
- **Trigger:** Security event detected
- **Main flow:** Incident detected → classified → contained → investigated → remediated → reported
- **Expected result:** Incident contained; root cause identified
- **Open questions:** Detection mechanisms; escalation; containment procedures

## UC-011 — Planned Maintenance

- **ID:** UC-011
- **Name:** Planned maintenance
- **Actors:** Network administrator, Owner
- **Preconditions:** Maintenance window approved; users notified
- **Trigger:** Scheduled maintenance
- **Main flow:** Administrator performs maintenance → tests → documents → normal operations resume
- **Expected result:** Maintenance completed without unexpected impact
- **Open questions:** Maintenance windows; notification procedures

## UC-012 — New Traffic Category Onboarding

- **ID:** UC-012
- **Name:** New traffic category onboarding
- **Actors:** Owner, network administrator
- **Preconditions:** New traffic requirement identified
- **Trigger:** Owner requests new traffic category
- **Main flow:** Requirement documented → classification rules defined → tested → deployed
- **Expected result:** New traffic correctly routed per policy
- **Open questions:** Approval workflow; testing procedures
