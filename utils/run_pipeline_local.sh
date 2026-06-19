#!/usr/bin/env bash
# Runs the full generation pipeline locally without modifying tracked files.
# Promotes security on a temp copy of api/, generates into a temp output
# directory, then validates and compares against a baseline git ref.
#
# Usage:
#   bash utils/run_pipeline_local.sh [baseline-ref]
#
# Examples:
#   bash utils/run_pipeline_local.sh              # compares against v1.174.0
#   bash utils/run_pipeline_local.sh 30b3af45

set -euo pipefail

REPO="$PWD"
BASELINE=${1:-30b3af45}
WORK_DIR=$(mktemp -d)
trap 'rm -rf "$WORK_DIR"' EXIT

echo "==> work dir: $WORK_DIR"
echo "==> baseline: $BASELINE"
echo

# ── 1. Copy api/ specs to a temp location so originals stay clean ────────────
cp -r api "$WORK_DIR/api"

# ── 2. Promote global security to operation level (on the copy) ──────────────
echo "==> promote_security"
(cd "$WORK_DIR" && python3 "$REPO/utils/promote_security.py")
echo

# ── 3. Generate merge config pointing at the temp api/ copy ─────────────────
#    Paths must be RELATIVE to the config file location (openapi-merge-cli
#    uses path.join, not path.resolve, so absolute paths get doubled).
echo "==> json_merge_generator"
python3 - << PYEOF
import os, json
work_dir = "$WORK_DIR"
yaml_dir = os.path.join(work_dir, "api")
base = "api/base/base.yaml"
others = sorted(
    f"api/{f}"
    for f in os.listdir(yaml_dir)
    if f.endswith(".yaml")
)
json_data = {
    "inputs": [{"inputFile": p} for p in [base] + others],
    "output": "wordliftApiSpec.yaml",
}
config_path = os.path.join(work_dir, "openapi-merge.json")
with open(config_path, "w") as f:
    json.dump(json_data, f, indent=2)
print(f"  wrote {config_path}")
PYEOF
echo

# ── 4. Merge (run from $WORK_DIR so relative paths in the config resolve) ────
echo "==> openapi-merge"
(cd "$WORK_DIR" && npx openapi-merge-cli --config ./openapi-merge.json)
echo

# ── 5. Normalize security scheme aliases ─────────────────────────────────────
echo "==> normalize_security_schemes"
python3 - << PYEOF
import re, sys
merged = "$WORK_DIR/wordliftApiSpec.yaml"
ALIASES = {"WordliftApiKey": "ApiKey"}
content = open(merged).read()
for alias, canonical in ALIASES.items():
    count = content.count(alias)
    if count:
        content = content.replace(alias, canonical)
        print(f"  replaced '{alias}' -> '{canonical}' ({count} occurrence(s))")
open(merged, "w").write(content)
PYEOF
echo

# ── 6. Generate SDK into temp output dir ─────────────────────────────────────
echo "==> openapi-generator-cli"
npx @openapitools/openapi-generator-cli generate \
    -i "$WORK_DIR/wordliftApiSpec.yaml" \
    -g python \
    -c config.json \
    --package-name wordlift_client \
    --library asyncio \
    --additional-properties=pythonVersion=3.8 \
    -o "$WORK_DIR/output" \
    2>&1 | grep -E "^\[main\]|ERROR|WARN" || true
echo

# ── 7. compare_auth_settings against baseline — fails only on regressions, not pre-existing ─
echo "==> compare vs baseline $BASELINE"
python3 - << PYEOF
import os, re, subprocess, sys

API_DIR_NEW  = "$WORK_DIR/output/wordlift_client/api"
BASELINE_REF = "$BASELINE"
AUTH_BLOCK   = re.compile(r'_auth_settings: List\[str\] = \[(.*?)\]', re.DOTALL)
SCHEME_NAME  = re.compile(r"'([^']+)'")

def parse(content):
    return [SCHEME_NAME.findall(b) for b in AUTH_BLOCK.findall(content)]

def from_git(ref):
    out = subprocess.check_output(['git','ls-tree','--name-only', ref,'wordlift_client/api/'], text=True)
    result = {}
    for path in out.strip().split('\n'):
        fname = os.path.basename(path)
        if not fname.endswith('.py') or fname == '__init__.py': continue
        try:
            c = subprocess.check_output(['git','show',f'{ref}:{path}'], text=True)
            result[fname] = parse(c)
        except: pass
    return result

def from_disk(d):
    result = {}
    for fname in sorted(os.listdir(d)):
        if not fname.endswith('.py') or fname == '__init__.py': continue
        result[fname] = parse(open(os.path.join(d, fname)).read())
    return result

baseline = from_git(BASELINE_REF)
current  = from_disk(API_DIR_NEW)

regressions = []
new_files   = []
ok = 0

for fname in sorted(set(baseline)|set(current)):
    b_ops = baseline.get(fname)
    c_ops = current.get(fname)
    if b_ops is None:
        new_files.append((fname, c_ops or []))
        continue
    if c_ops is None:
        continue
    for i,(b,c) in enumerate(zip(b_ops, c_ops)):
        if b==c: ok+=1
        elif b and not c: regressions.append((fname,i,b,c))

if regressions:
    print(f"REGRESSIONS — {len(regressions)} op(s):")
    for fname,i,b,c in regressions:
        print(f"  {fname} op[{i}]: {b} → {c}")
else:
    print(f"OK — {ok} op(s) match baseline. No regressions.")

if new_files:
    print(f"\nNEW (not in baseline):")
    for fname, ops in new_files:
        empty = sum(1 for o in ops if not o)
        print(f"  {fname}: {'all covered' if not empty else f'{empty}/{len(ops)} empty'}")

sys.exit(1 if regressions else 0)
PYEOF
