# CrawlJobPageListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CrawlJobPageSummary]**](CrawlJobPageSummary.md) | Page summaries for this crawl job. | 
**page** | [**CrawlJobListPaginationInfo**](CrawlJobListPaginationInfo.md) |  | 

## Example

```python
from wordlift_client.models.crawl_job_page_list_response import CrawlJobPageListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlJobPageListResponse from a JSON string
crawl_job_page_list_response_instance = CrawlJobPageListResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlJobPageListResponse.to_json())

# convert the object into a dict
crawl_job_page_list_response_dict = crawl_job_page_list_response_instance.to_dict()
# create an instance of CrawlJobPageListResponse from a dict
crawl_job_page_list_response_from_dict = CrawlJobPageListResponse.from_dict(crawl_job_page_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


