# GraphKpiValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[LocationInner]**](LocationInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 
**input** | **object** |  | [optional] 
**ctx** | **object** |  | [optional] 

## Example

```python
from wordlift_client.models.graph_kpi_validation_error import GraphKpiValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of GraphKpiValidationError from a JSON string
graph_kpi_validation_error_instance = GraphKpiValidationError.from_json(json)
# print the JSON string representation of the object
print(GraphKpiValidationError.to_json())

# convert the object into a dict
graph_kpi_validation_error_dict = graph_kpi_validation_error_instance.to_dict()
# create an instance of GraphKpiValidationError from a dict
graph_kpi_validation_error_from_dict = GraphKpiValidationError.from_dict(graph_kpi_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


