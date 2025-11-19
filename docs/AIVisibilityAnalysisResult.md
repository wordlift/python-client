# AIVisibilityAnalysisResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**num_queries_requested** | **int** |  | 
**coverage_threshold** | **float** |  | 
**entity_name** | **str** |  | 
**query_reasoning** | **str** |  | 
**covered_count** | **int** |  | 
**total_queries** | **int** |  | 
**query_details** | [**List[QueryCoverage]**](QueryCoverage.md) |  | 
**content_chunks_count** | **int** |  | 
**coverage_score** | **float** |  | [readonly] 

## Example

```python
from wordlift_client.models.ai_visibility_analysis_result import AIVisibilityAnalysisResult

# TODO update the JSON string below
json = "{}"
# create an instance of AIVisibilityAnalysisResult from a JSON string
ai_visibility_analysis_result_instance = AIVisibilityAnalysisResult.from_json(json)
# print the JSON string representation of the object
print(AIVisibilityAnalysisResult.to_json())

# convert the object into a dict
ai_visibility_analysis_result_dict = ai_visibility_analysis_result_instance.to_dict()
# create an instance of AIVisibilityAnalysisResult from a dict
ai_visibility_analysis_result_from_dict = AIVisibilityAnalysisResult.from_dict(ai_visibility_analysis_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


