# KpiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | 
**totals** | [**KpiTotals**](KpiTotals.md) |  | 
**entities_by_type** | **Dict[str, int]** |  | 
**properties_by_predicate** | **Dict[str, int]** |  | 
**validation** | **Dict[str, object]** |  | 

## Example

```python
from wordlift_client.models.kpi_response import KpiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KpiResponse from a JSON string
kpi_response_instance = KpiResponse.from_json(json)
# print the JSON string representation of the object
print(KpiResponse.to_json())

# convert the object into a dict
kpi_response_dict = kpi_response_instance.to_dict()
# create an instance of KpiResponse from a dict
kpi_response_from_dict = KpiResponse.from_dict(kpi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


