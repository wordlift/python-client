# BootstrapJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**account_id** | **str** |  | 
**account_url** | **str** |  | 
**repository_name** | **str** |  | 
**project_url** | **str** |  | 
**profile_name** | **str** |  | 
**status** | [**BootstrapJobStatus**](BootstrapJobStatus.md) |  | 
**attempt_number** | **int** |  | 
**root_job_id** | **str** |  | 
**last_heartbeat** | **datetime** |  | 
**cancellation_reason** | [**CancellationReason**](CancellationReason.md) |  | 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | 
**outcome** | **Dict[str, object]** |  | 
**created_at** | **datetime** |  | 
**started_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**worai_version** | **str** |  | 
**codex_version** | **str** |  | 
**bootstrap_md_hash** | **str** |  | 
**service_version** | **str** |  | 

## Example

```python
from wordlift_client.models.bootstrap_job_response import BootstrapJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BootstrapJobResponse from a JSON string
bootstrap_job_response_instance = BootstrapJobResponse.from_json(json)
# print the JSON string representation of the object
print(BootstrapJobResponse.to_json())

# convert the object into a dict
bootstrap_job_response_dict = bootstrap_job_response_instance.to_dict()
# create an instance of BootstrapJobResponse from a dict
bootstrap_job_response_from_dict = BootstrapJobResponse.from_dict(bootstrap_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


