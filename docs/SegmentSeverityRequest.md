# SegmentSeverityRequest

One entry of ``ReplaceExpectationSegmentsRequest.segments``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_id** | **str** |  | 
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 

## Example

```python
from wordlift_client.models.segment_severity_request import SegmentSeverityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentSeverityRequest from a JSON string
segment_severity_request_instance = SegmentSeverityRequest.from_json(json)
# print the JSON string representation of the object
print(SegmentSeverityRequest.to_json())

# convert the object into a dict
segment_severity_request_dict = segment_severity_request_instance.to_dict()
# create an instance of SegmentSeverityRequest from a dict
segment_severity_request_from_dict = SegmentSeverityRequest.from_dict(segment_severity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


