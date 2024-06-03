# AnalyticsImportRequest

An Analytics Import request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** | An array of URLs. | [optional] 

## Example

```python
from wordlift_client.models.analytics_import_request import AnalyticsImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsImportRequest from a JSON string
analytics_import_request_instance = AnalyticsImportRequest.from_json(json)
# print the JSON string representation of the object
print(AnalyticsImportRequest.to_json())

# convert the object into a dict
analytics_import_request_dict = analytics_import_request_instance.to_dict()
# create an instance of AnalyticsImportRequest from a dict
analytics_import_request_from_dict = AnalyticsImportRequest.from_dict(analytics_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


