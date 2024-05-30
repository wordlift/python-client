# ExchangeAuthCodeResponse

The response of the `buildAuthorizeUri` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token | [optional] 
**expires_in** | **int** | The number of seconds for the access token to expire | [optional] 
**refresh_token** | **str** | The refresh token | [optional] 
**scope** | **str** | The scope | [optional] 
**token_type** | **str** | The token type, usually Bearer | [optional] 

## Example

```python
from Wordlift_client.models.exchange_auth_code_response import ExchangeAuthCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeAuthCodeResponse from a JSON string
exchange_auth_code_response_instance = ExchangeAuthCodeResponse.from_json(json)
# print the JSON string representation of the object
print(ExchangeAuthCodeResponse.to_json())

# convert the object into a dict
exchange_auth_code_response_dict = exchange_auth_code_response_instance.to_dict()
# create an instance of ExchangeAuthCodeResponse from a dict
exchange_auth_code_response_from_dict = ExchangeAuthCodeResponse.from_dict(exchange_auth_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


