# ListExpectationSeverityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpectationSeverityResponse]**](ExpectationSeverityResponse.md) |  | 
**total** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.list_expectation_severity_response import ListExpectationSeverityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListExpectationSeverityResponse from a JSON string
list_expectation_severity_response_instance = ListExpectationSeverityResponse.from_json(json)
# print the JSON string representation of the object
print(ListExpectationSeverityResponse.to_json())

# convert the object into a dict
list_expectation_severity_response_dict = list_expectation_severity_response_instance.to_dict()
# create an instance of ListExpectationSeverityResponse from a dict
list_expectation_severity_response_from_dict = ListExpectationSeverityResponse.from_dict(list_expectation_severity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


