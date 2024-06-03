# WordRepetitionData

Words in completion which are repeated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**repeated_in_same_sentence** | **bool** |  | [optional] 

## Example

```python
from wordlift-client.models.word_repetition_data import WordRepetitionData

# TODO update the JSON string below
json = "{}"
# create an instance of WordRepetitionData from a JSON string
word_repetition_data_instance = WordRepetitionData.from_json(json)
# print the JSON string representation of the object
print(WordRepetitionData.to_json())

# convert the object into a dict
word_repetition_data_dict = word_repetition_data_instance.to_dict()
# create an instance of WordRepetitionData from a dict
word_repetition_data_from_dict = WordRepetitionData.from_dict(word_repetition_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


