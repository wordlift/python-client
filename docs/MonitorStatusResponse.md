# MonitorStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_id** | **str** |  | 
**url** | **str** |  | 
**status** | [**MonitorStatusCheckStatus**](MonitorStatusCheckStatus.md) |  | 
**score** | **float** |  | [optional] 
**ttfb_ms** | **float** |  | [optional] 
**response_time_ms** | **float** |  | [optional] 
**status_code** | **int** |  | [optional] 
**last_fetch_success** | **bool** |  | [optional] 
**oldest_check_at** | **datetime** |  | [optional] 
**latest_check_at** | **datetime** |  | [optional] 
**checks** | **Dict[str, object]** |  | [optional] 

## Example

```python
from wordlift_client.models.monitor_status_response import MonitorStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorStatusResponse from a JSON string
monitor_status_response_instance = MonitorStatusResponse.from_json(json)
# print the JSON string representation of the object
print(MonitorStatusResponse.to_json())

# convert the object into a dict
monitor_status_response_dict = monitor_status_response_instance.to_dict()
# create an instance of MonitorStatusResponse from a dict
monitor_status_response_from_dict = MonitorStatusResponse.from_dict(monitor_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


