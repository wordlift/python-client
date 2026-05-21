# ReplaceExpectationSegmentsRequest

Body for ``PUT /expectations/{id}/segments``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_ids** | **List[str]** |  | 

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


