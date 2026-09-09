# ReplaceExpectationSegmentsRequest

Body for ``PUT /expectations/{id}/segments``.  The per-segment expectation cap (``MAX_EXPECTATIONS_PER_SEGMENT``) can't be checked from this payload alone — it depends on how many *other* expectations each target segment already has attached. That's enforced with a 409 in ``ExpectationService`` instead (see ``_assert_segment_has_capacity``).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segments** | [**List[SegmentSeverityRequest]**](SegmentSeverityRequest.md) |  | 

## Example

```python
from wordlift_client.models.replace_expectation_segments_request import ReplaceExpectationSegmentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceExpectationSegmentsRequest from a JSON string
replace_expectation_segments_request_instance = ReplaceExpectationSegmentsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceExpectationSegmentsRequest.to_json())

# convert the object into a dict
replace_expectation_segments_request_dict = replace_expectation_segments_request_instance.to_dict()
# create an instance of ReplaceExpectationSegmentsRequest from a dict
replace_expectation_segments_request_from_dict = ReplaceExpectationSegmentsRequest.from_dict(replace_expectation_segments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


