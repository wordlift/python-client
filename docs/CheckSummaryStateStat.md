# CheckSummaryStateStat

One state slice of a by-check rollup item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**CheckSummaryState**](CheckSummaryState.md) |  | 
**monitor_count** | **int** |  | 
**check_result_count** | **int** |  | 

## Example

```python
from wordlift_client.models.check_summary_state_stat import CheckSummaryStateStat

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSummaryStateStat from a JSON string
check_summary_state_stat_instance = CheckSummaryStateStat.from_json(json)
# print the JSON string representation of the object
print(CheckSummaryStateStat.to_json())

# convert the object into a dict
check_summary_state_stat_dict = check_summary_state_stat_instance.to_dict()
# create an instance of CheckSummaryStateStat from a dict
check_summary_state_stat_from_dict = CheckSummaryStateStat.from_dict(check_summary_state_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


