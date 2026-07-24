# QuestionAndAnswerSet

Generated Q&A content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_entity_gaps** | **List[str]** | Entity Gaps created for the Web Page. | [optional] 
**id** | **str** | The unique id. | [optional] [readonly] 
**is_smart_content_of** | **str** | The Web Page this smart content is created for. | [optional] 
**published** | **bool** | The published status of the smart content. | [optional] [readonly] 
**questions_and_answers** | [**List[QuestionAndAnswer]**](QuestionAndAnswer.md) | The generated questions and answers. | [optional] 
**selected_entity_gaps** | **List[str]** | Entity Gaps used to generate the Smart Content. | [optional] 
**smart_content_project_id** | **int** |  | [optional] 
**url** | **str** | The URL of the Web Page this smart content is created for. | [optional] 

## Example

```python
from wordlift_client.models.question_and_answer_set import QuestionAndAnswerSet

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionAndAnswerSet from a JSON string
question_and_answer_set_instance = QuestionAndAnswerSet.from_json(json)
# print the JSON string representation of the object
print(QuestionAndAnswerSet.to_json())

# convert the object into a dict
question_and_answer_set_dict = question_and_answer_set_instance.to_dict()
# create an instance of QuestionAndAnswerSet from a dict
question_and_answer_set_from_dict = QuestionAndAnswerSet.from_dict(question_and_answer_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


