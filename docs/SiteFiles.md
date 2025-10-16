# SiteFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Overall status of site files | [optional] 
**explanation** | **str** | Detailed explanation of site files evaluation | [optional] 
**robots_txt** | **str** | Status of robots.txt file | [optional] 
**llms_txt** | **str** | Status of llms.txt file (AI model instructions) | [optional] 
**bot_access** | [**SiteFilesBotAccess**](SiteFilesBotAccess.md) |  | [optional] 

## Example

```python
from wordlift_client.models.site_files import SiteFiles

# TODO update the JSON string below
json = "{}"
# create an instance of SiteFiles from a JSON string
site_files_instance = SiteFiles.from_json(json)
# print the JSON string representation of the object
print(SiteFiles.to_json())

# convert the object into a dict
site_files_dict = site_files_instance.to_dict()
# create an instance of SiteFiles from a dict
site_files_from_dict = SiteFiles.from_dict(site_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


