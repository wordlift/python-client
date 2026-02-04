# MonitorSummaryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**state** | [**MonitorState**](MonitorState.md) |  | 
**details** | **str** |  | [optional] 
**score** | **float** |  | [optional] 

## Example

```python
from wordlift_client.models.monitor_summary_item import MonitorSummaryItem

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorSummaryItem from a JSON string
monitor_summary_item_instance = MonitorSummaryItem.from_json(json)
# print the JSON string representation of the object
print(MonitorSummaryItem.to_json())

# convert the object into a dict
monitor_summary_item_dict = monitor_summary_item_instance.to_dict()
# create an instance of MonitorSummaryItem from a dict
monitor_summary_item_from_dict = MonitorSummaryItem.from_dict(monitor_summary_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


