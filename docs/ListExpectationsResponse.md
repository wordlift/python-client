# ListExpectationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpectationResponse]**](ExpectationResponse.md) |  | 
**total** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.list_expectations_response import ListExpectationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListExpectationsResponse from a JSON string
list_expectations_response_instance = ListExpectationsResponse.from_json(json)
# print the JSON string representation of the object
print(ListExpectationsResponse.to_json())

# convert the object into a dict
list_expectations_response_dict = list_expectations_response_instance.to_dict()
# create an instance of ListExpectationsResponse from a dict
list_expectations_response_from_dict = ListExpectationsResponse.from_dict(list_expectations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


