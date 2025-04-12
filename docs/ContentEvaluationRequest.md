# ContentEvaluationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text content to be evaluated. | 
**keywords** | **List[str]** | List of keywords to analyze within the text content. | [optional] 

## Example

```python
from wordlift_client.models.content_evaluation_request import ContentEvaluationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationRequest from a JSON string
content_evaluation_request_instance = ContentEvaluationRequest.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationRequest.to_json())

# convert the object into a dict
content_evaluation_request_dict = content_evaluation_request_instance.to_dict()
# create an instance of ContentEvaluationRequest from a dict
content_evaluation_request_from_dict = ContentEvaluationRequest.from_dict(content_evaluation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


