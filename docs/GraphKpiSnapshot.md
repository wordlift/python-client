# GraphKpiSnapshot

Dated graph KPI snapshot for one WordLift account. KPI metrics are exposed as additional top-level JSON properties; metric values are non-negative numbers or nested objects of non-negative numbers. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | WordLift account id. | [optional] 
**calculated_at** | **datetime** | UTC instant when the snapshot was calculated. | [optional] 
**kpis** | **Dict[str, object]** |  | [optional] 
**snapshot_date** | **date** | Date the graph snapshot represents. | [optional] 
**snapshot_origin** | **str** | Origin of the snapshot, for example &#x60;calculated&#x60;. | [optional] 

## Example

```python
from wordlift_client.models.graph_kpi_snapshot import GraphKpiSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of GraphKpiSnapshot from a JSON string
graph_kpi_snapshot_instance = GraphKpiSnapshot.from_json(json)
# print the JSON string representation of the object
print(GraphKpiSnapshot.to_json())

# convert the object into a dict
graph_kpi_snapshot_dict = graph_kpi_snapshot_instance.to_dict()
# create an instance of GraphKpiSnapshot from a dict
graph_kpi_snapshot_from_dict = GraphKpiSnapshot.from_dict(graph_kpi_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


