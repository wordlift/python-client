# AskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**model** | **str** |  | [optional] [default to 'gpt-4o']
**security** | **bool** |  | [optional] [default to False]

## Example

```python
from wordlift_client.models.ask_request import AskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AskRequest from a JSON string
ask_request_instance = AskRequest.from_json(json)
# print the JSON string representation of the object
print(AskRequest.to_json())

# convert the object into a dict
ask_request_dict = ask_request_instance.to_dict()
# create an instance of AskRequest from a dict
ask_request_from_dict = AskRequest.from_dict(ask_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


