# FetchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the fetch completed successfully. | 
**url_requested** | **str** | The URL originally requested. | 
**url_final** | **str** | The final URL after any redirects. | 
**status_code** | **int** | HTTP response status code. | [optional] 
**content_type** | **str** | Response Content-Type header value. | [optional] 
**body** | **str** | The fetched document as UTF-8 text: HTML with its &lt;meta charset&gt; rewritten to UTF-8, or a plain text, Markdown, JSON or XML body unchanged except for the XML declaration&#39;s encoding, rewritten to UTF-8. | [optional] 
**original_charset** | **str** | Charset the body was decoded with before normalization to UTF-8, as a browser picks it, under its WHATWG Encoding Standard name: Latin-1 and ASCII labels report windows-1252, gb2312 reports gbk. Labels browsers don&#39;t know are skipped; utf-8 when none is declared. | [optional] 
**markdown** | **str** | Page content extracted as Markdown. For a Markdown response, the body itself; null for plain text, JSON and XML responses. | [optional] 
**title** | **str** | Page title extracted by trafilatura. Null for plain text, Markdown, JSON and XML responses. | [optional] 
**description** | **str** | Page description/abstract extracted by trafilatura. Null for plain text, Markdown, JSON and XML responses. | [optional] 
**text** | **str** | Plain text content extracted by trafilatura. Null for plain text, Markdown, JSON and XML responses. | [optional] 
**error_code** | **str** | Machine-readable error code if the fetch failed. | [optional] 
**error_message** | **str** | Human-readable error detail if the fetch failed. | [optional] 
**ttfb_ms** | **int** | Time to first byte in milliseconds. | [optional] 
**response_time_ms** | **int** | Total response time in milliseconds (from request sent to body received). | [optional] 
**networkidle_response_time_ms** | **int** | Time in milliseconds from request sent until Playwright&#39;s &#39;networkidle&#39; load event, when target_load_event&#x3D;&#39;networkidle&#39; was requested. | [optional] 
**fetched_at** | **datetime** | When the page was fetched. Significantly older than now means the result was served from cache. | [optional] 
**from_cache** | **bool** | True when the response was served from a previously stored fetch result. | [optional] [default to False]
**har** | **Dict[str, object]** | HAR 1.2 log of all network activity captured during the fetch. Null when not available for the given fetch strategy. | [optional] 
**effective_proxy_mode** | [**ProxyTier**](ProxyTier.md) | Proxy tier of the final fetch attempt, after any proxy_mode&#x3D;&#39;auto&#39; escalation. For cache hits, the tier of the fetch that produced the cached content. Null when the fetch worker did not respond, or for cache entries stored before the tier was recorded. | [optional] 
**html** | **str** | Deprecated: same value as &#x60;body&#x60;, which also carries non-HTML bodies. | [optional] [readonly] 
**har_truncated** | **bool** | True when the HAR log was truncated after hitting the size cap, so it covers only part of the page&#39;s network activity. | [readonly] 

## Example

```python
from wordlift_client.models.fetch_response import FetchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchResponse from a JSON string
fetch_response_instance = FetchResponse.from_json(json)
# print the JSON string representation of the object
print(FetchResponse.to_json())

# convert the object into a dict
fetch_response_dict = fetch_response_instance.to_dict()
# create an instance of FetchResponse from a dict
fetch_response_from_dict = FetchResponse.from_dict(fetch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


