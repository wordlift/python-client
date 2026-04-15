# ListMonitorStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MonitorStatusResponse]**](MonitorStatusResponse.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.list_monitor_status_response import ListMonitorStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMonitorStatusResponse from a JSON string
list_monitor_status_response_instance = ListMonitorStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ListMonitorStatusResponse.to_json())

# convert the object into a dict
list_monitor_status_response_dict = list_monitor_status_response_instance.to_dict()
# create an instance of ListMonitorStatusResponse from a dict
list_monitor_status_response_from_dict = ListMonitorStatusResponse.from_dict(list_monitor_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


