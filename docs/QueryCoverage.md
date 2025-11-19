# QueryCoverage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**is_covered** | **bool** |  | 
**similarity** | **float** |  | 
**best_chunk_preview** | **str** |  | 

## Example

```python
from wordlift_client.models.query_coverage import QueryCoverage

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCoverage from a JSON string
query_coverage_instance = QueryCoverage.from_json(json)
# print the JSON string representation of the object
print(QueryCoverage.to_json())

# convert the object into a dict
query_coverage_dict = query_coverage_instance.to_dict()
# create an instance of QueryCoverage from a dict
query_coverage_from_dict = QueryCoverage.from_dict(query_coverage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


