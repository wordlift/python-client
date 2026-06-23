# GraphKpiSnapshotPage

List response for account graph KPI snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GraphKpiSnapshot]**](GraphKpiSnapshot.md) | Graph KPI snapshots ordered by &#x60;snapshot_date&#x60; descending. | [optional] 

## Example

```python
from wordlift_client.models.graph_kpi_snapshot_page import GraphKpiSnapshotPage

# TODO update the JSON string below
json = "{}"
# create an instance of GraphKpiSnapshotPage from a JSON string
graph_kpi_snapshot_page_instance = GraphKpiSnapshotPage.from_json(json)
# print the JSON string representation of the object
print(GraphKpiSnapshotPage.to_json())

# convert the object into a dict
graph_kpi_snapshot_page_dict = graph_kpi_snapshot_page_instance.to_dict()
# create an instance of GraphKpiSnapshotPage from a dict
graph_kpi_snapshot_page_from_dict = GraphKpiSnapshotPage.from_dict(graph_kpi_snapshot_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


