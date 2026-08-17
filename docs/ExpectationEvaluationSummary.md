# ExpectationEvaluationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expectation_id** | **str** |  | 
**status** | [**ExpectationOutcome**](ExpectationOutcome.md) |  | 
**evaluated_at** | **datetime** |  | 
**segments_membership** | [**List[SegmentSeverityResponse]**](SegmentSeverityResponse.md) |  | 

## Example

```python
from wordlift_client.models.expectation_evaluation_summary import ExpectationEvaluationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectationEvaluationSummary from a JSON string
expectation_evaluation_summary_instance = ExpectationEvaluationSummary.from_json(json)
# print the JSON string representation of the object
print(ExpectationEvaluationSummary.to_json())

# convert the object into a dict
expectation_evaluation_summary_dict = expectation_evaluation_summary_instance.to_dict()
# create an instance of ExpectationEvaluationSummary from a dict
expectation_evaluation_summary_from_dict = ExpectationEvaluationSummary.from_dict(expectation_evaluation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


