# ListSegmentSeverityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SegmentSeverityResponse]**](SegmentSeverityResponse.md) |  | 
**total** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.list_segment_severity_response import ListSegmentSeverityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSegmentSeverityResponse from a JSON string
list_segment_severity_response_instance = ListSegmentSeverityResponse.from_json(json)
# print the JSON string representation of the object
print(ListSegmentSeverityResponse.to_json())

# convert the object into a dict
list_segment_severity_response_dict = list_segment_severity_response_instance.to_dict()
# create an instance of ListSegmentSeverityResponse from a dict
list_segment_severity_response_from_dict = ListSegmentSeverityResponse.from_dict(list_segment_severity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


