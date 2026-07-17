# WebPageImportsValidationError


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
from wordlift_client.models.web_page_imports_validation_error import WebPageImportsValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageImportsValidationError from a JSON string
web_page_imports_validation_error_instance = WebPageImportsValidationError.from_json(json)
# print the JSON string representation of the object
print(WebPageImportsValidationError.to_json())

# convert the object into a dict
web_page_imports_validation_error_dict = web_page_imports_validation_error_instance.to_dict()
# create an instance of WebPageImportsValidationError from a dict
web_page_imports_validation_error_from_dict = WebPageImportsValidationError.from_dict(web_page_imports_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


