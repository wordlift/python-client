# UrlSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**status** | **str** |  | 
**last_run** | **datetime** |  | [optional] 
**score** | **float** |  | [optional] 
**ttfb_ms** | **float** |  | [optional] 
**response_time_ms** | **float** |  | [optional] 
**monitors** | [**List[MonitorSummaryItem]**](MonitorSummaryItem.md) |  | 
**neighbors** | [**Neighbors**](Neighbors.md) |  | 

## Example

```python
from wordlift_client.models.url_summary_response import UrlSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UrlSummaryResponse from a JSON string
url_summary_response_instance = UrlSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(UrlSummaryResponse.to_json())

# convert the object into a dict
url_summary_response_dict = url_summary_response_instance.to_dict()
# create an instance of UrlSummaryResponse from a dict
url_summary_response_from_dict = UrlSummaryResponse.from_dict(url_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


