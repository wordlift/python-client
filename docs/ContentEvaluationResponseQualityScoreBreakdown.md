# ContentEvaluationResponseQualityScoreBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**ContentEvaluationResponseQualityScoreBreakdownContent**](ContentEvaluationResponseQualityScoreBreakdownContent.md) |  | 
**readability** | [**ContentEvaluationResponseQualityScoreBreakdownReadability**](ContentEvaluationResponseQualityScoreBreakdownReadability.md) |  | 
**seo** | [**ContentEvaluationResponseQualityScoreBreakdownSeo**](ContentEvaluationResponseQualityScoreBreakdownSeo.md) |  | 

## Example

```python
from wordlift_client.models.content_evaluation_response_quality_score_breakdown import ContentEvaluationResponseQualityScoreBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationResponseQualityScoreBreakdown from a JSON string
content_evaluation_response_quality_score_breakdown_instance = ContentEvaluationResponseQualityScoreBreakdown.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationResponseQualityScoreBreakdown.to_json())

# convert the object into a dict
content_evaluation_response_quality_score_breakdown_dict = content_evaluation_response_quality_score_breakdown_instance.to_dict()
# create an instance of ContentEvaluationResponseQualityScoreBreakdown from a dict
content_evaluation_response_quality_score_breakdown_from_dict = ContentEvaluationResponseQualityScoreBreakdown.from_dict(content_evaluation_response_quality_score_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


