# SnapshotListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SnapshotResponse]**](SnapshotResponse.md) |  | 
**page** | [**CursorPage**](CursorPage.md) |  | 

## Example

```python
from wordlift_client.models.snapshot_list_response import SnapshotListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotListResponse from a JSON string
snapshot_list_response_instance = SnapshotListResponse.from_json(json)
# print the JSON string representation of the object
print(SnapshotListResponse.to_json())

# convert the object into a dict
snapshot_list_response_dict = snapshot_list_response_instance.to_dict()
# create an instance of SnapshotListResponse from a dict
snapshot_list_response_from_dict = SnapshotListResponse.from_dict(snapshot_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


