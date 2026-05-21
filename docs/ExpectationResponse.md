# ExpectationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**check_name** | [**MonitorCheckName**](MonitorCheckName.md) |  | 
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 
**config** | [**StructuredDataExpectationConfig**](StructuredDataExpectationConfig.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wordlift_client.models.expectation_response import ExpectationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectationResponse from a JSON string
expectation_response_instance = ExpectationResponse.from_json(json)
# print the JSON string representation of the object
print(ExpectationResponse.to_json())

# convert the object into a dict
expectation_response_dict = expectation_response_instance.to_dict()
# create an instance of ExpectationResponse from a dict
expectation_response_from_dict = ExpectationResponse.from_dict(expectation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


