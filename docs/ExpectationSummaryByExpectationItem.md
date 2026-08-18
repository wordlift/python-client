# ExpectationSummaryByExpectationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_id** | **str** |  | 
**expectation_id** | **str** |  | 
**stats** | [**List[ExpectationSummaryOutcomeStat]**](ExpectationSummaryOutcomeStat.md) |  | 

## Example

```python
from wordlift_client.models.expectation_summary_by_expectation_item import ExpectationSummaryByExpectationItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectationSummaryByExpectationItem from a JSON string
expectation_summary_by_expectation_item_instance = ExpectationSummaryByExpectationItem.from_json(json)
# print the JSON string representation of the object
print(ExpectationSummaryByExpectationItem.to_json())

# convert the object into a dict
expectation_summary_by_expectation_item_dict = expectation_summary_by_expectation_item_instance.to_dict()
# create an instance of ExpectationSummaryByExpectationItem from a dict
expectation_summary_by_expectation_item_from_dict = ExpectationSummaryByExpectationItem.from_dict(expectation_summary_by_expectation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


