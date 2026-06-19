"""
For every spec in ./api/ that declares a top-level `security:` block,
promote that requirement to each operation that lacks an explicit one,
then drop the global block.

After this runs, the openapi-merge step has nothing to race over:
every operation carries its own security declaration, so the ordering
of specs in the merge is irrelevant to auth correctness.
"""
import os
import sys
import yaml

HTTP_METHODS = {'get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace'}
api_dir = './api'

promoted_total = 0

for fname in sorted(os.listdir(api_dir)):
    if not fname.endswith('.yaml'):
        continue

    fpath = os.path.join(api_dir, fname)
    with open(fpath) as f:
        spec = yaml.safe_load(f)

    if not isinstance(spec, dict):
        continue

    global_security = spec.get('security')
    if not global_security:
        continue

    paths = spec.get('paths', {}) or {}
    promoted = 0

    for path_item in paths.values():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method.lower() not in HTTP_METHODS:
                continue
            if not isinstance(operation, dict):
                continue
            if 'security' not in operation:
                operation['security'] = global_security
                promoted += 1

    del spec['security']

    with open(fpath, 'w') as f:
        yaml.dump(spec, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    promoted_total += promoted
    print(f'{fname}: injected global security into {promoted} operation(s), dropped global block')

print(f'\nTotal operations promoted: {promoted_total}')
