# TokenResponse

The tokens to access a service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token | [optional] [readonly] 
**access_token_expires_at** | **datetime** | The access token expiration | [optional] [readonly] 
**refresh_token** | **str** | The refresh token | [optional] [readonly] 

## Example

```python
from wordlift_client.models.token_response import TokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponse from a JSON string
token_response_instance = TokenResponse.from_json(json)
# print the JSON string representation of the object
print(TokenResponse.to_json())

# convert the object into a dict
token_response_dict = token_response_instance.to_dict()
# create an instance of TokenResponse from a dict
token_response_from_dict = TokenResponse.from_dict(token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


