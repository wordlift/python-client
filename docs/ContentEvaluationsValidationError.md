# ContentEvaluationsValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[LocationInner]**](LocationInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from wordlift_client.models.content_evaluations_validation_error import ContentEvaluationsValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationsValidationError from a JSON string
content_evaluations_validation_error_instance = ContentEvaluationsValidationError.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationsValidationError.to_json())

# convert the object into a dict
content_evaluations_validation_error_dict = content_evaluations_validation_error_instance.to_dict()
# create an instance of ContentEvaluationsValidationError from a dict
content_evaluations_validation_error_from_dict = ContentEvaluationsValidationError.from_dict(content_evaluations_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


