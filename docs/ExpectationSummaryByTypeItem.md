# ExpectationSummaryByTypeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_id** | **str** |  | 
**expectation_type** | [**ExpectationType**](ExpectationType.md) |  | 
**monitor_count** | **int** |  | 
**expectation_count** | **int** |  | 
**stats** | [**List[ExpectationSummaryTypeStat]**](ExpectationSummaryTypeStat.md) |  | 

## Example

```python
from wordlift_client.models.expectation_summary_by_type_item import ExpectationSummaryByTypeItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectationSummaryByTypeItem from a JSON string
expectation_summary_by_type_item_instance = ExpectationSummaryByTypeItem.from_json(json)
# print the JSON string representation of the object
print(ExpectationSummaryByTypeItem.to_json())

# convert the object into a dict
expectation_summary_by_type_item_dict = expectation_summary_by_type_item_instance.to_dict()
# create an instance of ExpectationSummaryByTypeItem from a dict
expectation_summary_by_type_item_from_dict = ExpectationSummaryByTypeItem.from_dict(expectation_summary_by_type_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


