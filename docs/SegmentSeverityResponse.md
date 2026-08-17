# SegmentSeverityResponse

Response for every segment-attachment endpoint (attach, replace, and list) — none of them hydrates a full Segment. The frontend already holds the full segment catalog (a small, bounded set fetched on many pages), so this only needs to report segment_id/severity. Also doubles as the segment-membership shape nested in ExpectationEvaluationSummary below, since both are the same (segment_id, severity) pairing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_id** | **str** |  | 
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 

## Example

```python
from wordlift_client.models.segment_severity_response import SegmentSeverityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentSeverityResponse from a JSON string
segment_severity_response_instance = SegmentSeverityResponse.from_json(json)
# print the JSON string representation of the object
print(SegmentSeverityResponse.to_json())

# convert the object into a dict
segment_severity_response_dict = segment_severity_response_instance.to_dict()
# create an instance of SegmentSeverityResponse from a dict
segment_severity_response_from_dict = SegmentSeverityResponse.from_dict(segment_severity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


