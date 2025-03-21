# Filter

A query request filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[Filter]**](Filter.md) | Operational filters such as AND or OR. | [optional] 
**key** | **str** | The filter key. Key is required for the filters [EQ, NE, GT, LT, GTE, LTE, IN, NIN] | [optional] 
**operator** | **str** | A query request filter operator. | 
**value** | [**FilterValue**](FilterValue.md) |  | [optional] 
**value_date** | **datetime** | The filter value as a date, if provided will be preferred over the &#x60;value&#x60; field. | [optional] 

## Example

```python
from wordlift_client.models.filter import Filter

# TODO update the JSON string below
json = "{}"
# create an instance of Filter from a JSON string
filter_instance = Filter.from_json(json)
# print the JSON string representation of the object
print(Filter.to_json())

# convert the object into a dict
filter_dict = filter_instance.to_dict()
# create an instance of Filter from a dict
filter_from_dict = Filter.from_dict(filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


