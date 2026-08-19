# StructuredDataExpectationConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** |  | 
**property_path** | **str** |  | [optional] 
**constraint** | [**StructuredDataConstraint**](StructuredDataConstraint.md) |  | 

## Example

```python
from wordlift_client.models.structured_data_expectation_config_request import StructuredDataExpectationConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredDataExpectationConfigRequest from a JSON string
structured_data_expectation_config_request_instance = StructuredDataExpectationConfigRequest.from_json(json)
# print the JSON string representation of the object
print(StructuredDataExpectationConfigRequest.to_json())

# convert the object into a dict
structured_data_expectation_config_request_dict = structured_data_expectation_config_request_instance.to_dict()
# create an instance of StructuredDataExpectationConfigRequest from a dict
structured_data_expectation_config_request_from_dict = StructuredDataExpectationConfigRequest.from_dict(structured_data_expectation_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


