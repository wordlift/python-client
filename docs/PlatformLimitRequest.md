# PlatformLimitRequest

Platform Limit request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | **str** |  | 
**based_on** | **str** | &#x60;SKU&#x60; if omitted on create; kept if omitted on update. | [optional] 
**based_on_value** | **str** |  | 
**description** | **str** |  | [optional] 
**limits** | **int** |  | 
**scope** | **str** | &#x60;SUBSCRIPTION&#x60; if omitted on create; kept if omitted on update. | [optional] 

## Example

```python
from wordlift_client.models.platform_limit_request import PlatformLimitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformLimitRequest from a JSON string
platform_limit_request_instance = PlatformLimitRequest.from_json(json)
# print the JSON string representation of the object
print(PlatformLimitRequest.to_json())

# convert the object into a dict
platform_limit_request_dict = platform_limit_request_instance.to_dict()
# create an instance of PlatformLimitRequest from a dict
platform_limit_request_from_dict = PlatformLimitRequest.from_dict(platform_limit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


