# ReplaceSegmentGlobsRequest

Body for ``PUT /segments/{id}/globs``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patterns** | **List[str]** |  | 

## Example

```python
from wordlift_client.models.replace_segment_globs_request import ReplaceSegmentGlobsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceSegmentGlobsRequest from a JSON string
replace_segment_globs_request_instance = ReplaceSegmentGlobsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceSegmentGlobsRequest.to_json())

# convert the object into a dict
replace_segment_globs_request_dict = replace_segment_globs_request_instance.to_dict()
# create an instance of ReplaceSegmentGlobsRequest from a dict
replace_segment_globs_request_from_dict = ReplaceSegmentGlobsRequest.from_dict(replace_segment_globs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


