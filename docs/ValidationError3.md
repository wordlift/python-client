# ValidationError3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[ValidationError3DetailInner]**](ValidationError3DetailInner.md) |  | [optional] 

## Example

```python
from wordlift_client.models.validation_error3 import ValidationError3

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError3 from a JSON string
validation_error3_instance = ValidationError3.from_json(json)
# print the JSON string representation of the object
print(ValidationError3.to_json())

# convert the object into a dict
validation_error3_dict = validation_error3_instance.to_dict()
# create an instance of ValidationError3 from a dict
validation_error3_from_dict = ValidationError3.from_dict(validation_error3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


