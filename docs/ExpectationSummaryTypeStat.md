# ExpectationSummaryTypeStat

One (severity, outcome) slice of a by-type rollup item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 
**outcome** | [**ExpectationSummaryOutcome**](ExpectationSummaryOutcome.md) |  | 
**monitor_count** | **int** |  | 
**expectation_count** | **int** |  | 
**expectation_evaluation_count** | **int** |  | 

## Example

```python
from wordlift_client.models.expectation_summary_type_stat import ExpectationSummaryTypeStat

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectationSummaryTypeStat from a JSON string
expectation_summary_type_stat_instance = ExpectationSummaryTypeStat.from_json(json)
# print the JSON string representation of the object
print(ExpectationSummaryTypeStat.to_json())

# convert the object into a dict
expectation_summary_type_stat_dict = expectation_summary_type_stat_instance.to_dict()
# create an instance of ExpectationSummaryTypeStat from a dict
expectation_summary_type_stat_from_dict = ExpectationSummaryTypeStat.from_dict(expectation_summary_type_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


