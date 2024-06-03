# BuildAuthorizeUriRequest

The request of the `buildAuthorizeUri` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri** | **str** | The Redirect URI to where redirect the Client after successful authentication. | 

## Example

```python
from wordlift-client.models.build_authorize_uri_request import BuildAuthorizeUriRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuildAuthorizeUriRequest from a JSON string
build_authorize_uri_request_instance = BuildAuthorizeUriRequest.from_json(json)
# print the JSON string representation of the object
print(BuildAuthorizeUriRequest.to_json())

# convert the object into a dict
build_authorize_uri_request_dict = build_authorize_uri_request_instance.to_dict()
# create an instance of BuildAuthorizeUriRequest from a dict
build_authorize_uri_request_from_dict = BuildAuthorizeUriRequest.from_dict(build_authorize_uri_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


