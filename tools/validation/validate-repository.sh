#!/usr/bin/env bash
# Repository validation script for Stage 00+
# Checks required files, directories, prohibited files, empty Markdown files,
# Stage 00 artifacts, trailing whitespace, .gitkeep presence, task.md completeness,
# evidence integrity, and report consistency.
# Exit 0 only if all checks pass.

set -Eeuo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"

PASS_COUNT=0
FAIL_COUNT=0
WARN_COUNT=0

pass() {
  echo "PASS: $1"
  PASS_COUNT=$((PASS_COUNT + 1))
}

fail() {
  echo "FAIL: $1"
  FAIL_COUNT=$((FAIL_COUNT + 1))
}

warn() {
  echo "WARN: $1"
  WARN_COUNT=$((WARN_COUNT + 1))
}

echo "========================================"
echo "Repository Validation"
echo "========================================"
echo "Repository root: $REPO_ROOT"
echo "Date (UTC): $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
echo "========================================"
echo ""

# -------------------------------------------------------------------
# CHECK 1: Required root files
# -------------------------------------------------------------------
echo "--- Check 1: Required root files ---"
REQUIRED_FILES=(
  "README.md"
  "LICENSE"
  "CHANGELOG.md"
  "CONTRIBUTING.md"
  "SECURITY.md"
  ".gitignore"
  ".editorconfig"
  ".gitattributes"
  "Makefile"
)

for file in "${REQUIRED_FILES[@]}"; do
  if [ -f "$file" ]; then
    pass "Required file exists: $file"
  else
    fail "Missing required file: $file"
  fi
done
echo ""

# -------------------------------------------------------------------
# CHECK 2: Required directories
# -------------------------------------------------------------------
echo "--- Check 2: Required directories ---"
REQUIRED_DIRS=(
  "docs"
  "docs/project"
  "docs/requirements"
  "docs/architecture"
  "docs/decisions"
  "docs/audit"
  "docs/testing"
  "docs/operations"
  "docs/security"
  "stages"
  "stages/stage-00-repository-baseline"
  "stages/templates"
  "configs"
  "configs/mikrotik"
  "configs/vps1"
  "configs/vps3"
  "configs/nftables"
  "configs/routing"
  "configs/dns"
  "configs/systemd"
  "configs/monitoring"
  "scripts"
  "scripts/bootstrap"
  "scripts/deploy"
  "scripts/validation"
  "scripts/testing"
  "scripts/rollback"
  "scripts/inventory"
  "scripts/security"
  "inventory"
  "inventory/templates"
  "inventory/mikrotik"
  "inventory/vps1"
  "inventory/vps3"
  "tests"
  "tests/static"
  "tests/functional"
  "tests/integration"
  "tests/performance"
  "tests/resilience"
  "tests/security"
  "tests/acceptance"
  "evidence"
  "evidence/stage-00"
  "reports"
  "reports/audit"
  "reports/testing"
  "reports/performance"
  "reports/security"
  "reports/acceptance"
  "diagrams"
  "diagrams/source"
  "diagrams/rendered"
  "tools"
  "tools/lint"
  "tools/validation"
  ".github"
  ".github/ISSUE_TEMPLATE"
  ".github/workflows"
)

for dir in "${REQUIRED_DIRS[@]}"; do
  if [ -d "$dir" ]; then
    pass "Required directory exists: $dir"
  else
    fail "Missing required directory: $dir"
  fi
done
echo ""

# -------------------------------------------------------------------
# CHECK 3: Stage 00 artifacts
# -------------------------------------------------------------------
echo "--- Check 3: Stage 00 artifacts ---"
STAGE00_FILES=(
  "stages/stage-00-repository-baseline/task.md"
  "stages/stage-00-repository-baseline/report.md"
  "stages/stage-00-repository-baseline/acceptance.md"
  "stages/stage-00-repository-baseline/evidence-index.md"
)

