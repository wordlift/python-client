# ResponseListWebsitePagesWebsitesHostPagesGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WebsitePageSummary]**](WebsitePageSummary.md) |  | 
**page** | [**PaginationInfo**](PaginationInfo.md) |  | 
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
from wordlift_client.models.response_list_website_pages_websites_host_pages_get import ResponseListWebsitePagesWebsitesHostPagesGet

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseListWebsitePagesWebsitesHostPagesGet from a JSON string
response_list_website_pages_websites_host_pages_get_instance = ResponseListWebsitePagesWebsitesHostPagesGet.from_json(json)
# print the JSON string representation of the object
print(ResponseListWebsitePagesWebsitesHostPagesGet.to_json())

# convert the object into a dict
response_list_website_pages_websites_host_pages_get_dict = response_list_website_pages_websites_host_pages_get_instance.to_dict()
# create an instance of ResponseListWebsitePagesWebsitesHostPagesGet from a dict
response_list_website_pages_websites_host_pages_get_from_dict = ResponseListWebsitePagesWebsitesHostPagesGet.from_dict(response_list_website_pages_websites_host_pages_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


