# GraphSyncRunResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.graph_sync_run_response import GraphSyncRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GraphSyncRunResponse from a JSON string
graph_sync_run_response_instance = GraphSyncRunResponse.from_json(json)
# print the JSON string representation of the object
print(GraphSyncRunResponse.to_json())

# convert the object into a dict
graph_sync_run_response_dict = graph_sync_run_response_instance.to_dict()
# create an instance of GraphSyncRunResponse from a dict
graph_sync_run_response_from_dict = GraphSyncRunResponse.from_dict(graph_sync_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


