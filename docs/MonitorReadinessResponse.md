# MonitorReadinessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**timestamp** | **datetime** |  | 
**services** | **Dict[str, str]** |  | 
**errors** | **Dict[str, str]** |  | [optional] 

## Example

```python
from wordlift_client.models.monitor_readiness_response import MonitorReadinessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorReadinessResponse from a JSON string
monitor_readiness_response_instance = MonitorReadinessResponse.from_json(json)
# print the JSON string representation of the object
print(MonitorReadinessResponse.to_json())

# convert the object into a dict
monitor_readiness_response_dict = monitor_readiness_response_instance.to_dict()
# create an instance of MonitorReadinessResponse from a dict
monitor_readiness_response_from_dict = MonitorReadinessResponse.from_dict(monitor_readiness_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


