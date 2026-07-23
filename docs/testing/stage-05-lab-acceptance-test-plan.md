# Stage 05 Lab Acceptance Test Plan

**Status:** Stage 05 — PLAN ONLY

## Test Specifications

### S05-CFG-001 — Lab config schema validation

- **ID:** S05-CFG-001
- **Title:** Lab config schema validation
- **Category:** cfg
- **Objective:** Lab config schema validation
- **Expected result:** Config loads with lab_environment=true
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-CFG-002 — Production classification rejection

- **ID:** S05-CFG-002
- **Title:** Production classification rejection
- **Category:** cfg
- **Objective:** Production classification rejection
- **Expected result:** production_environment=false enforced
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-CFG-003 — Real IP rejection

- **ID:** S05-CFG-003
- **Title:** Real IP rejection
- **Category:** cfg
- **Objective:** Real IP rejection
- **Expected result:** Only RFC 5737 documentation IPs allowed
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-CFG-004 — Non-example domain rejection

- **ID:** S05-CFG-004
- **Title:** Non-example domain rejection
- **Category:** cfg
- **Objective:** Non-example domain rejection
- **Expected result:** Only example.invalid allowed
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-PF-001 — Valid lab preflight

- **ID:** S05-PF-001
- **Title:** Valid lab preflight
- **Category:** pf
- **Objective:** Valid lab preflight
- **Expected result:** preflight validator exits 0
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-PF-002 — Missing role rejection

- **ID:** S05-PF-002
- **Title:** Missing role rejection
- **Category:** pf
- **Objective:** Missing role rejection
- **Expected result:** Missing traffic-classifier detected
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-PF-003 — Duplicate address rejection

- **ID:** S05-PF-003
- **Title:** Duplicate address rejection
- **Category:** pf
- **Objective:** Duplicate address rejection
- **Expected result:** Duplicate IP detected
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-PF-004 — Missing rollback mapping rejection

- **ID:** S05-PF-004
- **Title:** Missing rollback mapping rejection
- **Category:** pf
- **Objective:** Missing rollback mapping rejection
- **Expected result:** Rollback map file exists
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-ANS-001 — Site syntax-check

- **ID:** S05-ANS-001
- **Title:** Site syntax-check
- **Category:** ans
- **Objective:** Site syntax-check
- **Expected result:** ansible-playbook --syntax-check exits 0
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-ANS-002 — All playbooks syntax-check

- **ID:** S05-ANS-002
- **Title:** All playbooks syntax-check
- **Category:** ans
- **Objective:** All playbooks syntax-check
- **Expected result:** 4/4 playbooks pass syntax
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-ANS-003 — Check-mode local only

- **ID:** S05-ANS-003
- **Title:** Check-mode local only
- **Category:** ans
- **Objective:** Check-mode local only
- **Expected result:** --check --connection=local succeeds
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-ANS-004 — Normal execution rejected

- **ID:** S05-ANS-004
- **Title:** Normal execution rejected
- **Category:** ans
- **Objective:** Normal execution rejected
- **Expected result:** ansible_connection=local enforced
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-ANS-005 — Remote inventory rejected

- **ID:** S05-ANS-005
- **Title:** Remote inventory rejected
- **Category:** ans
- **Objective:** Remote inventory rejected
- **Expected result:** No ansible_connection=ssh
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-TPL-001 — WireGuard template

- **ID:** S05-TPL-001
- **Title:** WireGuard template
- **Category:** tpl
- **Objective:** WireGuard template
- **Expected result:** Template directory exists
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-TPL-002 — DNS template

- **ID:** S05-TPL-002
- **Title:** DNS template
- **Category:** tpl
- **Objective:** DNS template
- **Expected result:** Template directory exists
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-TPL-003 — Reverse proxy template

- **ID:** S05-TPL-003
- **Title:** Reverse proxy template
- **Category:** tpl
- **Objective:** Reverse proxy template
- **Expected result:** Template directory exists
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-TPL-004 — Certificate template

- **ID:** S05-TPL-004
- **Title:** Certificate template
- **Category:** tpl
- **Objective:** Certificate template
- **Expected result:** Template directory exists
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-TPL-005 — Logging template

