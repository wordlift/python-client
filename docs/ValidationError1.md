# ValidationError1


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
from wordlift_client.models.validation_error1 import ValidationError1

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError1 from a JSON string
validation_error1_instance = ValidationError1.from_json(json)
# print the JSON string representation of the object
print(ValidationError1.to_json())

# convert the object into a dict
validation_error1_dict = validation_error1_instance.to_dict()
# create an instance of ValidationError1 from a dict
validation_error1_from_dict = ValidationError1.from_dict(validation_error1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


