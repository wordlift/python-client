# DomainPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **str** |  | 
**js_render_mode** | [**DomainJsRenderMode**](DomainJsRenderMode.md) |  | 
**max_concurrency** | **int** |  | 
**refresh_interval_minutes** | **int** |  | 
**proxy_mode** | [**ProxyMode**](ProxyMode.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wordlift_client.models.domain_policy_response import DomainPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPolicyResponse from a JSON string
domain_policy_response_instance = DomainPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(DomainPolicyResponse.to_json())

# convert the object into a dict
domain_policy_response_dict = domain_policy_response_instance.to_dict()
# create an instance of DomainPolicyResponse from a dict
domain_policy_response_from_dict = DomainPolicyResponse.from_dict(domain_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


