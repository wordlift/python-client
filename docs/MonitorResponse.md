# MonitorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url** | **str** |  | 
**type** | [**ResourceType**](ResourceType.md) |  | 
**is_enabled** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wordlift_client.models.monitor_response import MonitorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorResponse from a JSON string
monitor_response_instance = MonitorResponse.from_json(json)
# print the JSON string representation of the object
print(MonitorResponse.to_json())

# convert the object into a dict
monitor_response_dict = monitor_response_instance.to_dict()
# create an instance of MonitorResponse from a dict
monitor_response_from_dict = MonitorResponse.from_dict(monitor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


