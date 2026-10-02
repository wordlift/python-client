# AddPageResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from wordlift_client.models.add_page_resource_request import AddPageResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPageResourceRequest from a JSON string
add_page_resource_request_instance = AddPageResourceRequest.from_json(json)
# print the JSON string representation of the object
print(AddPageResourceRequest.to_json())

# convert the object into a dict
add_page_resource_request_dict = add_page_resource_request_instance.to_dict()
# create an instance of AddPageResourceRequest from a dict
add_page_resource_request_from_dict = AddPageResourceRequest.from_dict(add_page_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


