# SnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_id** | **str** | Public WordLift graph identifier. | 
**snapshot_date** | **str** | Logical KPI day for this snapshot in &#x60;YYYY-MM-DD&#x60; format. | 
**calculated_at** | **str** | Timestamp when the graph-wide KPI calculation finished. | [optional] 
**dataset_id** | **str** | Dataset identity used to compute this snapshot. Clone reuse is allowed only when the current dataset identity matches this value. | [optional] 
**snapshot_origin** | **str** | How this snapshot was produced: &#x60;calculated&#x60; for a full worker run or &#x60;cloned&#x60; when the previous validated snapshot was reused because the graph source watermark and worker policy inputs had not changed. | [optional] 
**cloned_from_snapshot_date** | **str** | When &#x60;snapshot_origin&#x3D;cloned&#x60;, the source snapshot day copied into this row. | [optional] 
**source_watermark** | **str** | Latest source-graph &#x60;_modified_&#x60; watermark observed for the dataset when this snapshot was produced. | [optional] 
**kpi_worker_version** | **str** | Worker package version used for clone eligibility and snapshot provenance. | [optional] 
**validation_rules_fingerprint** | **str** | Stable fingerprint of the validation selector and options that affect SHACL/rich-snippet outcomes. | [optional] 
**validated_at** | **str** | Timestamp when SHACL/rich-snippet validation finished. | [optional] 
**all_total_entities** | **int** | All entities in the graph snapshot. | [optional] 
**public_total_entities** | **int** | Entities that have at least one public assertion. | [optional] 
**private_total_entities** | **int** | Entities that have no public assertions. | [optional] 
**all_total_properties** | **int** | All non-&#x60;rdf:type&#x60; assertions in the snapshot. | [optional] 
**public_total_properties** | **int** | Non-&#x60;rdf:type&#x60; assertions whose predicate is public. | [optional] 
**private_total_properties** | **int** | Non-&#x60;rdf:type&#x60; assertions whose predicate is private. | [optional] 
**all_total_triples** | **int** | All assertions in the snapshot, including &#x60;rdf:type&#x60;. | [optional] 
**public_total_triples** | **int** | Assertions whose predicate is public. | [optional] 
**private_total_triples** | **int** | Assertions whose predicate is private. | [optional] 
**all_internal_edges_count** | **int** | Internal links across all assertions, excluding literals and &#x60;rdf:type&#x60;. | [optional] 
**public_internal_edges_count** | **int** | Internal links created by public assertions. | [optional] 
**private_internal_edges_count** | **int** | Internal links created by private assertions. | [optional] 
**all_external_edges_count** | **int** | External links across all assertions, excluding literals and &#x60;rdf:type&#x60;. | [optional] 
**public_external_edges_count** | **int** | External links created by public assertions. | [optional] 
**private_external_edges_count** | **int** | External links created by private assertions. | [optional] 
**all_edges_count** | **int** | All internal and external links, excluding literals and &#x60;rdf:type&#x60;. | [optional] 
**public_edges_count** | **int** | Edges created by public assertions only. | [optional] 
**private_edges_count** | **int** | Edges created by private assertions only. | [optional] 
**all_edge_node_ratio** | **float** | All edges divided by all entities. | [optional] 
**public_edge_node_ratio** | **float** | Public edges divided by public entities. | [optional] 
**private_edge_node_ratio** | **float** | Private edges divided by private entities. | [optional] 
**all_edge_node_ratio_edges** | **int** | Numerator used for &#x60;all_edge_node_ratio&#x60;. | [optional] 
**public_edge_node_ratio_edges** | **int** | Numerator used for &#x60;public_edge_node_ratio&#x60;. | [optional] 
**private_edge_node_ratio_edges** | **int** | Numerator used for &#x60;private_edge_node_ratio&#x60;. | [optional] 
**all_edge_node_ratio_nodes** | **int** | Denominator used for &#x60;all_edge_node_ratio&#x60;. | [optional] 
**public_edge_node_ratio_nodes** | **int** | Denominator used for &#x60;public_edge_node_ratio&#x60;. | [optional] 
**private_edge_node_ratio_nodes** | **int** | Denominator used for &#x60;private_edge_node_ratio&#x60;. | [optional] 
**all_unique_urls_count** | **int** | Distinct &#x60;schema:url&#x60; values in the snapshot. | [optional] 
**public_unique_urls_count** | **int** | Same as &#x60;all_unique_urls_count&#x60; because &#x60;schema:url&#x60; is public. | [optional] 
**private_unique_urls_count** | **int** | Always &#x60;0&#x60; because &#x60;schema:url&#x60; is not private. | [optional] 
**all_orphans_count** | **int** | Public orphans plus private orphans. | [optional] 
**public_orphans_count** | **int** | Public entities that are never targets of public internal edges. | [optional] 
**private_orphans_count** | **int** | Private entities that are never targets of any internal edges. | [optional] 
**all_broken_links_count** | **int** | Public broken links plus private broken links. | [optional] 
**public_broken_links_count** | **int** | Missing targets referenced by public internal edges. | [optional] 
**private_broken_links_count** | **int** | Missing targets referenced by private internal edges. | [optional] 
**all_isolated_graphs_count** | **int** | Public isolated graphs plus private isolated graphs. | [optional] 
**public_isolated_graphs_count** | **int** | Connected components built from public entities and public internal edges. | [optional] 
**private_isolated_graphs_count** | **int** | Connected components for private entities using public internal edges that connect private entities. | [optional] 
**all_duplicates_count** | **int** | Duplicate groups sharing the same &#x60;schema:url&#x60;. | [optional] 
**public_duplicates_count** | **int** | Same as &#x60;all_duplicates_count&#x60; because &#x60;schema:url&#x60; is public. | [optional] 
**private_duplicates_count** | **int** | Always &#x60;0&#x60; because &#x60;schema:url&#x60; is not private. | [optional] 
**all_entity_types** | **Dict[str, int]** | Counts of all &#x60;rdf:type&#x60; assertions grouped by type IRI. | [optional] 
**public_entity_types** | **Dict[str, int]** | Counts of &#x60;rdf:type&#x60; assertions whose type IRI is not in a private namespace. | [optional] 
**private_entity_types** | **Dict[str, int]** | Counts of &#x60;rdf:type&#x60; assertions whose type IRI is in a private namespace. | [optional] 
**all_properties_by_predicate** | **Dict[str, int]** | Counts of non-&#x60;rdf:type&#x60; assertions grouped by predicate. | [optional] 
**public_properties_by_predicate** | **Dict[str, int]** | Counts of non-&#x60;rdf:type&#x60; assertions grouped by public predicate. | [optional] 
**private_properties_by_predicate** | **Dict[str, int]** | Counts of non-&#x60;rdf:type&#x60; assertions grouped by private predicate. | [optional] 
**rich_snippets_valid_count** | **int** | Public rich-snippet items that passed validation. | [optional] 
**rich_snippets_invalid_count** | **int** | Public rich-snippet items that failed validation. | [optional] 
**rich_snippets_by_type** | **Dict[str, Dict[str, int]]** | Public rich-snippet counts grouped by type and eligibility bucket. | [optional] 
**schema_compliance_errors** | **int** | Schema-compliance errors found in public URL-generated subgraphs. | [optional] 
**schema_compliance_warnings** | **int** | Schema-compliance warnings found in public URL-generated subgraphs. | [optional] 
**schema_compliance_urls_checked** | **int** | Number of public URLs validated for schema compliance. | [optional] 
**graph_health_score** | **int** | Composite graph health score from &#x60;0&#x60; to &#x60;100&#x60; based on validation, structure, public footprint, and freshness. | [optional] 
**graph_health_validation_health** | **int** | Validation-health subscore used in &#x60;graph_health_score&#x60;. | [optional] 
**graph_health_structural_integrity** | **int** | Structural-integrity subscore used in &#x60;graph_health_score&#x60;. | [optional] 
**graph_health_public_footprint_quality** | **int** | Public-footprint-quality subscore used in &#x60;graph_health_score&#x60;. | [optional] 
**graph_health_freshness_momentum** | **int** | Freshness-and-momentum subscore used in &#x60;graph_health_score&#x60;. | [optional] 

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


