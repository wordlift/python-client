# OAuth2ConnectorAuthorizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_issued_at** | **datetime** |  | [optional] 
**account_id** | **int** |  | [optional] 
**connector_id** | **str** |  | [optional] 
**refresh_token_issued_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.o_auth2_connector_authorization_response import OAuth2ConnectorAuthorizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ConnectorAuthorizationResponse from a JSON string
o_auth2_connector_authorization_response_instance = OAuth2ConnectorAuthorizationResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2ConnectorAuthorizationResponse.to_json())

# convert the object into a dict
o_auth2_connector_authorization_response_dict = o_auth2_connector_authorization_response_instance.to_dict()
# create an instance of OAuth2ConnectorAuthorizationResponse from a dict
o_auth2_connector_authorization_response_from_dict = OAuth2ConnectorAuthorizationResponse.from_dict(o_auth2_connector_authorization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


