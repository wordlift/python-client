# EntityPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The patch operation, example &#x60;add&#x60;. | [optional] 
**path** | **str** | The property to apply the operation, JSONPath formatted (leading slash) on, e.g. &#x60;/https://schema.org/image (note the leading slash). | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.entity_patch_request import EntityPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntityPatchRequest from a JSON string
entity_patch_request_instance = EntityPatchRequest.from_json(json)
# print the JSON string representation of the object
print(EntityPatchRequest.to_json())

# convert the object into a dict
entity_patch_request_dict = entity_patch_request_instance.to_dict()
# create an instance of EntityPatchRequest from a dict
entity_patch_request_from_dict = EntityPatchRequest.from_dict(entity_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


