# IncludeExclude


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [readonly] 
**flag** | **str** | A flag which determines whether the URL is &#x60;INCLUDE&#x60; or &#x60;EXCLUDE&#x60;. | 
**id** | **int** |  | [optional] [readonly] 
**url** | **str** |  | 

## Example

```python
from wordlift-client.models.include_exclude import IncludeExclude

# TODO update the JSON string below
json = "{}"
# create an instance of IncludeExclude from a JSON string
include_exclude_instance = IncludeExclude.from_json(json)
# print the JSON string representation of the object
print(IncludeExclude.to_json())

# convert the object into a dict
include_exclude_dict = include_exclude_instance.to_dict()
# create an instance of IncludeExclude from a dict
include_exclude_from_dict = IncludeExclude.from_dict(include_exclude_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


