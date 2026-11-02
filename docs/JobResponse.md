# JobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique job identifier. | 
**graph_id** | **str** | Public WordLift graph identifier. | 
**snapshot_date** | **str** | Logical KPI day targeted by the job. | 
**status** | **str** | Current job status. | 
**stage** | **str** | Current or last completed job stage. Cloned snapshots use &#x60;clone&#x60;. | 
**started_at** | **str** | Timestamp when the job started. | [optional] 
**finished_at** | **str** | Timestamp when the job finished, if complete. | [optional] 
**heartbeat_at** | **str** | Last heartbeat timestamp emitted by the worker. | [optional] 
**documents_seen** | **int** | Number of source documents scanned so far. | [optional] 
**documents_transformed** | **int** | Number of source documents transformed so far. | [optional] 
**triple_rows_written** | **int** | Number of helper/assertion rows materialized so far. | [optional] 
**issues_written** | **int** | Number of validation issue rows persisted so far. | [optional] 
**retry_count** | **int** | How many stage retries were used. | [optional] 
**error_code** | **str** | Machine-readable failure code, if any. | [optional] 
**error_message** | **str** | Human-readable failure message, if any. | [optional] 
**account_dataset_id** | **str** | Resolved internal dataset identifier used for Mongo access. | [optional] 
**website_url** | **str** | Configured website URL resolved for the graph. | [optional] 
**stage_timings_json** | **Dict[str, float]** | Per-stage elapsed time in seconds. | [optional] 
**runtime_profile_json** | **Dict[str, object]** | Structured calculate-stage runtime profile including fetch/analyze/flush timings and Mongo batch latency stats. | [optional] 

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


