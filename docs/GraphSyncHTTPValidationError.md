# GraphSyncHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[GraphSyncValidationError]**](GraphSyncValidationError.md) |  | [optional] 

## Example

```python
from wordlift_client.models.graph_sync_http_validation_error import GraphSyncHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of GraphSyncHTTPValidationError from a JSON string
graph_sync_http_validation_error_instance = GraphSyncHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(GraphSyncHTTPValidationError.to_json())

# convert the object into a dict
graph_sync_http_validation_error_dict = graph_sync_http_validation_error_instance.to_dict()
# create an instance of GraphSyncHTTPValidationError from a dict
graph_sync_http_validation_error_from_dict = GraphSyncHTTPValidationError.from_dict(graph_sync_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