for file in "${STAGE00_FILES[@]}"; do
  if [ -f "$file" ]; then
    pass "Stage 00 artifact exists: $file"
  else
    fail "Missing Stage 00 artifact: $file"
  fi
done
echo ""

# -------------------------------------------------------------------
# CHECK 4: Prohibited files
# -------------------------------------------------------------------
echo "--- Check 4: Prohibited files ---"
PROHIBITED=$(find . -type f \
  \( -name '*.key' -o -name '*.pem' -o -name '*.p12' \
     -o -name '*.pfx' -o -name '.env' -o -name '*.backup' \
     -o -name '*.backup.*' -o -name '*.rsc.private' \
     -o -name '*.secret' -o -name '*.secrets' \
     -o -name 'id_rsa' -o -name 'id_rsa.*' \
     -o -name 'id_ed25519' -o -name 'id_ed25519.*' \) \
  -not -path './.git/*' -print 2>/dev/null || true)

if [ -z "$PROHIBITED" ]; then
  pass "No prohibited files found"
else
  fail "Prohibited files found:"
  echo "$PROHIBITED" | while read -r f; do
    echo "  - $f"
    FAIL_COUNT=$((FAIL_COUNT + 1))
  done
fi
echo ""

# -------------------------------------------------------------------
# CHECK 5: Empty Markdown files
# -------------------------------------------------------------------
echo "--- Check 5: Empty Markdown files ---"
EMPTY_MD=$(find . -type f -name '*.md' -empty -not -path './.git/*' -print 2>/dev/null || true)

if [ -z "$EMPTY_MD" ]; then
  pass "No empty Markdown files found"
else
  fail "Empty Markdown files found:"
  echo "$EMPTY_MD" | while read -r f; do
    echo "  - $f"
  done
fi
echo ""

# -------------------------------------------------------------------
# CHECK 6: GitHub Actions workflows
# -------------------------------------------------------------------
echo "--- Check 6: GitHub Actions workflows ---"
REQUIRED_WORKFLOWS=(
  ".github/workflows/markdown-lint.yml"
  ".github/workflows/shellcheck.yml"
  ".github/workflows/secret-scan.yml"
  ".github/workflows/repository-validation.yml"
)

for workflow in "${REQUIRED_WORKFLOWS[@]}"; do
  if [ -f "$workflow" ]; then
    pass "Workflow exists: $workflow"
  else
    fail "Missing workflow: $workflow"
  fi
done
echo ""

# -------------------------------------------------------------------
# CHECK 7: .gitkeep in empty directories
# -------------------------------------------------------------------
echo "--- Check 7: .gitkeep presence ---"
EMPTY_DIRS_NEEDING_GITKEEP=(
  "configs/mikrotik/templates"
  "configs/mikrotik/generated"
  "configs/vps1/templates"
  "configs/vps1/generated"
  "configs/vps3/templates"
  "configs/vps3/generated"
  "configs/nftables"
  "configs/routing"
  "configs/dns"
  "configs/systemd"
  "configs/monitoring"
  "scripts/bootstrap"
  "scripts/deploy"
  "scripts/validation"
  "scripts/testing"
  "scripts/rollback"
  "scripts/inventory"
  "scripts/security"
  "inventory/templates"
  "inventory/mikrotik"
  "inventory/vps1"
  "inventory/vps3"
  "tests/static"
  "tests/functional"
  "tests/integration"
  "tests/performance"
  "tests/resilience"
  "tests/security"
  "tests/acceptance"
  "reports/audit"
  "reports/testing"
  "reports/performance"
  "reports/security"
  "reports/acceptance"
  "diagrams/source"
  "diagrams/rendered"
  "tools/lint"
)

for dir in "${EMPTY_DIRS_NEEDING_GITKEEP[@]}"; do
  if [ -f "$dir/.gitkeep" ]; then
    pass ".gitkeep present in: $dir"
  else
    fail "Missing .gitkeep in: $dir"
  fi
done
echo ""

