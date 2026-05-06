# WebsitePageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **int** |  | 
**host** | **str** |  | 
**run_id** | **str** |  | 
**last_crawled_at** | **datetime** |  | 
**status** | [**CrawlPageStatus**](CrawlPageStatus.md) |  | 
**url_requested** | **str** |  | 
**url_final** | **str** |  | [optional] 
**canonical_url** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from wordlift_client.models.website_page_summary import WebsitePageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WebsitePageSummary from a JSON string
website_page_summary_instance = WebsitePageSummary.from_json(json)
# print the JSON string representation of the object
print(WebsitePageSummary.to_json())

# convert the object into a dict
website_page_summary_dict = website_page_summary_instance.to_dict()
# create an instance of WebsitePageSummary from a dict
website_page_summary_from_dict = WebsitePageSummary.from_dict(website_page_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


