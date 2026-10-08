# ResolveValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[LocationInner]**](LocationInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 
**input** | **object** |  | [optional] 
**ctx** | **object** |  | [optional] 

## Example

```python
from wordlift_client.models.resolve_validation_error import ResolveValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveValidationError from a JSON string
resolve_validation_error_instance = ResolveValidationError.from_json(json)
# print the JSON string representation of the object
print(ResolveValidationError.to_json())

# convert the object into a dict
resolve_validation_error_dict = resolve_validation_error_instance.to_dict()
# create an instance of ResolveValidationError from a dict
resolve_validation_error_from_dict = ResolveValidationError.from_dict(resolve_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


