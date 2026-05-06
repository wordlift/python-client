# PageArtifactQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PageArtifactQueryItem]**](PageArtifactQueryItem.md) |  | 
**run_id** | **str** |  | [optional] 
**as_of** | **datetime** |  | [optional] 

## Example

```python
from wordlift_client.models.page_artifact_query_request import PageArtifactQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PageArtifactQueryRequest from a JSON string
page_artifact_query_request_instance = PageArtifactQueryRequest.from_json(json)
# print the JSON string representation of the object
print(PageArtifactQueryRequest.to_json())

# convert the object into a dict
page_artifact_query_request_dict = page_artifact_query_request_instance.to_dict()
# create an instance of PageArtifactQueryRequest from a dict
page_artifact_query_request_from_dict = PageArtifactQueryRequest.from_dict(page_artifact_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


