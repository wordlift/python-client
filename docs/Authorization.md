# Authorization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_issued_at** | **datetime** | When the access token was issued | [readonly] 
**account** | **str** | Account key | [readonly] 
**refresh_token_issued_at** | **datetime** | When the refresh token was issued | [optional] [readonly] 
**status** | [**AuthorizationStatus**](AuthorizationStatus.md) |  | 

## Example

```python
from wordlift_client.models.authorization import Authorization

# TODO update the JSON string below
json = "{}"
# create an instance of Authorization from a JSON string
authorization_instance = Authorization.from_json(json)
# print the JSON string representation of the object
print(Authorization.to_json())

# convert the object into a dict
authorization_dict = authorization_instance.to_dict()
# create an instance of Authorization from a dict
authorization_from_dict = Authorization.from_dict(authorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


