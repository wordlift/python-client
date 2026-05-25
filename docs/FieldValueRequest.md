# FieldValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 

## Example

```python
from wordlift_client.models.field_value_request import FieldValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FieldValueRequest from a JSON string
field_value_request_instance = FieldValueRequest.from_json(json)
# print the JSON string representation of the object
print(FieldValueRequest.to_json())

# convert the object into a dict
field_value_request_dict = field_value_request_instance.to_dict()
# create an instance of FieldValueRequest from a dict
field_value_request_from_dict = FieldValueRequest.from_dict(field_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


