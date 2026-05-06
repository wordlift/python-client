# CrawlJobInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website_url** | **str** | Canonical website URL used as crawl boundary. | 
**sitemaps** | **List[str]** | One or more sitemap URLs used as seed sources. | 
**max_concurrent_requests** | **int** |  | [optional] 
**max_pages** | **int** |  | [optional] 
**request_timeout_ms** | **int** | HTTP request timeout in milliseconds. | [optional] [default to 10000]
**render_timeout_ms** | **int** | Browser navigation timeout in milliseconds. | [optional] [default to 7000]
**request_handler_timeout_ms** | **int** | Per-request handler timeout in milliseconds. | [optional] [default to 18000]
**max_retries** | **int** | Maximum retry attempts per URL. | [optional] [default to 2]
**respect_robots** | **bool** | Whether to enforce robots.txt directives. | [optional] [default to True]
**crawl_delay_override** | **float** |  | [optional] 
**js_render_mode** | [**JsRenderMode**](JsRenderMode.md) |  | [optional] 
**discovery_sources** | [**DiscoverySources**](DiscoverySources.md) |  | [optional] 
**render_wait_until** | [**RenderWaitUntil**](RenderWaitUntil.md) |  | [optional] 
**render_wait_for_selector** | **str** |  | [optional] 
**render_wait_for_timeout_ms** | **int** | Additional fixed wait after navigation in milliseconds. | [optional] [default to 1500]
**render_wait_for_js** | **str** |  | [optional] 
**render_max_total_wait_ms** | **int** | Absolute cap for total render wait budget in milliseconds. | [optional] [default to 11000]

## Example

```python
from wordlift_client.models.crawl_job_input import CrawlJobInput

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlJobInput from a JSON string
crawl_job_input_instance = CrawlJobInput.from_json(json)
# print the JSON string representation of the object
print(CrawlJobInput.to_json())

# convert the object into a dict
crawl_job_input_dict = crawl_job_input_instance.to_dict()
# create an instance of CrawlJobInput from a dict
crawl_job_input_from_dict = CrawlJobInput.from_dict(crawl_job_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


