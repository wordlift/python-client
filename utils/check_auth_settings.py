"""
Validates that every operation in every generated API file has a non-empty
_auth_settings list. Exits non-zero if any are empty, so CI fails fast
before committing a broken client.

Mirrors the pre-v1.175.0 baseline: all operations should carry 'ApiKey'.
"""
import os
import re
import sys

api_dir = './wordlift_client/api'

# Matches the opening of an _auth_settings block followed immediately by ]
# (with only whitespace between), meaning it is empty.
EMPTY_PATTERN = re.compile(r'_auth_settings: List\[str\] = \[\s*\]')
TOTAL_PATTERN = re.compile(r'_auth_settings: List\[str\] = \[')

broken = []
total_ops = 0
total_files = 0

for fname in sorted(os.listdir(api_dir)):
    if not fname.endswith('.py') or fname == '__init__.py':
        continue

    total_files += 1
    content = open(os.path.join(api_dir, fname)).read()

    ops = len(TOTAL_PATTERN.findall(content))
    empty = len(EMPTY_PATTERN.findall(content))
    total_ops += ops

    if empty:
        broken.append((fname, empty, ops))

if broken:
    print(f'FAIL — {sum(e for _, e, _ in broken)} operation(s) with empty _auth_settings '
          f'across {len(broken)} file(s):\n')
    for fname, empty, ops in broken:
        print(f'  {fname}: {empty}/{ops} broken')
    sys.exit(1)

print(f'OK — {total_ops} operation(s) across {total_files} file(s) all have auth settings')
