# VectorSearchQuestionResponseItem

An array of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** |  | [optional] 
**question** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.vector_search_question_response_item import VectorSearchQuestionResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of VectorSearchQuestionResponseItem from a JSON string
vector_search_question_response_item_instance = VectorSearchQuestionResponseItem.from_json(json)
# print the JSON string representation of the object
print(VectorSearchQuestionResponseItem.to_json())

# convert the object into a dict
vector_search_question_response_item_dict = vector_search_question_response_item_instance.to_dict()
# create an instance of VectorSearchQuestionResponseItem from a dict
vector_search_question_response_item_from_dict = VectorSearchQuestionResponseItem.from_dict(vector_search_question_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


