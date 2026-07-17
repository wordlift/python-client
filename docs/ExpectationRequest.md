# ExpectationRequest

Body for ``POST /expectations``. Segment attachments are managed via the dedicated ``/expectations/{e}/segments`` endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_name** | [**MonitorCheckName**](MonitorCheckName.md) |  | 
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 
**config** | [**StructuredDataExpectationConfig**](StructuredDataExpectationConfig.md) |  | 

## Example

```python
from wordlift_client.models.expectation_request import ExpectationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectationRequest from a JSON string
expectation_request_instance = ExpectationRequest.from_json(json)
# print the JSON string representation of the object
print(ExpectationRequest.to_json())

# convert the object into a dict
expectation_request_dict = expectation_request_instance.to_dict()
# create an instance of ExpectationRequest from a dict
expectation_request_from_dict = ExpectationRequest.from_dict(expectation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


