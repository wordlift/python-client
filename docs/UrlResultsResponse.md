# UrlResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**run_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**processed_at** | **datetime** |  | [optional] 
**results** | [**List[MonitorResultItem]**](MonitorResultItem.md) |  | 

## Example

```python
from wordlift_client.models.url_results_response import UrlResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UrlResultsResponse from a JSON string
url_results_response_instance = UrlResultsResponse.from_json(json)
# print the JSON string representation of the object
print(UrlResultsResponse.to_json())

# convert the object into a dict
url_results_response_dict = url_results_response_instance.to_dict()
# create an instance of UrlResultsResponse from a dict
url_results_response_from_dict = UrlResultsResponse.from_dict(url_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


