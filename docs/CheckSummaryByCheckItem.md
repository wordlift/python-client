# CheckSummaryByCheckItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_id** | **str** |  | 
**check_name** | [**MonitorCheckName**](MonitorCheckName.md) |  | 
**monitor_count** | **int** |  | 
**check_result_count** | **int** |  | 
**stats** | [**List[CheckSummaryStateStat]**](CheckSummaryStateStat.md) |  | 

## Example

```python
from wordlift_client.models.check_summary_by_check_item import CheckSummaryByCheckItem

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSummaryByCheckItem from a JSON string
check_summary_by_check_item_instance = CheckSummaryByCheckItem.from_json(json)
# print the JSON string representation of the object
print(CheckSummaryByCheckItem.to_json())

# convert the object into a dict
check_summary_by_check_item_dict = check_summary_by_check_item_instance.to_dict()
# create an instance of CheckSummaryByCheckItem from a dict
check_summary_by_check_item_from_dict = CheckSummaryByCheckItem.from_dict(check_summary_by_check_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


