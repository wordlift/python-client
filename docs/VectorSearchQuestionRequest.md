# VectorSearchQuestionRequest

One or more questions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The desired language of the answer. | [optional] 
**questions** | **List[str]** | The list of questions. | 

## Example

```python
from wordlift_client.models.vector_search_question_request import VectorSearchQuestionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VectorSearchQuestionRequest from a JSON string
vector_search_question_request_instance = VectorSearchQuestionRequest.from_json(json)
# print the JSON string representation of the object
print(VectorSearchQuestionRequest.to_json())

# convert the object into a dict
vector_search_question_request_dict = vector_search_question_request_instance.to_dict()
# create an instance of VectorSearchQuestionRequest from a dict
vector_search_question_request_from_dict = VectorSearchQuestionRequest.from_dict(vector_search_question_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