# -------------------------------------------------------------------
# CHECK 8: Stage templates
# -------------------------------------------------------------------
echo "--- Check 8: Stage templates ---"
STAGE_TEMPLATES=(
  "stages/templates/task-template.md"
  "stages/templates/report-template.md"
  "stages/templates/acceptance-template.md"
  "stages/templates/evidence-index-template.md"
)

for template in "${STAGE_TEMPLATES[@]}"; do
  if [ -f "$template" ]; then
    pass "Stage template exists: $template"
  else
    fail "Missing stage template: $template"
  fi
done
echo ""

# -------------------------------------------------------------------
# CHECK 9: Evidence Stage 00 files (FAIL if missing, not WARN)
# -------------------------------------------------------------------
echo "--- Check 9: Evidence Stage 00 ---"
EVIDENCE_FILES=(
  "evidence/stage-00/repository-tree.txt"
  "evidence/stage-00/git-status.txt"
  "evidence/stage-00/git-log.txt"
  "evidence/stage-00/markdown-files.txt"
  "evidence/stage-00/secret-scan.txt"
  "evidence/stage-00/validation.txt"
  "evidence/stage-00/checksums.sha256"
)

for file in "${EVIDENCE_FILES[@]}"; do
  if [ -f "$file" ]; then
    pass "Evidence file exists: $file"
  else
    fail "Evidence file missing: $file"
  fi
done
echo ""

# -------------------------------------------------------------------
# CHECK 10: README content checks
# -------------------------------------------------------------------
echo "--- Check 10: README content checks ---"
if grep -q "Stage-Gate\|stage-gate" README.md 2>/dev/null; then
  pass "README mentions stage-gate process"
else
  fail "README does not mention stage-gate process"
fi

if grep -q "PASSED" README.md 2>/dev/null; then
  pass "README mentions PASSED status"
else
  fail "README does not mention PASSED status"
fi
echo ""

# -------------------------------------------------------------------
# CHECK 11: Roles and PASSED authority
# -------------------------------------------------------------------
echo "--- Check 11: Roles and PASSED authority ---"
if grep -q "Hermes + Qwen\|Hermes.*Qwen" docs/project/roles-and-responsibilities.md 2>/dev/null; then
  pass "Roles document references Hermes + Qwen"
else
  fail "Roles document does not reference Hermes + Qwen"
fi

if grep -q "PASSED\|passed" docs/project/stage-gates.md 2>/dev/null; then
  pass "Stage-gates document defines PASSED status"
else
  fail "Stage-gates document does not define PASSED status"
fi
echo ""

# -------------------------------------------------------------------
# CHECK 12: File encoding and newlines
# -------------------------------------------------------------------
echo "--- Check 12: File encoding and newlines ---"
MD_COUNT=$(find . -type f -name '*.md' -not -path './.git/*' | wc -l)
echo "Total Markdown files: $MD_COUNT"

NO_NEWLINE_COUNT=0
while IFS= read -r -d '' file; do
  if [ -s "$file" ]; then
    last_char=$(tail -c1 "$file" 2>/dev/null | od -An -tx1 | tr -d ' ' | tr -d '\n')
    if [ "$last_char" != "0a" ]; then
      NO_NEWLINE_COUNT=$((NO_NEWLINE_COUNT + 1))
    fi
  fi
done < <(find . -type f -name '*.md' -not -path './.git/*' -print0)

if [ "$NO_NEWLINE_COUNT" -eq 0 ]; then
  pass "All Markdown files end with newline"
else
  fail "$NO_NEWLINE_COUNT Markdown file(s) missing final newline"
fi
echo ""

