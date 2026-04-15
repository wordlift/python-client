# AddResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**type** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.add_resource_request import AddResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddResourceRequest from a JSON string
add_resource_request_instance = AddResourceRequest.from_json(json)
# print the JSON string representation of the object
print(AddResourceRequest.to_json())

# convert the object into a dict
add_resource_request_dict = add_resource_request_instance.to_dict()
# create an instance of AddResourceRequest from a dict
add_resource_request_from_dict = AddResourceRequest.from_dict(add_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


