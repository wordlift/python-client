# IncludeExcludeRequest

A request to create an IncludeExclude.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_or_exclude** | **str** | A flag which determines whether the URL is &#x60;INCLUDE&#x60; or &#x60;EXCLUDE&#x60;. | 
**the_url** | **str** |  | 

## Example

```python
from wordlift_client.models.include_exclude_request import IncludeExcludeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IncludeExcludeRequest from a JSON string
include_exclude_request_instance = IncludeExcludeRequest.from_json(json)
# print the JSON string representation of the object
print(IncludeExcludeRequest.to_json())

# convert the object into a dict
include_exclude_request_dict = include_exclude_request_instance.to_dict()
# create an instance of IncludeExcludeRequest from a dict
include_exclude_request_from_dict = IncludeExcludeRequest.from_dict(include_exclude_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


