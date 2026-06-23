# GraphKpiSnapshotRequest

Graph KPI snapshot write payload. The account id is provided in the path. For `POST`, `snapshot_date` is required in the body. For `PUT`, `snapshot_date` may be omitted; when provided it must match the path date. KPI metrics are additional top-level JSON properties whose values are non-negative numbers or nested objects of non-negative numbers. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculated_at** | **datetime** | UTC instant when the snapshot was calculated. | 
**snapshot_date** | **date** | Snapshot date. Required for POST; optional for PUT and must match the path date when present. | [optional] 
**snapshot_origin** | **str** | Origin of the snapshot, for example &#x60;calculated&#x60;. | [optional] 

## Example

```python
from wordlift_client.models.graph_kpi_snapshot_request import GraphKpiSnapshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GraphKpiSnapshotRequest from a JSON string
graph_kpi_snapshot_request_instance = GraphKpiSnapshotRequest.from_json(json)
# print the JSON string representation of the object
print(GraphKpiSnapshotRequest.to_json())

# convert the object into a dict
graph_kpi_snapshot_request_dict = graph_kpi_snapshot_request_instance.to_dict()
# create an instance of GraphKpiSnapshotRequest from a dict
graph_kpi_snapshot_request_from_dict = GraphKpiSnapshotRequest.from_dict(graph_kpi_snapshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


