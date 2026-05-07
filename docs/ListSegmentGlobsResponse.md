# ListSegmentGlobsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SegmentGlobResponse]**](SegmentGlobResponse.md) |  | 
**total** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.list_segment_globs_response import ListSegmentGlobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSegmentGlobsResponse from a JSON string
list_segment_globs_response_instance = ListSegmentGlobsResponse.from_json(json)
# print the JSON string representation of the object
print(ListSegmentGlobsResponse.to_json())

# convert the object into a dict
list_segment_globs_response_dict = list_segment_globs_response_instance.to_dict()
# create an instance of ListSegmentGlobsResponse from a dict
list_segment_globs_response_from_dict = ListSegmentGlobsResponse.from_dict(list_segment_globs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


