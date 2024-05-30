# QuestionAndAnswerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smart_content_id** | **int** |  | [optional] 
**webpage_properties** | [**WebpageProperties**](WebpageProperties.md) |  | [optional] 

## Example

```python
from Wordlift_client.models.question_and_answer_request import QuestionAndAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionAndAnswerRequest from a JSON string
question_and_answer_request_instance = QuestionAndAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(QuestionAndAnswerRequest.to_json())

# convert the object into a dict
question_and_answer_request_dict = question_and_answer_request_instance.to_dict()
# create an instance of QuestionAndAnswerRequest from a dict
question_and_answer_request_from_dict = QuestionAndAnswerRequest.from_dict(question_and_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


