# KpiTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entities** | **int** | Total entities synced in this run. | 
**type_assertions_total** | **int** | Total type (rdf:type) assertions. | 
**property_assertions_total** | **int** | Total property assertions. | 

## Example

```python
from wordlift_client.models.kpi_totals import KpiTotals

# TODO update the JSON string below
json = "{}"
# create an instance of KpiTotals from a JSON string
kpi_totals_instance = KpiTotals.from_json(json)
# print the JSON string representation of the object
print(KpiTotals.to_json())

# convert the object into a dict
kpi_totals_dict = kpi_totals_instance.to_dict()
# create an instance of KpiTotals from a dict
kpi_totals_from_dict = KpiTotals.from_dict(kpi_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


