# ContentEvaluationResponseMetadataPerformance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automated_metrics** | **float** |  | 
**keyword_analysis** | **float** |  | 
**llm_evaluation** | **float** |  | 
**combine_metrics** | **int** |  | 
**quality_score** | **int** |  | 

## Example

```python
from wordlift_client.models.content_evaluation_response_metadata_performance import ContentEvaluationResponseMetadataPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationResponseMetadataPerformance from a JSON string
content_evaluation_response_metadata_performance_instance = ContentEvaluationResponseMetadataPerformance.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationResponseMetadataPerformance.to_json())

# convert the object into a dict
content_evaluation_response_metadata_performance_dict = content_evaluation_response_metadata_performance_instance.to_dict()
# create an instance of ContentEvaluationResponseMetadataPerformance from a dict
content_evaluation_response_metadata_performance_from_dict = ContentEvaluationResponseMetadataPerformance.from_dict(content_evaluation_response_metadata_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


