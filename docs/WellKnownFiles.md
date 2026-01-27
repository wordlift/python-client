# WellKnownFiles

Status of .well-known directory files

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_plugin** | **bool** | Whether .well-known/ai-plugin.json exists (ChatGPT/OpenAI plugins) | [optional] 
**ucp** | **bool** | Whether .well-known/ucp.json exists (Universal Commerce Protocol) | [optional] 
**security** | **bool** | Whether .well-known/security.txt exists (security contact info) | [optional] 
**asset_links** | **bool** | Whether .well-known/assetlinks.json exists (Android deep linking) | [optional] 
**apple_association** | **bool** | Whether .well-known/apple-app-site-association exists (iOS deep linking) | [optional] 
**llms_txt** | **bool** | Whether .well-known/llms.txt exists (alternative LLM instructions location) | [optional] 

## Example

```python
from wordlift_client.models.well_known_files import WellKnownFiles

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownFiles from a JSON string
well_known_files_instance = WellKnownFiles.from_json(json)
# print the JSON string representation of the object
print(WellKnownFiles.to_json())

# convert the object into a dict
well_known_files_dict = well_known_files_instance.to_dict()
# create an instance of WellKnownFiles from a dict
well_known_files_from_dict = WellKnownFiles.from_dict(well_known_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


