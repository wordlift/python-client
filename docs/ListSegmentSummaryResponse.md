# ListSegmentSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SegmentSummaryItem]**](SegmentSummaryItem.md) |  | 
**total** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.list_segment_summary_response import ListSegmentSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSegmentSummaryResponse from a JSON string
list_segment_summary_response_instance = ListSegmentSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(ListSegmentSummaryResponse.to_json())

# convert the object into a dict
list_segment_summary_response_dict = list_segment_summary_response_instance.to_dict()
# create an instance of ListSegmentSummaryResponse from a dict
list_segment_summary_response_from_dict = ListSegmentSummaryResponse.from_dict(list_segment_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


