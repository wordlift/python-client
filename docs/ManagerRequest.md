# ManagerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeem_code** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.manager_request import ManagerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagerRequest from a JSON string
manager_request_instance = ManagerRequest.from_json(json)
# print the JSON string representation of the object
print(ManagerRequest.to_json())

# convert the object into a dict
manager_request_dict = manager_request_instance.to_dict()
# create an instance of ManagerRequest from a dict
manager_request_from_dict = ManagerRequest.from_dict(manager_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


