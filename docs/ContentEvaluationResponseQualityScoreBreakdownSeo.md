# ContentEvaluationResponseQualityScoreBreakdownSeo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_density** | **Dict[str, float]** | Object with keyword percentages when keywords are provided | 
**top_entities** | **Dict[str, List[ContentEvaluationResponseQualityScoreBreakdownSeoTopEntitiesValueInner]]** |  | 
**score** | **int** |  | 

## Example

```python
from wordlift_client.models.content_evaluation_response_quality_score_breakdown_seo import ContentEvaluationResponseQualityScoreBreakdownSeo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationResponseQualityScoreBreakdownSeo from a JSON string
content_evaluation_response_quality_score_breakdown_seo_instance = ContentEvaluationResponseQualityScoreBreakdownSeo.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationResponseQualityScoreBreakdownSeo.to_json())

# convert the object into a dict
content_evaluation_response_quality_score_breakdown_seo_dict = content_evaluation_response_quality_score_breakdown_seo_instance.to_dict()
# create an instance of ContentEvaluationResponseQualityScoreBreakdownSeo from a dict
content_evaluation_response_quality_score_breakdown_seo_from_dict = ContentEvaluationResponseQualityScoreBreakdownSeo.from_dict(content_evaluation_response_quality_score_breakdown_seo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


