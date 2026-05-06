# ValidationError4


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
from wordlift_client.models.validation_error4 import ValidationError4

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError4 from a JSON string
validation_error4_instance = ValidationError4.from_json(json)
# print the JSON string representation of the object
print(ValidationError4.to_json())

# convert the object into a dict
validation_error4_dict = validation_error4_instance.to_dict()
# create an instance of ValidationError4 from a dict
validation_error4_from_dict = ValidationError4.from_dict(validation_error4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


