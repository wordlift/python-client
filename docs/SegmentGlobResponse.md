# SegmentGlobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**segment_id** | **str** |  | 
**pattern** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wordlift_client.models.segment_glob_response import SegmentGlobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentGlobResponse from a JSON string
segment_glob_response_instance = SegmentGlobResponse.from_json(json)
# print the JSON string representation of the object
print(SegmentGlobResponse.to_json())

# convert the object into a dict
segment_glob_response_dict = segment_glob_response_instance.to_dict()
# create an instance of SegmentGlobResponse from a dict
segment_glob_response_from_dict = SegmentGlobResponse.from_dict(segment_glob_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


