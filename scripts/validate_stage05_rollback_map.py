#!/usr/bin/env python3
"""Stage 05 Rollback Map Validator — S05-RB-001"""
import sys, os, yaml, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    rbf = os.path.join(ROOT, 'iac/tests/fixtures/stage05-rollback-map.yml')
    if not os.path.exists(rbf):
        print("FAIL: rollback map not found")
        sys.exit(1)

    with open(rbf) as f:
        data = yaml.safe_load(f)

    steps = data.get('rollback_map', {}).get('steps', [])
    results = []

    results.append(check(f"Steps={len(steps)}", len(steps) >= 3))

    step_ids = [s.get('step_id','') for s in steps]
    dups = [x for x in step_ids if step_ids.count(x) > 1]
    results.append(check(f"No duplicate step IDs", len(dups) == 0))

    required = ['step_id','component','checkpoint','rollback_trigger',
                'rollback_task_reference','post_rollback_validation',
                'stop_condition']

    for s in steps:
        sid = s.get('step_id','?')
        for field in required:
            val = s.get(field,'')
            results.append(check(f"{sid}.{field}", bool(val)))

    report = {
        "steps_total": len(steps),
        "duplicates": len(set(dups)),
        "result": "PASS" if all(results) else "FAIL"
    }
    print(json.dumps(report, indent=2))
    sys.exit(0 if all(results) else 1)

def check(label, ok):
    print(f"  {'PASS' if ok else 'FAIL'}: {label}")
    return ok

if __name__ == '__main__':
    main()
