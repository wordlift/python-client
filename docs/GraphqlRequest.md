# GraphqlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 

## Example

```python
from wordlift-client.models.graphql_request import GraphqlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GraphqlRequest from a JSON string
graphql_request_instance = GraphqlRequest.from_json(json)
# print the JSON string representation of the object
print(GraphqlRequest.to_json())

# convert the object into a dict
graphql_request_dict = graphql_request_instance.to_dict()
# create an instance of GraphqlRequest from a dict
graphql_request_from_dict = GraphqlRequest.from_dict(graphql_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


