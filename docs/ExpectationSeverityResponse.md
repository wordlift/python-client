# ExpectationSeverityResponse

Response for ``GET /segments/{id}/expectations`` — the reverse of ``SegmentSeverityResponse``. Doesn't hydrate a full ``Expectation``; the caller either already holds the expectation catalog it needs or fetches it separately via ``GET /expectations?id=...``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expectation_id** | **str** |  | 
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 

## Example

```python
from wordlift_client.models.expectation_severity_response import ExpectationSeverityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectationSeverityResponse from a JSON string
expectation_severity_response_instance = ExpectationSeverityResponse.from_json(json)
# print the JSON string representation of the object
print(ExpectationSeverityResponse.to_json())

# convert the object into a dict
expectation_severity_response_dict = expectation_severity_response_instance.to_dict()
# create an instance of ExpectationSeverityResponse from a dict
expectation_severity_response_from_dict = ExpectationSeverityResponse.from_dict(expectation_severity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


