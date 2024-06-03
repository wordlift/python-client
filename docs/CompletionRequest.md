# CompletionRequest

A request for a completion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency_penalty** | **float** |  | [optional] 
**logit_bias** | **Dict[str, int]** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**min_words** | **int** |  | [optional] 
**model_id** | **int** |  | [optional] 
**presence_penalty** | **float** |  | [optional] 
**prompt** | **str** |  | 
**stop** | **str** |  | [optional] 
**temperature** | **float** |  | [optional] 

## Example

```python
from wordlift_client.models.completion_request import CompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionRequest from a JSON string
completion_request_instance = CompletionRequest.from_json(json)
# print the JSON string representation of the object
print(CompletionRequest.to_json())

# convert the object into a dict
completion_request_dict = completion_request_instance.to_dict()
# create an instance of CompletionRequest from a dict
completion_request_from_dict = CompletionRequest.from_dict(completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


