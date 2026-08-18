# ListExpectationSummaryByTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpectationSummaryByTypeItem]**](ExpectationSummaryByTypeItem.md) |  | 
**total** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.list_expectation_summary_by_type_response import ListExpectationSummaryByTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListExpectationSummaryByTypeResponse from a JSON string
list_expectation_summary_by_type_response_instance = ListExpectationSummaryByTypeResponse.from_json(json)
# print the JSON string representation of the object
print(ListExpectationSummaryByTypeResponse.to_json())

# convert the object into a dict
list_expectation_summary_by_type_response_dict = list_expectation_summary_by_type_response_instance.to_dict()
# create an instance of ListExpectationSummaryByTypeResponse from a dict
list_expectation_summary_by_type_response_from_dict = ListExpectationSummaryByTypeResponse.from_dict(list_expectation_summary_by_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


