# GraphSyncRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_name** | **str** |  | 
**repository_name** | **str** |  | 
**sheets_name** | **str** |  | [optional] 
**sheets_service_account** | **str** |  | [optional] 
**sheets_url** | **str** |  | [optional] 
**sitemap_url** | **str** |  | [optional] 
**sitemap_url_pattern** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 
**urls** | **List[str]** |  | [optional] 

## Example

```python
from wordlift_client.models.graph_sync_request import GraphSyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GraphSyncRequest from a JSON string
graph_sync_request_instance = GraphSyncRequest.from_json(json)
# print the JSON string representation of the object
print(GraphSyncRequest.to_json())

# convert the object into a dict
graph_sync_request_dict = graph_sync_request_instance.to_dict()
# create an instance of GraphSyncRequest from a dict
graph_sync_request_from_dict = GraphSyncRequest.from_dict(graph_sync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


