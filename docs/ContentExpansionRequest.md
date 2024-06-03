# ContentExpansionRequest

The Content Expansion request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The target URL. | 
**entities** | **List[str]** | A list of entity labels. | 
**openai_key** | **str** | The OpenAI key. | 

## Example

```python
from wordlift_client.models.content_expansion_request import ContentExpansionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentExpansionRequest from a JSON string
content_expansion_request_instance = ContentExpansionRequest.from_json(json)
# print the JSON string representation of the object
print(ContentExpansionRequest.to_json())

# convert the object into a dict
content_expansion_request_dict = content_expansion_request_instance.to_dict()
# create an instance of ContentExpansionRequest from a dict
content_expansion_request_from_dict = ContentExpansionRequest.from_dict(content_expansion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


