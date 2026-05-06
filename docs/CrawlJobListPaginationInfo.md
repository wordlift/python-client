# CrawlJobListPaginationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Zero-based list offset. | 
**limit** | **int** | Maximum number of items requested. | 
**total** | **int** | Total number of matching crawl jobs. | 

## Example

```python
from wordlift_client.models.crawl_job_list_pagination_info import CrawlJobListPaginationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlJobListPaginationInfo from a JSON string
crawl_job_list_pagination_info_instance = CrawlJobListPaginationInfo.from_json(json)
# print the JSON string representation of the object
print(CrawlJobListPaginationInfo.to_json())

# convert the object into a dict
crawl_job_list_pagination_info_dict = crawl_job_list_pagination_info_instance.to_dict()
# create an instance of CrawlJobListPaginationInfo from a dict
crawl_job_list_pagination_info_from_dict = CrawlJobListPaginationInfo.from_dict(crawl_job_list_pagination_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


