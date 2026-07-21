# AddSegmentUrlRequest

Body for ``POST /segments/{id}/urls``.  URL is normalized and validated to be in scope of the account base (``is_in_scope``); out-of-scope URLs are rejected with 422.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from wordlift_client.models.add_segment_url_request import AddSegmentUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddSegmentUrlRequest from a JSON string
add_segment_url_request_instance = AddSegmentUrlRequest.from_json(json)
# print the JSON string representation of the object
print(AddSegmentUrlRequest.to_json())

# convert the object into a dict
add_segment_url_request_dict = add_segment_url_request_instance.to_dict()
# create an instance of AddSegmentUrlRequest from a dict
add_segment_url_request_from_dict = AddSegmentUrlRequest.from_dict(add_segment_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


