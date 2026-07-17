# MonitorRunResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**MonitorRunStatus**](MonitorRunStatus.md) |  | 
**dispatched_pages** | **int** |  | 
**fetched_pages** | **int** |  | 
**failed_fetches** | **int** |  | 
**checked_pages** | **int** |  | 
**end_at** | **datetime** |  | [optional] 
**last_progress_at** | **datetime** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wordlift_client.models.monitor_run_response import MonitorRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorRunResponse from a JSON string
monitor_run_response_instance = MonitorRunResponse.from_json(json)
# print the JSON string representation of the object
print(MonitorRunResponse.to_json())

# convert the object into a dict
monitor_run_response_dict = monitor_run_response_instance.to_dict()
# create an instance of MonitorRunResponse from a dict
monitor_run_response_from_dict = MonitorRunResponse.from_dict(monitor_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


