# ContentEvaluationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quality_score** | [**ContentEvaluationResponseQualityScore**](ContentEvaluationResponseQualityScore.md) |  | 
**metadata** | [**ContentEvaluationResponseMetadata**](ContentEvaluationResponseMetadata.md) |  | 

## Example

```python
from wordlift_client.models.content_evaluation_response import ContentEvaluationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationResponse from a JSON string
content_evaluation_response_instance = ContentEvaluationResponse.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationResponse.to_json())

# convert the object into a dict
content_evaluation_response_dict = content_evaluation_response_instance.to_dict()
# create an instance of ContentEvaluationResponse from a dict
content_evaluation_response_from_dict = ContentEvaluationResponse.from_dict(content_evaluation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


