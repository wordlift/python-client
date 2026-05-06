# CrawlJobCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Server-generated crawl job identifier. | 
**run_id** | **str** | Execution run identifier used to correlate pages and logs. | 
**status** | [**JobStatus**](JobStatus.md) |  | 
**created_at** | **datetime** | Job creation timestamp (UTC). | 

## Example

```python
from wordlift_client.models.crawl_job_create_response import CrawlJobCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlJobCreateResponse from a JSON string
crawl_job_create_response_instance = CrawlJobCreateResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlJobCreateResponse.to_json())

# convert the object into a dict
crawl_job_create_response_dict = crawl_job_create_response_instance.to_dict()
# create an instance of CrawlJobCreateResponse from a dict
crawl_job_create_response_from_dict = CrawlJobCreateResponse.from_dict(crawl_job_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


