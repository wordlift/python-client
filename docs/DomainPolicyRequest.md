# DomainPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**js_render_mode** | [**DomainJsRenderMode**](DomainJsRenderMode.md) |  | [optional] 
**max_concurrency** | **int** |  | [optional] 
**refresh_interval_minutes** | **int** |  | [optional] 
**proxy_mode** | [**ProxyMode**](ProxyMode.md) |  | [optional] 

## Example

```python
from wordlift_client.models.domain_policy_request import DomainPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPolicyRequest from a JSON string
domain_policy_request_instance = DomainPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(DomainPolicyRequest.to_json())

# convert the object into a dict
domain_policy_request_dict = domain_policy_request_instance.to_dict()
# create an instance of DomainPolicyRequest from a dict
domain_policy_request_from_dict = DomainPolicyRequest.from_dict(domain_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


