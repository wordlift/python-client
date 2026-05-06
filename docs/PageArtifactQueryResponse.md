# PageArtifactQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PageArtifactQueryResultItem]**](PageArtifactQueryResultItem.md) |  | 

## Example

```python
from wordlift_client.models.page_artifact_query_response import PageArtifactQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageArtifactQueryResponse from a JSON string
page_artifact_query_response_instance = PageArtifactQueryResponse.from_json(json)
# print the JSON string representation of the object
print(PageArtifactQueryResponse.to_json())

# convert the object into a dict
page_artifact_query_response_dict = page_artifact_query_response_instance.to_dict()
# create an instance of PageArtifactQueryResponse from a dict
page_artifact_query_response_from_dict = PageArtifactQueryResponse.from_dict(page_artifact_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


