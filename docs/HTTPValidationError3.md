# HTTPValidationError3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[ValidationError4]**](ValidationError4.md) |  | [optional] 

## Example

```python
from wordlift_client.models.http_validation_error3 import HTTPValidationError3

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPValidationError3 from a JSON string
http_validation_error3_instance = HTTPValidationError3.from_json(json)
# print the JSON string representation of the object
print(HTTPValidationError3.to_json())

# convert the object into a dict
http_validation_error3_dict = http_validation_error3_instance.to_dict()
# create an instance of HTTPValidationError3 from a dict
http_validation_error3_from_dict = HTTPValidationError3.from_dict(http_validation_error3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


