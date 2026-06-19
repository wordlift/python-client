# MonitorHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[MonitorValidationError]**](MonitorValidationError.md) |  | [optional] 

## Example

```python
from wordlift_client.models.monitor_http_validation_error import MonitorHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorHTTPValidationError from a JSON string
monitor_http_validation_error_instance = MonitorHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(MonitorHTTPValidationError.to_json())

# convert the object into a dict
monitor_http_validation_error_dict = monitor_http_validation_error_instance.to_dict()
# create an instance of MonitorHTTPValidationError from a dict
monitor_http_validation_error_from_dict = MonitorHTTPValidationError.from_dict(monitor_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


