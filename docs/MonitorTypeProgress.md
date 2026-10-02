# MonitorTypeProgress

One monitor type's progress within a run. fetched isn't literally \"fetched\" for every type — it means \"reached a terminal, resolved outcome\" (mirrors how fetched_pages already counts both successful and failed fetches, not just successes). checked/failed are the disjoint subsets of fetched that resolved as checked vs. failed outright.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ResourceType**](ResourceType.md) |  | 
**dispatched** | **int** |  | 
**fetched** | **int** |  | 
**checked** | **int** |  | 
**failed** | **int** |  | 

## Example

```python
from wordlift_client.models.monitor_type_progress import MonitorTypeProgress

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorTypeProgress from a JSON string
monitor_type_progress_instance = MonitorTypeProgress.from_json(json)
# print the JSON string representation of the object
print(MonitorTypeProgress.to_json())

# convert the object into a dict
monitor_type_progress_dict = monitor_type_progress_instance.to_dict()
# create an instance of MonitorTypeProgress from a dict
monitor_type_progress_from_dict = MonitorTypeProgress.from_dict(monitor_type_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


