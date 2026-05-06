# WebsitePageResponse


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
**xhtml_available** | **bool** |  | [optional] [default to False]
**markdown_available** | **bool** |  | [optional] [default to False]

## Example

```python
from wordlift_client.models.website_page_response import WebsitePageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebsitePageResponse from a JSON string
website_page_response_instance = WebsitePageResponse.from_json(json)
# print the JSON string representation of the object
print(WebsitePageResponse.to_json())

# convert the object into a dict
website_page_response_dict = website_page_response_instance.to_dict()
# create an instance of WebsitePageResponse from a dict
website_page_response_from_dict = WebsitePageResponse.from_dict(website_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


