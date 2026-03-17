# JobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique job identifier. | 
**graph_id** | **str** | Public WordLift graph identifier. | 
**snapshot_date** | **str** | Logical KPI day targeted by the job. | 
**status** | **str** | Current job status. | 
**stage** | **str** | Current or last completed job stage. Cloned snapshots use &#x60;clone&#x60;. | 
**started_at** | **str** |  | [optional] 
**finished_at** | **str** |  | [optional] 
**heartbeat_at** | **str** |  | [optional] 
**documents_seen** | **int** |  | [optional] 
**documents_transformed** | **int** |  | [optional] 
**triple_rows_written** | **int** |  | [optional] 
**issues_written** | **int** |  | [optional] 
**retry_count** | **int** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**account_dataset_id** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**stage_timings_json** | **Dict[str, float]** |  | [optional] 
**runtime_profile_json** | **Dict[str, object]** |  | [optional] 

## Example

```python
from wordlift_client.models.job_response import JobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobResponse from a JSON string
job_response_instance = JobResponse.from_json(json)
# print the JSON string representation of the object
print(JobResponse.to_json())

# convert the object into a dict
job_response_dict = job_response_instance.to_dict()
# create an instance of JobResponse from a dict
job_response_from_dict = JobResponse.from_dict(job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


