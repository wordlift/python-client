import json

config_file = 'config.json'

with open(config_file, 'r') as file:
    config_data = json.load(file)

current_version = config_data.get('packageVersion')
major, minor, patch = map(int, current_version.split('.'))
minor += 1
new_version = f"{major}.{minor}.{patch}"

config_data['packageVersion'] = new_version

with open(config_file, 'w') as file:
    json.dump(config_data, file, indent=2)

print(f"Updated packageVersion to {new_version} in {config_file}")