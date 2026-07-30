# BootstrapJobOutcome

The bootstrap judge's verdict on a COMPLETED job, whether accepted or rejected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**succeeded** | **bool** |  | 
**confidence** | **float** |  | [optional] 
**summary** | **str** |  | [optional] 
**blocking_issues** | **List[str]** |  | [optional] 
**narrative** | **str** |  | [optional] 
**token_usage** | **Dict[str, int]** |  | [optional] 

## Example

```python
from wordlift_client.models.bootstrap_job_outcome import BootstrapJobOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of BootstrapJobOutcome from a JSON string
bootstrap_job_outcome_instance = BootstrapJobOutcome.from_json(json)
# print the JSON string representation of the object
print(BootstrapJobOutcome.to_json())

# convert the object into a dict
bootstrap_job_outcome_dict = bootstrap_job_outcome_instance.to_dict()
# create an instance of BootstrapJobOutcome from a dict
bootstrap_job_outcome_from_dict = BootstrapJobOutcome.from_dict(bootstrap_job_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


