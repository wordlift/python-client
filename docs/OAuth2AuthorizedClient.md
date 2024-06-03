# OAuth2AuthorizedClient

A OAuth2 Authorized Client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_expires_at** | **datetime** |  | [optional] 
**access_token_issued_at** | **datetime** |  | [optional] 
**access_token_scopes** | **str** |  | [optional] 
**access_token_type** | **str** |  | [optional] 
**access_token_value** | **str** |  | [optional] 
**client_registration_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**principal_name** | **str** |  | [optional] 
**refresh_token_issued_at** | **datetime** |  | [optional] 
**refresh_token_value** | **str** |  | [optional] 

## Example

```python
from wordlift-client.models.o_auth2_authorized_client import OAuth2AuthorizedClient

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2AuthorizedClient from a JSON string
o_auth2_authorized_client_instance = OAuth2AuthorizedClient.from_json(json)
# print the JSON string representation of the object
print(OAuth2AuthorizedClient.to_json())

# convert the object into a dict
o_auth2_authorized_client_dict = o_auth2_authorized_client_instance.to_dict()
# create an instance of OAuth2AuthorizedClient from a dict
o_auth2_authorized_client_from_dict = OAuth2AuthorizedClient.from_dict(o_auth2_authorized_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


