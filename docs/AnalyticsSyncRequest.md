# AnalyticsSyncRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 

## Example

```python
from wordlift_client.models.analytics_sync_request import AnalyticsSyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsSyncRequest from a JSON string
analytics_sync_request_instance = AnalyticsSyncRequest.from_json(json)
# print the JSON string representation of the object
print(AnalyticsSyncRequest.to_json())

# convert the object into a dict
analytics_sync_request_dict = analytics_sync_request_instance.to_dict()
# create an instance of AnalyticsSyncRequest from a dict
analytics_sync_request_from_dict = AnalyticsSyncRequest.from_dict(analytics_sync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


