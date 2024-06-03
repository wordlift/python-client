# UpdateQuestionAndAnswerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** |  | [optional] 
**question** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.update_question_and_answer_request import UpdateQuestionAndAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuestionAndAnswerRequest from a JSON string
update_question_and_answer_request_instance = UpdateQuestionAndAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateQuestionAndAnswerRequest.to_json())

# convert the object into a dict
update_question_and_answer_request_dict = update_question_and_answer_request_instance.to_dict()
# create an instance of UpdateQuestionAndAnswerRequest from a dict
update_question_and_answer_request_from_dict = UpdateQuestionAndAnswerRequest.from_dict(update_question_and_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


