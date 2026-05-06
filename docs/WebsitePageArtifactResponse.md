# WebsitePageArtifactResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**page_id** | **int** |  | 
**run_id** | **str** |  | 
**artifact_type** | **str** |  | 
**as_of** | **datetime** |  | [optional] 
**content_type** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from wordlift_client.models.website_page_artifact_response import WebsitePageArtifactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebsitePageArtifactResponse from a JSON string
website_page_artifact_response_instance = WebsitePageArtifactResponse.from_json(json)
# print the JSON string representation of the object
print(WebsitePageArtifactResponse.to_json())

# convert the object into a dict
website_page_artifact_response_dict = website_page_artifact_response_instance.to_dict()
# create an instance of WebsitePageArtifactResponse from a dict
website_page_artifact_response_from_dict = WebsitePageArtifactResponse.from_dict(website_page_artifact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


