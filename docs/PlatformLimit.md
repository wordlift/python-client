# PlatformLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | **str** |  | 
**based_on** | **str** |  | 
**based_on_value** | **str** |  | 
**created_at** | **datetime** | The create date-time. | [optional] [readonly] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**limits** | **int** |  | 
**modified_at** | **datetime** | The last modified date-time. | [optional] [readonly] 
**scope** | **str** |  | 

## Example

```python
from wordlift_client.models.platform_limit import PlatformLimit

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformLimit from a JSON string
platform_limit_instance = PlatformLimit.from_json(json)
# print the JSON string representation of the object
print(PlatformLimit.to_json())

# convert the object into a dict
platform_limit_dict = platform_limit_instance.to_dict()
# create an instance of PlatformLimit from a dict
platform_limit_from_dict = PlatformLimit.from_dict(platform_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


