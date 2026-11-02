"""
Normalize the merged spec so OpenAPI Generator >= 7.25 keeps the client API that
earlier releases (generated with 7.6) exposed. Runs on ./wordliftApiSpec.yaml
after the merge, like normalize_security_schemes.py.

1. Unify operation tags that differ only by case/spacing.
   The generator derives the API class from the tag, so 'Jobs' (crawler.yaml)
   and 'jobs' (graph-kpi.yaml) both map to JobsApi. 7.6 silently wrote one file
   over the other; >= 7.25 emits jobs_api.py and jobs0_api.py, two classes both
   named JobsApi, only one of them exported. Rewriting every variant to a single
   spelling puts all operations of the tag on one class. The canonical spelling
   is the one in the top-level `tags` list (first spec in merge order wins),
   falling back to the first one seen on an operation.

2. Drop `format: uuid` from string schemas.
   7.6 typed these as StrictStr; >= 7.25 types them as uuid.UUID, which changes
   response model fields from str to UUID objects (breaking equality checks and
   json.dumps of model_dump()). The generator has no option to opt out.

3. Rewrite the OAS 3.1 null-union (`oneOf|anyOf: [X, {type: 'null'}]`, which
   openapi-down-convert leaves alone) to 3.0 form in the two shapes >= 7.25
   generates differently from 7.6:
   - `oneOf` with an inline X: 7.25+ emits a oneOf wrapper model referencing an
     undefined `none_type`, so the model (and its parents) fail to validate.
   - `anyOf` with a `$ref` X in a parameter: 7.25+ types the parameter as Any.
   All other null-unions (properties, anyOf with inline X) generate the same
   types as 7.6 and are left untouched.
"""
import yaml

merged_spec = "./wordliftApiSpec.yaml"


def tag_key(tag):
    return tag.replace(" ", "").replace("_", "").replace("-", "").lower()


def normalize_tags(spec):
    operations = [
        op
        for item in (spec.get("paths") or {}).values()
        for op in item.values()
        if isinstance(op, dict) and "responses" in op
    ]
    canonical = {}
    for tag in spec.get("tags") or []:
        canonical.setdefault(tag_key(tag["name"]), tag["name"])
    for op in operations:
        for tag in op.get("tags") or []:
            canonical.setdefault(tag_key(tag), tag)

    changed = 0
    for op in operations:
        tags = op.get("tags")
        if not tags:
            continue
        new_tags = list(dict.fromkeys(canonical[tag_key(t)] for t in tags))
        if new_tags != tags:
            print(f"  {op.get('operationId')}: tags {tags} -> {new_tags}")
            op["tags"] = new_tags
            changed += 1
    return changed


def strip_uuid_format(node):
    count = 0
    if isinstance(node, dict):
        if node.get("format") == "uuid" and node.get("type", "string") == "string":
            del node["format"]
            count += 1
        for value in node.values():
            count += strip_uuid_format(value)
    elif isinstance(node, list):
        for value in node:
            count += strip_uuid_format(value)
    return count


def is_null(schema):
    return isinstance(schema, dict) and schema.get("type") == "null"


def rewrite_null_union(schema, in_parameter):
    """Return the 3.0 replacement for a targeted null-union schema, or None."""
    for keyword in ("oneOf", "anyOf"):
        branches = schema.get(keyword)
        if not isinstance(branches, list) or len(branches) != 2:
            continue
        others = [b for b in branches if not is_null(b)]
        if len(others) != 1 or not isinstance(others[0], dict):
            continue
        (other,) = others
        siblings = {k: v for k, v in schema.items() if k != keyword}
        if keyword == "oneOf" and "$ref" not in other:
            return {**other, **siblings, "nullable": True}
        if keyword == "anyOf" and "$ref" in other and in_parameter:
            return {"$ref": other["$ref"]}
    return None


def normalize_null_unions(node, in_parameter=False):
    count = 0
    if isinstance(node, dict):
        if in_parameter is False and "in" in node and "name" in node and isinstance(node.get("schema"), dict):
            replacement = rewrite_null_union(node["schema"], in_parameter=True)
            if replacement is not None:
                node["schema"] = replacement
                count += 1
        for key, value in node.items():
            if isinstance(value, dict):
                replacement = rewrite_null_union(value, in_parameter=False)
                if replacement is not None:
                    node[key] = value = replacement
                    count += 1
            count += normalize_null_unions(value, in_parameter)
    elif isinstance(node, list):
        for value in node:
            count += normalize_null_unions(value, in_parameter)
    return count


with open(merged_spec, "r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)

tags_changed = normalize_tags(spec)
uuids_stripped = strip_uuid_format(spec)
null_unions = normalize_null_unions(spec)

if tags_changed or uuids_stripped or null_unions:
    with open(merged_spec, "w", encoding="utf-8") as f:
        yaml.dump(spec, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

print(f"Normalized tags on {tags_changed} operation(s), dropped format: uuid from {uuids_stripped} schema(s), "
      f"rewrote {null_unions} null-union schema(s)")
