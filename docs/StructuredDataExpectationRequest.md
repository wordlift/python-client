# StructuredDataExpectationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**config** | [**StructuredDataExpectationConfigRequest**](StructuredDataExpectationConfigRequest.md) |  | 

## Example

```python
from wordlift_client.models.structured_data_expectation_request import StructuredDataExpectationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredDataExpectationRequest from a JSON string
structured_data_expectation_request_instance = StructuredDataExpectationRequest.from_json(json)
# print the JSON string representation of the object
print(StructuredDataExpectationRequest.to_json())

# convert the object into a dict
structured_data_expectation_request_dict = structured_data_expectation_request_instance.to_dict()
# create an instance of StructuredDataExpectationRequest from a dict
structured_data_expectation_request_from_dict = StructuredDataExpectationRequest.from_dict(structured_data_expectation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


