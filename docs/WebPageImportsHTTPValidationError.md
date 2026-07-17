# WebPageImportsHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[WebPageImportsValidationError]**](WebPageImportsValidationError.md) |  | [optional] 

## Example

```python
from wordlift_client.models.web_page_imports_http_validation_error import WebPageImportsHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageImportsHTTPValidationError from a JSON string
web_page_imports_http_validation_error_instance = WebPageImportsHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(WebPageImportsHTTPValidationError.to_json())

# convert the object into a dict
web_page_imports_http_validation_error_dict = web_page_imports_http_validation_error_instance.to_dict()
# create an instance of WebPageImportsHTTPValidationError from a dict
web_page_imports_http_validation_error_from_dict = WebPageImportsHTTPValidationError.from_dict(web_page_imports_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


