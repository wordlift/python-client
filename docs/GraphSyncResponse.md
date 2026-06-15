# GraphSyncResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_name** | **str** |  | [optional] 
**project_url** | **str** |  | [optional] 
**repository_name** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.graph_sync_response import GraphSyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GraphSyncResponse from a JSON string
graph_sync_response_instance = GraphSyncResponse.from_json(json)
# print the JSON string representation of the object
print(GraphSyncResponse.to_json())

# convert the object into a dict
graph_sync_response_dict = graph_sync_response_instance.to_dict()
# create an instance of GraphSyncResponse from a dict
graph_sync_response_from_dict = GraphSyncResponse.from_dict(graph_sync_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


