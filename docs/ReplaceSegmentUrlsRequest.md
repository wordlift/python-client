# ReplaceSegmentUrlsRequest

Body for ``PUT /segments/{id}/urls``.  URLs are normalized and validated to be in scope of the account base (``is_in_scope``); any out-of-scope URL fails the whole request with 422 listing the offenders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** |  | 

## Example

```python
from wordlift_client.models.replace_segment_urls_request import ReplaceSegmentUrlsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceSegmentUrlsRequest from a JSON string
replace_segment_urls_request_instance = ReplaceSegmentUrlsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceSegmentUrlsRequest.to_json())

# convert the object into a dict
replace_segment_urls_request_dict = replace_segment_urls_request_instance.to_dict()
# create an instance of ReplaceSegmentUrlsRequest from a dict
replace_segment_urls_request_from_dict = ReplaceSegmentUrlsRequest.from_dict(replace_segment_urls_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


