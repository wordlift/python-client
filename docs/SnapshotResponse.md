# SnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_id** | **str** | Public WordLift graph identifier. | 
**snapshot_date** | **str** | Logical KPI day for this snapshot in &#x60;YYYY-MM-DD&#x60; format. | 
**calculated_at** | **str** |  | [optional] 
**dataset_id** | **str** |  | [optional] 
**snapshot_origin** | **str** |  | [optional] 
**cloned_from_snapshot_date** | **str** |  | [optional] 
**source_watermark** | **str** |  | [optional] 
**kpi_worker_version** | **str** |  | [optional] 
**validation_rules_fingerprint** | **str** |  | [optional] 
**validated_at** | **str** |  | [optional] 
**all_total_entities** | **int** |  | [optional] 
**public_total_entities** | **int** |  | [optional] 
**private_total_entities** | **int** |  | [optional] 
**all_total_properties** | **int** |  | [optional] 
**public_total_properties** | **int** |  | [optional] 
**private_total_properties** | **int** |  | [optional] 
**all_total_triples** | **int** |  | [optional] 
**public_total_triples** | **int** |  | [optional] 
**private_total_triples** | **int** |  | [optional] 
**all_internal_edges_count** | **int** |  | [optional] 
**public_internal_edges_count** | **int** |  | [optional] 
**private_internal_edges_count** | **int** |  | [optional] 
**all_external_edges_count** | **int** |  | [optional] 
**public_external_edges_count** | **int** |  | [optional] 
**private_external_edges_count** | **int** |  | [optional] 
**all_edges_count** | **int** |  | [optional] 
**public_edges_count** | **int** |  | [optional] 
**private_edges_count** | **int** |  | [optional] 
**all_edge_node_ratio** | **float** |  | [optional] 
**public_edge_node_ratio** | **float** |  | [optional] 
**private_edge_node_ratio** | **float** |  | [optional] 
**all_edge_node_ratio_edges** | **int** |  | [optional] 
**public_edge_node_ratio_edges** | **int** |  | [optional] 
**private_edge_node_ratio_edges** | **int** |  | [optional] 
**all_edge_node_ratio_nodes** | **int** |  | [optional] 
**public_edge_node_ratio_nodes** | **int** |  | [optional] 
**private_edge_node_ratio_nodes** | **int** |  | [optional] 
**all_unique_urls_count** | **int** |  | [optional] 
**public_unique_urls_count** | **int** |  | [optional] 
**private_unique_urls_count** | **int** |  | [optional] 
**all_orphans_count** | **int** |  | [optional] 
**public_orphans_count** | **int** |  | [optional] 
**private_orphans_count** | **int** |  | [optional] 
**all_broken_links_count** | **int** |  | [optional] 
**public_broken_links_count** | **int** |  | [optional] 
**private_broken_links_count** | **int** |  | [optional] 
**all_isolated_graphs_count** | **int** |  | [optional] 
**public_isolated_graphs_count** | **int** |  | [optional] 
**private_isolated_graphs_count** | **int** |  | [optional] 
**all_duplicates_count** | **int** |  | [optional] 
**public_duplicates_count** | **int** |  | [optional] 
**private_duplicates_count** | **int** |  | [optional] 
**all_entity_types** | **Dict[str, int]** |  | [optional] 
**public_entity_types** | **Dict[str, int]** |  | [optional] 
**private_entity_types** | **Dict[str, int]** |  | [optional] 
**all_properties_by_predicate** | **Dict[str, int]** |  | [optional] 
**public_properties_by_predicate** | **Dict[str, int]** |  | [optional] 
**private_properties_by_predicate** | **Dict[str, int]** |  | [optional] 
**rich_snippets_valid_count** | **int** |  | [optional] 
**rich_snippets_invalid_count** | **int** |  | [optional] 
**rich_snippets_by_type** | **Dict[str, Dict[str, int]]** |  | [optional] 
**schema_compliance_errors** | **int** |  | [optional] 
**schema_compliance_warnings** | **int** |  | [optional] 
**schema_compliance_urls_checked** | **int** |  | [optional] 
**graph_health_score** | **int** |  | [optional] 
**graph_health_validation_health** | **int** |  | [optional] 
**graph_health_structural_integrity** | **int** |  | [optional] 
**graph_health_public_footprint_quality** | **int** |  | [optional] 
**graph_health_freshness_momentum** | **int** |  | [optional] 

## Example

```python
from wordlift_client.models.snapshot_response import SnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotResponse from a JSON string
snapshot_response_instance = SnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(SnapshotResponse.to_json())

# convert the object into a dict
snapshot_response_dict = snapshot_response_instance.to_dict()
# create an instance of SnapshotResponse from a dict
snapshot_response_from_dict = SnapshotResponse.from_dict(snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


