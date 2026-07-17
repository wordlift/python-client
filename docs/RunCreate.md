# RunCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **str** | Graph sync profile name. | 
**sdk_version** | **str** | wordlift-sdk version used for this run. | 
**worai_version** | **str** |  | [optional] 
**started_at** | **datetime** | Client-side wall-clock time when the run started. | 

## Example

```python
from wordlift_client.models.run_create import RunCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RunCreate from a JSON string
run_create_instance = RunCreate.from_json(json)
# print the JSON string representation of the object
print(RunCreate.to_json())

# convert the object into a dict
run_create_dict = run_create_instance.to_dict()
# create an instance of RunCreate from a dict
run_create_from_dict = RunCreate.from_dict(run_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


