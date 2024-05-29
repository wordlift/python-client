# ValidationFix

The list of fixes to apply when the rule validation fails.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ValidationTypeEnum**](ValidationTypeEnum.md) |  | [optional] 
**what** | **str** |  | [optional] 
**var_with** | **str** |  | [optional] 

## Example

```python
from Wordlift_client.models.validation_fix import ValidationFix

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationFix from a JSON string
validation_fix_instance = ValidationFix.from_json(json)
# print the JSON string representation of the object
print(ValidationFix.to_json())

# convert the object into a dict
validation_fix_dict = validation_fix_instance.to_dict()
# create an instance of ValidationFix from a dict
validation_fix_from_dict = ValidationFix.from_dict(validation_fix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


