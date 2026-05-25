# OAuth2ConnectorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**registration_id** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from wordlift_client.models.o_auth2_connector_response import OAuth2ConnectorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ConnectorResponse from a JSON string
o_auth2_connector_response_instance = OAuth2ConnectorResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2ConnectorResponse.to_json())

# convert the object into a dict
o_auth2_connector_response_dict = o_auth2_connector_response_instance.to_dict()
# create an instance of OAuth2ConnectorResponse from a dict
o_auth2_connector_response_from_dict = OAuth2ConnectorResponse.from_dict(o_auth2_connector_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


