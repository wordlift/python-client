"""
Before the openapi-merge step, rename schemas that would collide across specs.

openapi-merge renames duplicate schema names with numeric suffixes (HTTPValidationError1,
HTTPValidationError2, …). This script prefixes conflicting copies with their spec's
CamelCase filename instead, producing names like CrawlerHTTPValidationError.

The first spec in merge order (alphabetically, with base.yaml first) keeps the
canonical name; all later specs that define the same name get the prefix.

Runs on ./api/ in-place — in CI this is a fresh checkout, locally run via
run_pipeline_local.sh which operates on a temp copy.
"""
import os
import re
import sys
import yaml

api_dir = './api'

# Merge order mirrors json_merge_generator.py: base first, then sorted api/*.yaml
yaml_files = ['base/base.yaml'] + sorted(
    f for f in os.listdir(api_dir) if f.endswith('.yaml')
)


def spec_prefix(fname):
    """'graph-kpi.yaml' → 'GraphKpi',  'ai_visibility_audits.yaml' → 'AiVisibilityAudits'"""
    base = os.path.splitext(os.path.basename(fname))[0]
    return ''.join(w.capitalize() for w in re.split(r'[-_]', base))


def rename_refs(obj, renames):
    """Recursively update $ref strings for renamed schemas."""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k == '$ref' and isinstance(v, str):
                for old, new in renames.items():
                    v = v.replace(f'#/components/schemas/{old}',
                                  f'#/components/schemas/{new}')
                out[k] = v
            else:
                out[k] = rename_refs(v, renames)
        return out
    if isinstance(obj, list):
        return [rename_refs(item, renames) for item in obj]
    return obj


# ── Pass 1: find the canonical owner of every schema name ────────────────────
schema_owners = {}
for fname in yaml_files:
    fpath = os.path.join(api_dir, fname)
    try:
        spec = yaml.safe_load(open(fpath))
    except FileNotFoundError:
        continue
    if not isinstance(spec, dict):
        continue
    for name in ((spec.get('components') or {}).get('schemas') or {}):
        schema_owners.setdefault(name, fname)

# ── Pass 2: rename conflicting schemas in each non-base spec ─────────────────
total = 0
for fname in sorted(f for f in os.listdir(api_dir) if f.endswith('.yaml')):
    fpath = os.path.join(api_dir, fname)
    spec = yaml.safe_load(open(fpath))
    if not isinstance(spec, dict):
        continue

    schemas = (spec.get('components') or {}).get('schemas') or {}
    prefix = spec_prefix(fname)

    renames = {
        name: f'{prefix}{name}'
        for name in schemas
        if schema_owners.get(name) != fname
    }
    if not renames:
        continue

    # Rename schema definitions
    old_schemas = spec['components']['schemas']
    spec['components']['schemas'] = {
        renames.get(k, k): v for k, v in old_schemas.items()
    }

    # Update all $refs in the spec
    spec = rename_refs(spec, renames)

    with open(fpath, 'w') as f:
        yaml.dump(spec, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    total += len(renames)
    for old, new in renames.items():
        print(f'  {fname}: {old} → {new}')

print(f'\nTotal schemas renamed: {total}')
