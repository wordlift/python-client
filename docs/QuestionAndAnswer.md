# QuestionAndAnswer

Generated Q&A content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** | The generated answer. | [optional] 
**created_at** | **datetime** | The create date-time. | [optional] [readonly] 
**entity_gaps** | **List[str]** |  | [optional] 
**errors** | [**List[ValidationResult]**](ValidationResult.md) | The set of errors found for the answer. | [optional] [readonly] 
**id** | **int** | The unique id. | [optional] [readonly] 
**iri** | **str** | The webpage IRI tied to this Q&amp;A. | 
**is_deleted** | **bool** | The deleted flag. | [optional] [default to False]
**is_published** | **bool** | The published flag. | [optional] [default to False]
**modified_at** | **datetime** | The last modified date-time. | [optional] [readonly] 
**question** | **str** | The generated question. | [optional] 
**smart_content_id** | **int** |  | [optional] 
**url** | **str** | The webpage URL tied to this Q&amp;A. | 
**warnings** | [**List[ValidationResult]**](ValidationResult.md) | The set of warnings found for the answer. | [optional] [readonly] 

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


