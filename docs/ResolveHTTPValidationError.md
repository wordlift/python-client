# ResolveHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[ResolveValidationError]**](ResolveValidationError.md) |  | [optional] 

## Example

```python
from wordlift_client.models.resolve_http_validation_error import ResolveHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveHTTPValidationError from a JSON string
resolve_http_validation_error_instance = ResolveHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(ResolveHTTPValidationError.to_json())

# convert the object into a dict
resolve_http_validation_error_dict = resolve_http_validation_error_instance.to_dict()
# create an instance of ResolveHTTPValidationError from a dict
resolve_http_validation_error_from_dict = ResolveHTTPValidationError.from_dict(resolve_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


