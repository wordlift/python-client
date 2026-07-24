# QuestionAndAnswer

Generated Q&A content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_answer** | [**AcceptedAnswer**](AcceptedAnswer.md) |  | [optional] 
**answer** | **str** | The generated answer. | [optional] 
**errors** | [**List[ValidationResult]**](ValidationResult.md) | The set of errors found for the answer. | [readonly] 
**id** | **str** | The unique id. | [optional] [readonly] 
**question** | **str** | The generated question. | [optional] 
**warnings** | [**List[ValidationResult]**](ValidationResult.md) | The set of warnings found for the answer. | [readonly] 

## Example

```python
from wordlift_client.models.question_and_answer import QuestionAndAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionAndAnswer from a JSON string
question_and_answer_instance = QuestionAndAnswer.from_json(json)
# print the JSON string representation of the object
print(QuestionAndAnswer.to_json())

# convert the object into a dict
question_and_answer_dict = question_and_answer_instance.to_dict()
# create an instance of QuestionAndAnswer from a dict
question_and_answer_from_dict = QuestionAndAnswer.from_dict(question_and_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


