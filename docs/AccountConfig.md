# AccountConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **int** |  | [optional] 
**site_url** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.account_config import AccountConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AccountConfig from a JSON string
account_config_instance = AccountConfig.from_json(json)
# print the JSON string representation of the object
print(AccountConfig.to_json())

# convert the object into a dict
account_config_dict = account_config_instance.to_dict()
# create an instance of AccountConfig from a dict
account_config_from_dict = AccountConfig.from_dict(account_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


