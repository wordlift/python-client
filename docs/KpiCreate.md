# KpiCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totals** | [**KpiTotals**](KpiTotals.md) |  | [optional] 
**entities_by_type** | **Dict[str, int]** |  | [optional] 
**properties_by_predicate** | **Dict[str, int]** |  | [optional] 
**validation** | **Dict[str, object]** |  | [optional] 

## Example

```python
from wordlift_client.models.kpi_create import KpiCreate

# TODO update the JSON string below
json = "{}"
# create an instance of KpiCreate from a JSON string
kpi_create_instance = KpiCreate.from_json(json)
# print the JSON string representation of the object
print(KpiCreate.to_json())

# convert the object into a dict
kpi_create_dict = kpi_create_instance.to_dict()
# create an instance of KpiCreate from a dict
kpi_create_from_dict = KpiCreate.from_dict(kpi_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


