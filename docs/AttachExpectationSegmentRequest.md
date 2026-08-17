# AttachExpectationSegmentRequest

Body for ``PUT /expectations/{id}/segments/{segment_id}``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 

## Example

```python
from wordlift_client.models.attach_expectation_segment_request import AttachExpectationSegmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachExpectationSegmentRequest from a JSON string
attach_expectation_segment_request_instance = AttachExpectationSegmentRequest.from_json(json)
# print the JSON string representation of the object
print(AttachExpectationSegmentRequest.to_json())

# convert the object into a dict
attach_expectation_segment_request_dict = attach_expectation_segment_request_instance.to_dict()
# create an instance of AttachExpectationSegmentRequest from a dict
attach_expectation_segment_request_from_dict = AttachExpectationSegmentRequest.from_dict(attach_expectation_segment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


