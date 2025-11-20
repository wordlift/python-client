# QueryCoverageOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**is_covered** | **bool** |  | 
**similarity** | **float** |  | 

## Example

```python
from wordlift_client.models.query_coverage_output import QueryCoverageOutput

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCoverageOutput from a JSON string
query_coverage_output_instance = QueryCoverageOutput.from_json(json)
# print the JSON string representation of the object
print(QueryCoverageOutput.to_json())

# convert the object into a dict
query_coverage_output_dict = query_coverage_output_instance.to_dict()
# create an instance of QueryCoverageOutput from a dict
query_coverage_output_from_dict = QueryCoverageOutput.from_dict(query_coverage_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


