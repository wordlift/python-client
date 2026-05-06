# WebsitePageResolvedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **int** |  | 
**host** | **str** |  | 
**run_id** | **str** |  | 
**last_crawled_at** | **datetime** |  | 
**url_requested** | **str** |  | 
**url_final** | **str** |  | [optional] 
**canonical_url** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 
**xhtml** | **str** |  | [optional] 
**markdown** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.website_page_resolved_response import WebsitePageResolvedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebsitePageResolvedResponse from a JSON string
website_page_resolved_response_instance = WebsitePageResolvedResponse.from_json(json)
# print the JSON string representation of the object
print(WebsitePageResolvedResponse.to_json())

# convert the object into a dict
website_page_resolved_response_dict = website_page_resolved_response_instance.to_dict()
# create an instance of WebsitePageResolvedResponse from a dict
website_page_resolved_response_from_dict = WebsitePageResolvedResponse.from_dict(website_page_resolved_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


