# AccountSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**sku** | **str** |  | [optional] 

## Example

```python
from Wordlift_client.models.account_subscription import AccountSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSubscription from a JSON string
account_subscription_instance = AccountSubscription.from_json(json)
# print the JSON string representation of the object
print(AccountSubscription.to_json())

# convert the object into a dict
account_subscription_dict = account_subscription_instance.to_dict()
# create an instance of AccountSubscription from a dict
account_subscription_from_dict = AccountSubscription.from_dict(account_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


