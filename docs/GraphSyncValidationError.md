# GraphSyncValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[LocationInner]**](LocationInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 
**input** | **object** |  | [optional] 
**ctx** | **object** |  | [optional] 

## Example

```python
from wordlift_client.models.graph_sync_validation_error import GraphSyncValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of GraphSyncValidationError from a JSON string
graph_sync_validation_error_instance = GraphSyncValidationError.from_json(json)
# print the JSON string representation of the object
print(GraphSyncValidationError.to_json())

# convert the object into a dict
graph_sync_validation_error_dict = graph_sync_validation_error_instance.to_dict()
# create an instance of GraphSyncValidationError from a dict
graph_sync_validation_error_from_dict = GraphSyncValidationError.from_dict(graph_sync_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


