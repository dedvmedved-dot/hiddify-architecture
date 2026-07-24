#!/usr/bin/env bash
# expect_exit_code.sh — strict negative gate validation
# Usage: expect_exit_code.sh <expected_code> <command...>
#
# Runs the command, captures its exit code, and PASSes only if it matches expectation.
# Exits 0 on match, exits 1 on mismatch.

set -Eeuo pipefail

if [ $# -lt 2 ]; then
    echo "USAGE: expect_exit_code.sh <expected_code> <command...>"
    echo "ERROR: at least 2 arguments required"
    exit 1
fi

EXPECTED="$1"
shift

# Validate expected code is a number
if ! [[ "$EXPECTED" =~ ^[0-9]+$ ]]; then
    echo "ERROR: expected exit code must be a non-negative integer, got: $EXPECTED"
    exit 1
fi

COMMAND="$*"

echo "================================================"
echo "NEGATIVE GATE: expect_exit_code.sh"
echo "================================================"
echo "COMMAND: $COMMAND"
echo "EXPECTED EXIT CODE: $EXPECTED"

# Run the command in a subshell to capture exit code safely
# (prevents 'exit N' from killing the main script)
set +e
( eval "$COMMAND" )
ACTUAL=$?
set -e

echo "ACTUAL EXIT CODE: $ACTUAL"

if [ "$ACTUAL" -eq "$EXPECTED" ]; then
    echo "NEGATIVE TEST: PASS"
    echo ""
    exit 0
else
    echo "NEGATIVE TEST: FAIL"
    echo "Expected exit code $EXPECTED but got $ACTUAL"
    echo ""
    exit 1
fi
