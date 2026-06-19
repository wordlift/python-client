"""
Compares _auth_settings across all generated API files between a known-good
git ref and the working tree (or a second ref).

Usage:
  python3 utils/compare_auth_settings.py <baseline-ref>
  python3 utils/compare_auth_settings.py <baseline-ref> <new-ref>

Examples:
  python3 utils/compare_auth_settings.py 30b3af45          # v1.174.0 vs working tree
  python3 utils/compare_auth_settings.py HEAD~1            # previous release vs working tree
"""
import os
import re
import subprocess
import sys

API_DIR = 'wordlift_client/api'

AUTH_BLOCK  = re.compile(r'_auth_settings: List\[str\] = \[(.*?)\]', re.DOTALL)
SCHEME_NAME = re.compile(r"'([^']+)'")


def parse_ops(content):
    return [SCHEME_NAME.findall(block) for block in AUTH_BLOCK.findall(content)]


def read_from_git(ref):
    result = {}
    try:
        paths = subprocess.check_output(
            ['git', 'ls-tree', '--name-only', ref, f'{API_DIR}/'],
            text=True, stderr=subprocess.DEVNULL
        ).strip().split('\n')
    except subprocess.CalledProcessError:
        print(f"error: could not list files at ref '{ref}'", file=sys.stderr)
        sys.exit(1)

    for path in paths:
        fname = os.path.basename(path)
        if not fname.endswith('.py') or fname == '__init__.py':
            continue
        try:
            content = subprocess.check_output(
                ['git', 'show', f'{ref}:{path}'],
                text=True, stderr=subprocess.DEVNULL
            )
            result[fname] = parse_ops(content)
        except subprocess.CalledProcessError:
            pass
    return result


def read_from_disk():
    result = {}
    if not os.path.isdir(API_DIR):
        print(f"error: {API_DIR} not found — run from repo root", file=sys.stderr)
        sys.exit(1)
    for fname in sorted(os.listdir(API_DIR)):
        if not fname.endswith('.py') or fname == '__init__.py':
            continue
        result[fname] = parse_ops(open(f'{API_DIR}/{fname}').read())
    return result


def load(ref):
    return read_from_disk() if ref == 'DISK' else read_from_git(ref)


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        sys.exit(1)

    baseline_ref = sys.argv[1]
    new_ref      = sys.argv[2] if len(sys.argv) > 2 else 'DISK'

    label_n = 'working tree' if new_ref == 'DISK' else new_ref

    print(f"baseline : {baseline_ref}")
    print(f"compare  : {label_n}")
    print()

    baseline = load(baseline_ref)
    current  = load(new_ref)

    regressions  = []
    still_broken = []
    fixed        = []
    new_files    = []
    ok_count     = 0

    for fname in sorted(set(baseline) | set(current)):
        b_ops = baseline.get(fname)
        c_ops = current.get(fname)

        if b_ops is None:
            new_files.append((fname, c_ops))
            continue

        if c_ops is None:
            continue

        for i, (b, c) in enumerate(zip(b_ops, c_ops)):
            if b == c:
                ok_count += 1
            elif b and not c:
                regressions.append((fname, i, b, c))
            elif not b and c:
                fixed.append((fname, i, b, c))
            elif not b and not c:
                still_broken.append((fname, i))
            else:
                regressions.append((fname, i, b, c))

        extra = len(c_ops) - len(b_ops)
        if extra > 0:
            for i in range(len(b_ops), len(c_ops)):
                c = c_ops[i]
                if c:
                    ok_count += 1
                else:
                    new_files.append((fname + f' op[{i}] (new)', []))

    if regressions:
        print(f"REGRESSIONS — {len(regressions)} operation(s) lost auth settings:")
        for fname, i, b, c in regressions:
            b_str = repr(b) if b else '[]'
            c_str = repr(c) if c else '[]'
            print(f"  {fname} op[{i}]: {b_str} → {c_str}")
        print()

    if still_broken:
        print(f"STILL BROKEN — {len(still_broken)} operation(s) were empty in baseline and remain empty:")
        for fname, i in still_broken:
            print(f"  {fname} op[{i}]")
        print()

    if fixed:
        print(f"FIXED — {len(fixed)} operation(s) gained auth settings (were empty in baseline):")
        for fname, i, b, c in fixed:
            print(f"  {fname} op[{i}]: [] → {repr(c)}")
        print()

    if new_files:
        print(f"NEW — {len(new_files)} file(s)/op(s) not present in baseline:")
        for fname, ops in new_files:
            empty = sum(1 for o in ops if not o)
            status = f"{empty}/{len(ops)} empty" if empty else "all covered"
            print(f"  {fname}: {status}")
        print()

    if not regressions and not still_broken:
        print(f"OK — {ok_count} operation(s) match baseline. No regressions.")

    sys.exit(1 if regressions else 0)


if __name__ == '__main__':
    main()
