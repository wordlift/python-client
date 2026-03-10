# ResetAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keep_country** | **bool** |  | [optional] 
**keep_language** | **bool** |  | [optional] 
**keep_url** | **bool** |  | [optional] 

## Example

```python
from wordlift_client.models.reset_account_request import ResetAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResetAccountRequest from a JSON string
reset_account_request_instance = ResetAccountRequest.from_json(json)
# print the JSON string representation of the object
print(ResetAccountRequest.to_json())

# convert the object into a dict
reset_account_request_dict = reset_account_request_instance.to_dict()
# create an instance of ResetAccountRequest from a dict
reset_account_request_from_dict = ResetAccountRequest.from_dict(reset_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


