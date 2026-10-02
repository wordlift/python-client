# MonitorSeverityResponse

Response for the monitor-attachment endpoint — the account-scoped (URL-less) analog of ``SegmentSeverityResponse``. No hydration of the full Monitor, matching that precedent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_id** | **str** |  | 
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 

## Example

```python
from wordlift_client.models.monitor_severity_response import MonitorSeverityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorSeverityResponse from a JSON string
monitor_severity_response_instance = MonitorSeverityResponse.from_json(json)
# print the JSON string representation of the object
print(MonitorSeverityResponse.to_json())

# convert the object into a dict
monitor_severity_response_dict = monitor_severity_response_instance.to_dict()
# create an instance of MonitorSeverityResponse from a dict
monitor_severity_response_from_dict = MonitorSeverityResponse.from_dict(monitor_severity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


