# PageArtifactQueryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **int** |  | 
**artifact_type** | **str** |  | 

## Example

```python
from wordlift_client.models.page_artifact_query_item import PageArtifactQueryItem

# TODO update the JSON string below
json = "{}"
# create an instance of PageArtifactQueryItem from a JSON string
page_artifact_query_item_instance = PageArtifactQueryItem.from_json(json)
# print the JSON string representation of the object
print(PageArtifactQueryItem.to_json())

# convert the object into a dict
page_artifact_query_item_dict = page_artifact_query_item_instance.to_dict()
# create an instance of PageArtifactQueryItem from a dict
page_artifact_query_item_from_dict = PageArtifactQueryItem.from_dict(page_artifact_query_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


