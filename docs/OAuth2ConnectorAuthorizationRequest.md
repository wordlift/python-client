# OAuth2ConnectorAuthorizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri** | **str** |  | 
**state_id** | **str** |  | 

## Example

```python
from wordlift_client.models.o_auth2_connector_authorization_request import OAuth2ConnectorAuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ConnectorAuthorizationRequest from a JSON string
o_auth2_connector_authorization_request_instance = OAuth2ConnectorAuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print(OAuth2ConnectorAuthorizationRequest.to_json())

# convert the object into a dict
o_auth2_connector_authorization_request_dict = o_auth2_connector_authorization_request_instance.to_dict()
# create an instance of OAuth2ConnectorAuthorizationRequest from a dict
o_auth2_connector_authorization_request_from_dict = OAuth2ConnectorAuthorizationRequest.from_dict(o_auth2_connector_authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


