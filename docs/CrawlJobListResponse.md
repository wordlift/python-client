# CrawlJobListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CrawlJobSummary]**](CrawlJobSummary.md) | List of crawl jobs ordered by newest first. | 
**page** | [**CrawlJobListPaginationInfo**](CrawlJobListPaginationInfo.md) |  | 

## Example

```python
from wordlift_client.models.crawl_job_list_response import CrawlJobListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlJobListResponse from a JSON string
crawl_job_list_response_instance = CrawlJobListResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlJobListResponse.to_json())

# convert the object into a dict
crawl_job_list_response_dict = crawl_job_list_response_instance.to_dict()
# create an instance of CrawlJobListResponse from a dict
crawl_job_list_response_from_dict = CrawlJobListResponse.from_dict(crawl_job_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


