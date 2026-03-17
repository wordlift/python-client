# SubmitJobBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_date** | **str** | Logical KPI day to calculate in &#x60;YYYY-MM-DD&#x60; format. | 
**force_rerun** | **bool** | If &#x60;true&#x60;, ignore the 24-hour freshness rule and replace a currently active job. | [optional] [default to False]
**stage_retries** | **int** | Number of retries allowed for each stage before the job fails. | [optional] [default to 1]
**limit_documents** | **int** |  | [optional] 
**limit_urls** | **int** |  | [optional] 
**skip_validation** | **bool** | If &#x60;true&#x60;, skip the SHACL/rich-snippet validation stage. | [optional] [default to False]
**replace_validation** | **bool** | If &#x60;true&#x60;, replace previously persisted validation output for the same graph/day. | [optional] [default to False]

## Example

```python
from wordlift_client.models.submit_job_body import SubmitJobBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitJobBody from a JSON string
submit_job_body_instance = SubmitJobBody.from_json(json)
# print the JSON string representation of the object
print(SubmitJobBody.to_json())

# convert the object into a dict
submit_job_body_dict = submit_job_body_instance.to_dict()
# create an instance of SubmitJobBody from a dict
submit_job_body_from_dict = SubmitJobBody.from_dict(submit_job_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


