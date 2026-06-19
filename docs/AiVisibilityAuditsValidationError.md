# AiVisibilityAuditsValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[LocationInner]**](LocationInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from wordlift_client.models.ai_visibility_audits_validation_error import AiVisibilityAuditsValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AiVisibilityAuditsValidationError from a JSON string
ai_visibility_audits_validation_error_instance = AiVisibilityAuditsValidationError.from_json(json)
# print the JSON string representation of the object
print(AiVisibilityAuditsValidationError.to_json())

# convert the object into a dict
ai_visibility_audits_validation_error_dict = ai_visibility_audits_validation_error_instance.to_dict()
# create an instance of AiVisibilityAuditsValidationError from a dict
ai_visibility_audits_validation_error_from_dict = AiVisibilityAuditsValidationError.from_dict(ai_visibility_audits_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


