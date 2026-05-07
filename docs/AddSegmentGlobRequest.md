# AddSegmentGlobRequest

Body for ``POST /segments/{id}/globs``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** |  | 

## Example

```python
from wordlift_client.models.add_segment_glob_request import AddSegmentGlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddSegmentGlobRequest from a JSON string
add_segment_glob_request_instance = AddSegmentGlobRequest.from_json(json)
# print the JSON string representation of the object
print(AddSegmentGlobRequest.to_json())

# convert the object into a dict
add_segment_glob_request_dict = add_segment_glob_request_instance.to_dict()
# create an instance of AddSegmentGlobRequest from a dict
add_segment_glob_request_from_dict = AddSegmentGlobRequest.from_dict(add_segment_glob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


