# ResolveMentions503Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**dataset_uri** | **str** |  | [optional] 
**retry_after_s** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.resolve_mentions503_response import ResolveMentions503Response

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveMentions503Response from a JSON string
resolve_mentions503_response_instance = ResolveMentions503Response.from_json(json)
# print the JSON string representation of the object
print(ResolveMentions503Response.to_json())

# convert the object into a dict
resolve_mentions503_response_dict = resolve_mentions503_response_instance.to_dict()
# create an instance of ResolveMentions503Response from a dict
resolve_mentions503_response_from_dict = ResolveMentions503Response.from_dict(resolve_mentions503_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


