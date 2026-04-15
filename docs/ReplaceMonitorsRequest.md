# ReplaceMonitorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReplaceMonitorItem]**](ReplaceMonitorItem.md) |  | 

## Example

```python
from wordlift_client.models.replace_monitors_request import ReplaceMonitorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceMonitorsRequest from a JSON string
replace_monitors_request_instance = ReplaceMonitorsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceMonitorsRequest.to_json())

# convert the object into a dict
replace_monitors_request_dict = replace_monitors_request_instance.to_dict()
# create an instance of ReplaceMonitorsRequest from a dict
replace_monitors_request_from_dict = ReplaceMonitorsRequest.from_dict(replace_monitors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


