# Word

A Word bias.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bias** | **int** | The bias. | 
**cluster** | **str** | The cluster of the word. | 
**content_generation_id** | **int** | The content generation id. | [readonly] 
**created_at** | **datetime** | The create date-time. | [optional] [readonly] 
**id** | **int** | The unique id. | [optional] [readonly] 
**modified_at** | **datetime** | The last modified date-time. | [optional] [readonly] 
**token_id** | **str** | The token id for the word. | 
**word** | **str** | The actual word. | 

## Example

```python
from wordlift-client.models.word import Word

# TODO update the JSON string below
json = "{}"
# create an instance of Word from a JSON string
word_instance = Word.from_json(json)
# print the JSON string representation of the object
print(Word.to_json())

# convert the object into a dict
word_dict = word_instance.to_dict()
# create an instance of Word from a dict
word_from_dict = Word.from_dict(word_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


