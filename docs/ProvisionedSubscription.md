# ProvisionedSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**ends_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**wordlift_key** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.provisioned_subscription import ProvisionedSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionedSubscription from a JSON string
provisioned_subscription_instance = ProvisionedSubscription.from_json(json)
# print the JSON string representation of the object
print(ProvisionedSubscription.to_json())

# convert the object into a dict
provisioned_subscription_dict = provisioned_subscription_instance.to_dict()
# create an instance of ProvisionedSubscription from a dict
provisioned_subscription_from_dict = ProvisionedSubscription.from_dict(provisioned_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


