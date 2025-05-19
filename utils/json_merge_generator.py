import os
import json

# Directory containing the YAML files
yaml_directory = "./api"

# Output JSON file
output_json_file = "./openapi-merge.json"

# Gather all YAML files in the directory. The openapi merge operation takes the first security scheme and api server
# that if finds, so that we provide them using the base.yaml file, see https://github.com/robertmassaioli/openapi-merge/tree/main/packages/openapi-merge#merging-behaviour
# We do this because it happened that bogus yaml files broke the Python Client.
yaml_files = [os.path.join(yaml_directory, "base", "base.yaml")] + [
    os.path.join(yaml_directory, f)
    for f in os.listdir(yaml_directory)
    if f.endswith(".yaml")
]

# Construct the JSON structure
json_data = {
    "inputs": [{"inputFile": yaml_file} for yaml_file in yaml_files],
    "output": "./wordliftApiSpec.yaml",
}

# Write the JSON data to the output file
with open(output_json_file, "w") as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"JSON file has been generated and saved to {output_json_file}")
