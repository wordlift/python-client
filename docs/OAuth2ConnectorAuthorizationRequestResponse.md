# OAuth2ConnectorAuthorizationRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.o_auth2_connector_authorization_request_response import OAuth2ConnectorAuthorizationRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ConnectorAuthorizationRequestResponse from a JSON string
o_auth2_connector_authorization_request_response_instance = OAuth2ConnectorAuthorizationRequestResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2ConnectorAuthorizationRequestResponse.to_json())

# convert the object into a dict
o_auth2_connector_authorization_request_response_dict = o_auth2_connector_authorization_request_response_instance.to_dict()
# create an instance of OAuth2ConnectorAuthorizationRequestResponse from a dict
o_auth2_connector_authorization_request_response_from_dict = OAuth2ConnectorAuthorizationRequestResponse.from_dict(o_auth2_connector_authorization_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


