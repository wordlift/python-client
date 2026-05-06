# FetchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the fetch completed successfully. | 
**url_requested** | **str** | The URL originally requested. | 
**url_final** | **str** | The final URL after any redirects. | 
**status_code** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**original_charset** | **str** |  | [optional] 
**markdown** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**ttfb_ms** | **int** |  | [optional] 
**response_time_ms** | **int** |  | [optional] 
**fetched_at** | **datetime** |  | [optional] 
**from_cache** | **bool** | True when the response was served from a previously stored fetch result. | [optional] [default to False]

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