# -------------------------------------------------------------------
# CHECK 13: task.md completeness
# -------------------------------------------------------------------
echo "--- Check 13: task.md completeness ---"
TASK_FILE="stages/stage-00-repository-baseline/task.md"
if [ -f "$TASK_FILE" ]; then
  # Check for all 15 required sections
  for section_num in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
    if grep -q "## ${section_num}\." "$TASK_FILE" 2>/dev/null; then
      pass "task.md contains section ${section_num}"
    else
      fail "task.md missing section ${section_num}"
    fi
  done

  # Check for prohibited shorthand phrases
  if grep -q "Остальные разделы задания" "$TASK_FILE" 2>/dev/null; then
    fail "task.md contains prohibited shorthand: 'Остальные разделы задания'"
  else
    pass "task.md does not contain prohibited shorthand phrases"
  fi

  if grep -q "Полный текст задания сохранен в исходном документе" "$TASK_FILE" 2>/dev/null; then
    fail "task.md references non-existent external document"
  else
    pass "task.md does not reference non-existent external document"
  fi
else
  fail "task.md does not exist"
fi
echo ""

# -------------------------------------------------------------------
# CHECK 14: Evidence checksums verification
# -------------------------------------------------------------------
echo "--- Check 14: Evidence checksums ---"
CHECKSUM_FILE="evidence/stage-00/checksums.sha256"
if [ -f "$CHECKSUM_FILE" ]; then
  pass "checksums.sha256 exists"
  if sha256sum --check "$CHECKSUM_FILE" >/dev/null 2>&1; then
    pass "checksums.sha256 verification passed"
  else
    fail "checksums.sha256 verification FAILED"
    sha256sum --check "$CHECKSUM_FILE" 2>&1 | grep -i "FAILED" || true
  fi
else
  fail "checksums.sha256 does not exist"
fi
echo ""

# -------------------------------------------------------------------
# CHECK 15: Report SHA consistency
# -------------------------------------------------------------------
echo "--- Check 15: Report SHA consistency ---"
REPORT_FILE="stages/stage-00-repository-baseline/report.md"
if [ -f "$REPORT_FILE" ]; then
  # Check for truncated/short SHAs (less than 40 hex chars that look like commit references)
  # Only flag SHAs that are 7-39 hex chars (7 is git's default abbreviated form)
  SHORT_SHA_LINES=$(grep -nE "(SHA|Commit)[^0-9a-f]*[0-9a-f]{7,39}[^0-9a-f]" "$REPORT_FILE" 2>/dev/null | grep -vE "[0-9a-f]{40}" || true)
  if [ -n "$SHORT_SHA_LINES" ]; then
    warn "Report may contain shortened SHA values (verify manually)"
    echo "$SHORT_SHA_LINES" | head -5
  else
    pass "No shortened SHA patterns detected in report"
  fi

  # Check that report does not contain "to be obtained after push"
  if grep -q "to be obtained after push" "$REPORT_FILE" 2>/dev/null; then
    fail "Report contains stale placeholder: 'to be obtained after push'"
  else
    pass "Report does not contain stale push placeholder"
  fi
else
  fail "Report file does not exist"
fi
echo ""

# -------------------------------------------------------------------
# CHECK 16: Acceptance metadata
# -------------------------------------------------------------------
echo "--- Check 16: Acceptance metadata ---"
ACCEPTANCE_FILE="stages/stage-00-repository-baseline/acceptance.md"
if [ -f "$ACCEPTANCE_FILE" ]; then
  if grep -q "PENDING EXTERNAL AUDIT\|PENDING" "$ACCEPTANCE_FILE" 2>/dev/null; then
    pass "Acceptance file has correct PENDING status"
  else
    warn "Acceptance file may not have PENDING status"
  fi
else
  fail "Acceptance file does not exist"
fi
echo ""

# -------------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------------
echo "========================================"
echo "VALIDATION SUMMARY"
echo "========================================"
echo "PASS: $PASS_COUNT"
echo "FAIL: $FAIL_COUNT"
echo "WARN: $WARN_COUNT"
echo "========================================"

if [ "$FAIL_COUNT" -gt 0 ]; then
  echo "RESULT: FAILED"
  exit 1
else
  echo "RESULT: PASSED"
  exit 0
fi
