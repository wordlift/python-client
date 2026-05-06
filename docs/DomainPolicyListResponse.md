# DomainPolicyListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DomainPolicyResponse]**](DomainPolicyResponse.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from wordlift_client.models.domain_policy_list_response import DomainPolicyListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPolicyListResponse from a JSON string
domain_policy_list_response_instance = DomainPolicyListResponse.from_json(json)
# print the JSON string representation of the object
print(DomainPolicyListResponse.to_json())

# convert the object into a dict
domain_policy_list_response_dict = domain_policy_list_response_instance.to_dict()
# create an instance of DomainPolicyListResponse from a dict
domain_policy_list_response_from_dict = DomainPolicyListResponse.from_dict(domain_policy_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


