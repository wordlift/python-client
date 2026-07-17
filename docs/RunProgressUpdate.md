# RunProgressUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls_processed** | **int** | Cumulative number of URLs processed so far. | 
**entities_so_far** | **int** | Cumulative number of entities synced so far. | 

## Example

```python
from wordlift_client.models.run_progress_update import RunProgressUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RunProgressUpdate from a JSON string
run_progress_update_instance = RunProgressUpdate.from_json(json)
# print the JSON string representation of the object
print(RunProgressUpdate.to_json())

# convert the object into a dict
run_progress_update_dict = run_progress_update_instance.to_dict()
# create an instance of RunProgressUpdate from a dict
run_progress_update_from_dict = RunProgressUpdate.from_dict(run_progress_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


