import sys

# Maps security scheme names used in sub-specs to the canonical name defined in base/base.yaml.
# openapi-merge keeps only the first securitySchemes block it finds (base.yaml), so sub-spec
# scheme names survive only in operation-level security references — pointing to a now-undefined
# scheme and causing the generator to emit empty _auth_settings lists.
SECURITY_SCHEME_ALIASES = {
    "WordliftApiKey": "ApiKey",
}

merged_spec = "./wordliftApiSpec.yaml"

with open(merged_spec, "r") as f:
    content = f.read()

for alias, canonical in SECURITY_SCHEME_ALIASES.items():
    count = content.count(alias)
    if count:
        content = content.replace(alias, canonical)
        print(f"Replaced '{alias}' → '{canonical}' ({count} occurrence(s))")

with open(merged_spec, "w") as f:
    f.write(content)
