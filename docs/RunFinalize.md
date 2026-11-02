# RunFinalize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**RunStatus**](RunStatus.md) |  | 
**url_count** | **int** | Total URLs in this run. | [optional] 
**failure_count** | **int** | Total URL failures. | [optional] 
**ended_at** | **datetime** | Client-side wall-clock time when the run ended. | [optional] 

## Example

```python
from wordlift_client.models.run_finalize import RunFinalize

# TODO update the JSON string below
json = "{}"
# create an instance of RunFinalize from a JSON string
run_finalize_instance = RunFinalize.from_json(json)
# print the JSON string representation of the object
print(RunFinalize.to_json())

# convert the object into a dict
run_finalize_dict = run_finalize_instance.to_dict()
# create an instance of RunFinalize from a dict
run_finalize_from_dict = RunFinalize.from_dict(run_finalize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


