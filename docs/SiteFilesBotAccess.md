# SiteFilesBotAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gptbot** | **str** |  | [optional] 
**claude** | **str** |  | [optional] 
**googlebot** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.site_files_bot_access import SiteFilesBotAccess

# TODO update the JSON string below
json = "{}"
# create an instance of SiteFilesBotAccess from a JSON string
site_files_bot_access_instance = SiteFilesBotAccess.from_json(json)
# print the JSON string representation of the object
print(SiteFilesBotAccess.to_json())

# convert the object into a dict
site_files_bot_access_dict = site_files_bot_access_instance.to_dict()
# create an instance of SiteFilesBotAccess from a dict
site_files_bot_access_from_dict = SiteFilesBotAccess.from_dict(site_files_bot_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


