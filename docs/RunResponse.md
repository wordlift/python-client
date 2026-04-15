# RunResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**MonitorRunStatus**](MonitorRunStatus.md) |  | 
**dispatched_pages** | **int** |  | 
**fetched_pages** | **int** |  | 
**failed_fetches** | **int** |  | 
**checked_pages** | **int** |  | 
**end_at** | **datetime** |  | [optional] 
**last_progress_at** | **datetime** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wordlift_client.models.run_response import RunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunResponse from a JSON string
run_response_instance = RunResponse.from_json(json)
# print the JSON string representation of the object
print(RunResponse.to_json())

# convert the object into a dict
run_response_dict = run_response_instance.to_dict()
# create an instance of RunResponse from a dict
run_response_from_dict = RunResponse.from_dict(run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


