# HTTPValidationError2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[ValidationError2]**](ValidationError2.md) |  | [optional] 

## Example

```python
from wordlift_client.models.http_validation_error2 import HTTPValidationError2

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPValidationError2 from a JSON string
http_validation_error2_instance = HTTPValidationError2.from_json(json)
# print the JSON string representation of the object
print(HTTPValidationError2.to_json())

# convert the object into a dict
http_validation_error2_dict = http_validation_error2_instance.to_dict()
# create an instance of HTTPValidationError2 from a dict
http_validation_error2_from_dict = HTTPValidationError2.from_dict(http_validation_error2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


