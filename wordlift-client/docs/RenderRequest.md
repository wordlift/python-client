# RenderRequest

A request to render a template using the provided data structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | The data from knowledge graph after applying the graphql query. | [readonly] 
**template** | **str** | The liquid template. | 

## Example

```python
from Wordlift_client.models.render_request import RenderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RenderRequest from a JSON string
render_request_instance = RenderRequest.from_json(json)
# print the JSON string representation of the object
print(RenderRequest.to_json())

# convert the object into a dict
render_request_dict = render_request_instance.to_dict()
# create an instance of RenderRequest from a dict
render_request_from_dict = RenderRequest.from_dict(render_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


