# ValidationError2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[ValidationError2DetailInner]**](ValidationError2DetailInner.md) |  | [optional] 

## Example

```python
from wordlift_client.models.validation_error2 import ValidationError2

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError2 from a JSON string
validation_error2_instance = ValidationError2.from_json(json)
# print the JSON string representation of the object
print(ValidationError2.to_json())

# convert the object into a dict
validation_error2_dict = validation_error2_instance.to_dict()
# create an instance of ValidationError2 from a dict
validation_error2_from_dict = ValidationError2.from_dict(validation_error2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


