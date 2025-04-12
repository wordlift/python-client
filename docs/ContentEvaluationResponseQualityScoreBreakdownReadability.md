# ContentEvaluationResponseQualityScoreBreakdownReadability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** |  | 
**grade_level** | **int** |  | 
**complex_sentences** | [**ContentEvaluationResponseQualityScoreBreakdownReadabilityComplexSentences**](ContentEvaluationResponseQualityScoreBreakdownReadabilityComplexSentences.md) |  | 

## Example

```python
from wordlift_client.models.content_evaluation_response_quality_score_breakdown_readability import ContentEvaluationResponseQualityScoreBreakdownReadability

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationResponseQualityScoreBreakdownReadability from a JSON string
content_evaluation_response_quality_score_breakdown_readability_instance = ContentEvaluationResponseQualityScoreBreakdownReadability.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationResponseQualityScoreBreakdownReadability.to_json())

# convert the object into a dict
content_evaluation_response_quality_score_breakdown_readability_dict = content_evaluation_response_quality_score_breakdown_readability_instance.to_dict()
# create an instance of ContentEvaluationResponseQualityScoreBreakdownReadability from a dict
content_evaluation_response_quality_score_breakdown_readability_from_dict = ContentEvaluationResponseQualityScoreBreakdownReadability.from_dict(content_evaluation_response_quality_score_breakdown_readability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


