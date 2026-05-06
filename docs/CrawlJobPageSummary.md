# CrawlJobPageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **int** | Persisted page identifier within this crawl job. | 
**last_crawled_at** | **datetime** | Timestamp when this page record finished processing. | 
**status** | [**CrawlPageStatus**](CrawlPageStatus.md) |  | 
**url_requested** | **str** | URL originally requested. | 
**url_final** | **str** |  | [optional] 
**canonical_url** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.crawl_job_page_summary import CrawlJobPageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlJobPageSummary from a JSON string
crawl_job_page_summary_instance = CrawlJobPageSummary.from_json(json)
# print the JSON string representation of the object
print(CrawlJobPageSummary.to_json())

# convert the object into a dict
crawl_job_page_summary_dict = crawl_job_page_summary_instance.to_dict()
# create an instance of CrawlJobPageSummary from a dict
crawl_job_page_summary_from_dict = CrawlJobPageSummary.from_dict(crawl_job_page_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


