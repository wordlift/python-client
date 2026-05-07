# SegmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wordlift_client.models.segment_response import SegmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentResponse from a JSON string
segment_response_instance = SegmentResponse.from_json(json)
# print the JSON string representation of the object
print(SegmentResponse.to_json())

# convert the object into a dict
segment_response_dict = segment_response_instance.to_dict()
# create an instance of SegmentResponse from a dict
segment_response_from_dict = SegmentResponse.from_dict(segment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


