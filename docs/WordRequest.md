# WordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bias** | **int** | The bias. | 
**word** | **str** | The actual word. | 

## Example

```python
from wordlift-client.models.word_request import WordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordRequest from a JSON string
word_request_instance = WordRequest.from_json(json)
# print the JSON string representation of the object
print(WordRequest.to_json())

# convert the object into a dict
word_request_dict = word_request_instance.to_dict()
# create an instance of WordRequest from a dict
word_request_from_dict = WordRequest.from_dict(word_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


