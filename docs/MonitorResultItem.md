# MonitorResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_name** | **str** |  | 
**state** | [**MonitorState**](MonitorState.md) |  | 
**details** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | 
**processed_at** | **datetime** |  | [optional] 

## Example

```python
from wordlift_client.models.monitor_result_item import MonitorResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorResultItem from a JSON string
monitor_result_item_instance = MonitorResultItem.from_json(json)
# print the JSON string representation of the object
print(MonitorResultItem.to_json())

# convert the object into a dict
monitor_result_item_dict = monitor_result_item_instance.to_dict()
# create an instance of MonitorResultItem from a dict
monitor_result_item_from_dict = MonitorResultItem.from_dict(monitor_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


