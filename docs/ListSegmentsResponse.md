# ListSegmentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SegmentResponse]**](SegmentResponse.md) |  | 
**total** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.list_segments_response import ListSegmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSegmentsResponse from a JSON string
list_segments_response_instance = ListSegmentsResponse.from_json(json)
# print the JSON string representation of the object
print(ListSegmentsResponse.to_json())

# convert the object into a dict
list_segments_response_dict = list_segments_response_instance.to_dict()
# create an instance of ListSegmentsResponse from a dict
list_segments_response_from_dict = ListSegmentsResponse.from_dict(list_segments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


