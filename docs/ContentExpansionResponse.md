# ContentExpansionResponse

A Content Expansion response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion** | **str** | The completion. | [optional] 

## Example

```python
from wordlift-client.models.content_expansion_response import ContentExpansionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentExpansionResponse from a JSON string
content_expansion_response_instance = ContentExpansionResponse.from_json(json)
# print the JSON string representation of the object
print(ContentExpansionResponse.to_json())

# convert the object into a dict
content_expansion_response_dict = content_expansion_response_instance.to_dict()
# create an instance of ContentExpansionResponse from a dict
content_expansion_response_from_dict = ContentExpansionResponse.from_dict(content_expansion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


