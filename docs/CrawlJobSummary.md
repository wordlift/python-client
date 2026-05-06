# CrawlJobSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Job identifier. | 
**run_id** | **str** | Execution run identifier. | 
**status** | [**JobStatus**](JobStatus.md) |  | 
**created_at** | **datetime** | Job creation timestamp (UTC). | 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**website_url** | **str** | Canonical website URL used as crawl boundary. | 
**sitemaps** | **List[str]** | Sitemap URLs configured for this crawl job. | 
**pages_count** | **int** | Number of persisted page results for this job. | [optional] [default to 0]

## Example

```python
from wordlift_client.models.crawl_job_summary import CrawlJobSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlJobSummary from a JSON string
crawl_job_summary_instance = CrawlJobSummary.from_json(json)
# print the JSON string representation of the object
print(CrawlJobSummary.to_json())

# convert the object into a dict
crawl_job_summary_dict = crawl_job_summary_instance.to_dict()
# create an instance of CrawlJobSummary from a dict
crawl_job_summary_from_dict = CrawlJobSummary.from_dict(crawl_job_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


