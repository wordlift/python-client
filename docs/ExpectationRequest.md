# ExpectationRequest

Body for ``POST /expectations``.  ``config`` is typed as ``AnyExpectationConfig`` — the extension point that will hold a union once a second check type ships. Pydantic validates the concrete shape per-field (422 on bad input). Segment attachments are managed via the dedicated ``PUT/DELETE /expectations/{e}/segments[/{s}]`` endpoints.

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


