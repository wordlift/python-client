# DuplicateAuthorizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account_key** | **str** |  | 
**to_account_keys** | **List[str]** |  | 

## Example

```python
from wordlift_client.models.duplicate_authorization_request import DuplicateAuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateAuthorizationRequest from a JSON string
duplicate_authorization_request_instance = DuplicateAuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print(DuplicateAuthorizationRequest.to_json())

# convert the object into a dict
duplicate_authorization_request_dict = duplicate_authorization_request_instance.to_dict()
# create an instance of DuplicateAuthorizationRequest from a dict
duplicate_authorization_request_from_dict = DuplicateAuthorizationRequest.from_dict(duplicate_authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


