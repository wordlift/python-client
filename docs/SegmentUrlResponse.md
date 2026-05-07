# SegmentUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**segment_id** | **str** |  | 
**url** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wordlift_client.models.segment_url_response import SegmentUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentUrlResponse from a JSON string
segment_url_response_instance = SegmentUrlResponse.from_json(json)
# print the JSON string representation of the object
print(SegmentUrlResponse.to_json())

# convert the object into a dict
segment_url_response_dict = segment_url_response_instance.to_dict()
# create an instance of SegmentUrlResponse from a dict
segment_url_response_from_dict = SegmentUrlResponse.from_dict(segment_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


