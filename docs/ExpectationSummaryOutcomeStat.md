# ExpectationSummaryOutcomeStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | [**ExpectationSummaryOutcome**](ExpectationSummaryOutcome.md) |  | 
**monitor_count** | **int** |  | 

## Example

```python
from wordlift_client.models.expectation_summary_outcome_stat import ExpectationSummaryOutcomeStat

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectationSummaryOutcomeStat from a JSON string
expectation_summary_outcome_stat_instance = ExpectationSummaryOutcomeStat.from_json(json)
# print the JSON string representation of the object
print(ExpectationSummaryOutcomeStat.to_json())

# convert the object into a dict
expectation_summary_outcome_stat_dict = expectation_summary_outcome_stat_instance.to_dict()
# create an instance of ExpectationSummaryOutcomeStat from a dict
expectation_summary_outcome_stat_from_dict = ExpectationSummaryOutcomeStat.from_dict(expectation_summary_outcome_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


