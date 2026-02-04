# ValidationError2DetailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | **List[str]** |  | [optional] 
**msg** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.validation_error2_detail_inner import ValidationError2DetailInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError2DetailInner from a JSON string
validation_error2_detail_inner_instance = ValidationError2DetailInner.from_json(json)
# print the JSON string representation of the object
print(ValidationError2DetailInner.to_json())

# convert the object into a dict
validation_error2_detail_inner_dict = validation_error2_detail_inner_instance.to_dict()
# create an instance of ValidationError2DetailInner from a dict
validation_error2_detail_inner_from_dict = ValidationError2DetailInner.from_dict(validation_error2_detail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


