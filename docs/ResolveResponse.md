# ResolveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentions** | [**List[MentionResolution]**](MentionResolution.md) |  | 
**dataset_uri** | **str** |  | 
**language** | **str** |  | 
**processing_time_ms** | **float** |  | 
**engine** | **str** |  | [optional] [default to 'content-analysis-v3']

## Example

```python
from wordlift_client.models.resolve_response import ResolveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveResponse from a JSON string
resolve_response_instance = ResolveResponse.from_json(json)
# print the JSON string representation of the object
print(ResolveResponse.to_json())

# convert the object into a dict
resolve_response_dict = resolve_response_instance.to_dict()
# create an instance of ResolveResponse from a dict
resolve_response_from_dict = ResolveResponse.from_dict(resolve_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


