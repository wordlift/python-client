# AnalyticsSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The Account identifier | [optional] [readonly] 
**created_at** | **datetime** | The creation date-time. | [optional] [readonly] 
**id** | **str** | The resource identifier | [optional] [readonly] 
**queries_retrieved** | **int** | Total number of queries retrieved by the analytics provider. | [optional] [readonly] 
**retrievable_urls** | **int** | Number of URLs processable by the analytics provider based on the Account URL. | [optional] [readonly] 
**started_at** | **datetime** | The started date-time. | [optional] [readonly] 
**status** | **str** | Status of the sync process. | [optional] [readonly] 
**stopped_at** | **datetime** | The stopped date-time. | [optional] [readonly] 
**total_entities_updated** | **int** | Number of unique entities updated with analytics by this sync. | [optional] [readonly] 
**urls_in_dataset** | **int** | Number of total URLs retrieved from dataset entities | [optional] [readonly] 

## Example

```python
from wordlift_client.models.analytics_sync import AnalyticsSync

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsSync from a JSON string
analytics_sync_instance = AnalyticsSync.from_json(json)
# print the JSON string representation of the object
print(AnalyticsSync.to_json())

# convert the object into a dict
analytics_sync_dict = analytics_sync_instance.to_dict()
# create an instance of AnalyticsSync from a dict
analytics_sync_from_dict = AnalyticsSync.from_dict(analytics_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


