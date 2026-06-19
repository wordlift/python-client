# GraphKpiHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[GraphKpiValidationError]**](GraphKpiValidationError.md) |  | [optional] 

## Example

```python
from wordlift_client.models.graph_kpi_http_validation_error import GraphKpiHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of GraphKpiHTTPValidationError from a JSON string
graph_kpi_http_validation_error_instance = GraphKpiHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(GraphKpiHTTPValidationError.to_json())

# convert the object into a dict
graph_kpi_http_validation_error_dict = graph_kpi_http_validation_error_instance.to_dict()
# create an instance of GraphKpiHTTPValidationError from a dict
graph_kpi_http_validation_error_from_dict = GraphKpiHTTPValidationError.from_dict(graph_kpi_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


