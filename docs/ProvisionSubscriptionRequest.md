# ProvisionSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | [optional] 
**sku** | **str** |  | 

## Example

```python
from wordlift_client.models.provision_subscription_request import ProvisionSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionSubscriptionRequest from a JSON string
provision_subscription_request_instance = ProvisionSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(ProvisionSubscriptionRequest.to_json())

# convert the object into a dict
provision_subscription_request_dict = provision_subscription_request_instance.to_dict()
# create an instance of ProvisionSubscriptionRequest from a dict
provision_subscription_request_from_dict = ProvisionSubscriptionRequest.from_dict(provision_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


