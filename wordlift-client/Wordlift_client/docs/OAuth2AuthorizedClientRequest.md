# OAuth2AuthorizedClientRequest

The OAuth2 Authorized Client request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_expires_at** | **datetime** | When the Access Token expires | [optional] 
**access_token_issued_at** | **datetime** | When the Access Token was issued | [optional] 
**access_token_scopes** | **str** | The Access Token scopes | [optional] 
**access_token_type** | **str** | The Access Token Type | [optional] 
**access_token_value** | **str** | The Access Token Value | [optional] 
**client_registration_id** | **str** | The Client Registration Id | [optional] 
**principal_name** | **str** | The Principal Name | [optional] 
**refresh_token_issued_at** | **datetime** | When the Access Token was issued | [optional] 
**refresh_token_value** | **str** | The Refresh Token Value | [optional] 

## Example

```python
from Wordlift_client.models.o_auth2_authorized_client_request import OAuth2AuthorizedClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2AuthorizedClientRequest from a JSON string
o_auth2_authorized_client_request_instance = OAuth2AuthorizedClientRequest.from_json(json)
# print the JSON string representation of the object
print(OAuth2AuthorizedClientRequest.to_json())

# convert the object into a dict
o_auth2_authorized_client_request_dict = o_auth2_authorized_client_request_instance.to_dict()
# create an instance of OAuth2AuthorizedClientRequest from a dict
o_auth2_authorized_client_request_from_dict = OAuth2AuthorizedClientRequest.from_dict(o_auth2_authorized_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


