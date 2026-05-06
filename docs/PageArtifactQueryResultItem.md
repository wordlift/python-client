# PageArtifactQueryResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **int** |  | 
**artifact_type** | **str** |  | 
**content_type** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.page_artifact_query_result_item import PageArtifactQueryResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of PageArtifactQueryResultItem from a JSON string
page_artifact_query_result_item_instance = PageArtifactQueryResultItem.from_json(json)
# print the JSON string representation of the object
print(PageArtifactQueryResultItem.to_json())

# convert the object into a dict
page_artifact_query_result_item_dict = page_artifact_query_result_item_instance.to_dict()
# create an instance of PageArtifactQueryResultItem from a dict
page_artifact_query_result_item_from_dict = PageArtifactQueryResultItem.from_dict(page_artifact_query_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