- **ID:** S05-TPL-005
- **Title:** Logging template
- **Category:** tpl
- **Objective:** Logging template
- **Expected result:** Template directory exists
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-TPL-006 — Monitoring template

- **ID:** S05-TPL-006
- **Title:** Monitoring template
- **Category:** tpl
- **Objective:** Monitoring template
- **Expected result:** Template directory exists
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-TPL-007 — Backup template

- **ID:** S05-TPL-007
- **Title:** Backup template
- **Category:** tpl
- **Objective:** Backup template
- **Expected result:** Template directory exists
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-TPL-008 — Deterministic rendering

- **ID:** S05-TPL-008
- **Title:** Deterministic rendering
- **Category:** tpl
- **Objective:** Deterministic rendering
- **Expected result:** SHA-256 matches on re-render
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-SEC-001 — Private key detection

- **ID:** S05-SEC-001
- **Title:** Private key detection
- **Category:** sec
- **Objective:** Private key detection
- **Expected result:** PRIVATE KEY block detected
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-SEC-002 — Token detection

- **ID:** S05-SEC-002
- **Title:** Token detection
- **Category:** sec
- **Objective:** Token detection
- **Expected result:** ghp_ pattern detected
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-SEC-003 — Password assignment detection

- **ID:** S05-SEC-003
- **Title:** Password assignment detection
- **Category:** sec
- **Objective:** Password assignment detection
- **Expected result:** password pattern detected
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-SG-001 — Terraform apply rejection

- **ID:** S05-SG-001
- **Title:** Terraform apply rejection
- **Category:** sg
- **Objective:** Terraform apply rejection
- **Expected result:** terraform apply detected
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-SG-002 — Remote Ansible rejection

- **ID:** S05-SG-002
- **Title:** Remote Ansible rejection
- **Category:** sg
- **Objective:** Remote Ansible rejection
- **Expected result:** ansible_connection=ssh detected
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-SG-003 — SSH command rejection

- **ID:** S05-SG-003
- **Title:** SSH command rejection
- **Category:** sg
- **Objective:** SSH command rejection
- **Expected result:** ssh command detected
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-SG-004 — Network modification rejection

- **ID:** S05-SG-004
- **Title:** Network modification rejection
- **Category:** sg
- **Objective:** Network modification rejection
- **Expected result:** iptables command detected
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-PLN-001 — Deployment plan generation

- **ID:** S05-PLN-001
- **Title:** Deployment plan generation
- **Category:** pln
- **Objective:** Deployment plan generation
- **Expected result:** Plan exits 0
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-PLN-002 — Deterministic plan output

- **ID:** S05-PLN-002
- **Title:** Deterministic plan output
- **Category:** pln
- **Objective:** Deterministic plan output
- **Expected result:** Two runs produce identical JSON
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-PLN-003 — Plan contains rollback mapping

- **ID:** S05-PLN-003
- **Title:** Plan contains rollback mapping
- **Category:** pln
- **Objective:** Plan contains rollback mapping
- **Expected result:** Plan references rollback steps
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-PLN-004 — Plan contains validation mapping

- **ID:** S05-PLN-004
- **Title:** Plan contains validation mapping
- **Category:** pln
- **Objective:** Plan contains validation mapping
- **Expected result:** Plan contains validation references
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-RB-001 — Rollback map completeness

- **ID:** S05-RB-001
- **Title:** Rollback map completeness
- **Category:** rb
- **Objective:** Rollback map completeness
- **Expected result:** All required fields populated
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-TRC-001 — Traceability completeness

- **ID:** S05-TRC-001
- **Title:** Traceability completeness
- **Category:** trc
- **Objective:** Traceability completeness
- **Expected result:** Required columns present, refs valid
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-ID-001 — Duplicate Test ID detection

- **ID:** S05-ID-001
- **Title:** Duplicate Test ID detection
- **Category:** id
- **Objective:** Duplicate Test ID detection
- **Expected result:** Duplicate IDs detected
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED
### S05-IT-001 — Full integration simulation

- **ID:** S05-IT-001
- **Title:** Full integration simulation
- **Category:** it
- **Objective:** Full integration simulation
- **Expected result:** All gates pass, simulation exits 0
- **Test implementation:** `tests/stage05/test_all.py`
- **CI step:** stage-05-validation
- **Status:** IMPLEMENTED

