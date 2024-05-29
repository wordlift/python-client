# BuildAuthorizeUriResponse

The response of the `buildAuthorizeUri` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorize_uri** | **str** | The Authorization URI. The Client should be redirected to this URI. | 

## Example

```python
from Wordlift_client.models.build_authorize_uri_response import BuildAuthorizeUriResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuildAuthorizeUriResponse from a JSON string
build_authorize_uri_response_instance = BuildAuthorizeUriResponse.from_json(json)
# print the JSON string representation of the object
print(BuildAuthorizeUriResponse.to_json())

# convert the object into a dict
build_authorize_uri_response_dict = build_authorize_uri_response_instance.to_dict()
# create an instance of BuildAuthorizeUriResponse from a dict
build_authorize_uri_response_from_dict = BuildAuthorizeUriResponse.from_dict(build_authorize_uri_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


