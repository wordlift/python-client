# MonitorValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[LocationInner]**](LocationInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 
**input** | **object** |  | [optional] 
**ctx** | **object** |  | [optional] 

## Example

```python
from wordlift_client.models.monitor_validation_error import MonitorValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorValidationError from a JSON string
monitor_validation_error_instance = MonitorValidationError.from_json(json)
# print the JSON string representation of the object
print(MonitorValidationError.to_json())

# convert the object into a dict
monitor_validation_error_dict = monitor_validation_error_instance.to_dict()
# create an instance of MonitorValidationError from a dict
monitor_validation_error_from_dict = MonitorValidationError.from_dict(monitor_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


