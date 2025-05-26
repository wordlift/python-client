# Tokens

The tokens to access a service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token | [optional] [readonly] 
**refresh_token** | **str** | The refresh token | [optional] [readonly] 

## Example

```python
from wordlift_client.models.tokens import Tokens

# TODO update the JSON string below
json = "{}"
# create an instance of Tokens from a JSON string
tokens_instance = Tokens.from_json(json)
# print the JSON string representation of the object
print(Tokens.to_json())

# convert the object into a dict
tokens_dict = tokens_instance.to_dict()
# create an instance of Tokens from a dict
tokens_from_dict = Tokens.from_dict(tokens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


