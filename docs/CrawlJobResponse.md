# CrawlJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Job identifier. | 
**run_id** | **str** | Execution run identifier. | 
**status** | [**JobStatus**](JobStatus.md) |  | 
**created_at** | **datetime** | Job creation timestamp (UTC). | 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**input** | [**CrawlJobInput**](CrawlJobInput.md) |  | 
**pages_total** | **int** | Total number of persisted page results for this job. | [optional] [default to 0]
**pages_with_error** | **int** | Number of persisted page results with crawl/HTTP errors. | [optional] [default to 0]
**error_message** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.crawl_job_response import CrawlJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlJobResponse from a JSON string
crawl_job_response_instance = CrawlJobResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlJobResponse.to_json())

# convert the object into a dict
crawl_job_response_dict = crawl_job_response_instance.to_dict()
# create an instance of CrawlJobResponse from a dict
crawl_job_response_from_dict = CrawlJobResponse.from_dict(crawl_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


