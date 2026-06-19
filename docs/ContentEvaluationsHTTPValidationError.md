# ContentEvaluationsHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[ContentEvaluationsValidationError]**](ContentEvaluationsValidationError.md) |  | [optional] 

## Example

```python
from wordlift_client.models.content_evaluations_http_validation_error import ContentEvaluationsHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationsHTTPValidationError from a JSON string
content_evaluations_http_validation_error_instance = ContentEvaluationsHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationsHTTPValidationError.to_json())

# convert the object into a dict
content_evaluations_http_validation_error_dict = content_evaluations_http_validation_error_instance.to_dict()
# create an instance of ContentEvaluationsHTTPValidationError from a dict
content_evaluations_http_validation_error_from_dict = ContentEvaluationsHTTPValidationError.from_dict(content_evaluations_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


