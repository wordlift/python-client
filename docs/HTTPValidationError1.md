# HTTPValidationError1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[ValidationError1]**](ValidationError1.md) |  | [optional] 

## Example

```python
from wordlift_client.models.http_validation_error1 import HTTPValidationError1

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPValidationError1 from a JSON string
http_validation_error1_instance = HTTPValidationError1.from_json(json)
# print the JSON string representation of the object
print(HTTPValidationError1.to_json())

# convert the object into a dict
http_validation_error1_dict = http_validation_error1_instance.to_dict()
# create an instance of HTTPValidationError1 from a dict
http_validation_error1_from_dict = HTTPValidationError1.from_dict(http_validation_error1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


