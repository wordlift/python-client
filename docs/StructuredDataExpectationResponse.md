# StructuredDataExpectationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 
**created_at** | **datetime** |  | 
**type** | **str** |  | 
**config** | [**StructuredDataExpectationConfig**](StructuredDataExpectationConfig.md) |  | 

## Example

```python
from wordlift_client.models.structured_data_expectation_response import StructuredDataExpectationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredDataExpectationResponse from a JSON string
structured_data_expectation_response_instance = StructuredDataExpectationResponse.from_json(json)
# print the JSON string representation of the object
print(StructuredDataExpectationResponse.to_json())

# convert the object into a dict
structured_data_expectation_response_dict = structured_data_expectation_response_instance.to_dict()
# create an instance of StructuredDataExpectationResponse from a dict
structured_data_expectation_response_from_dict = StructuredDataExpectationResponse.from_dict(structured_data_expectation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


