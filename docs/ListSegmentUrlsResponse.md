# ListSegmentUrlsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SegmentUrlResponse]**](SegmentUrlResponse.md) |  | 
**total** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.list_segment_urls_response import ListSegmentUrlsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSegmentUrlsResponse from a JSON string
list_segment_urls_response_instance = ListSegmentUrlsResponse.from_json(json)
# print the JSON string representation of the object
print(ListSegmentUrlsResponse.to_json())

# convert the object into a dict
list_segment_urls_response_dict = list_segment_urls_response_instance.to_dict()
# create an instance of ListSegmentUrlsResponse from a dict
list_segment_urls_response_from_dict = ListSegmentUrlsResponse.from_dict(list_segment_urls_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


