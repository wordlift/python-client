# ContentEvaluationResponseQualityScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall** | **float** | The overall quality score. | 
**breakdown** | [**ContentEvaluationResponseQualityScoreBreakdown**](ContentEvaluationResponseQualityScoreBreakdown.md) |  | 

## Example

```python
from wordlift_client.models.content_evaluation_response_quality_score import ContentEvaluationResponseQualityScore

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationResponseQualityScore from a JSON string
content_evaluation_response_quality_score_instance = ContentEvaluationResponseQualityScore.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationResponseQualityScore.to_json())

# convert the object into a dict
content_evaluation_response_quality_score_dict = content_evaluation_response_quality_score_instance.to_dict()
# create an instance of ContentEvaluationResponseQualityScore from a dict
content_evaluation_response_quality_score_from_dict = ContentEvaluationResponseQualityScore.from_dict(content_evaluation_response_quality_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


