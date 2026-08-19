# ListCheckSummaryByCheckResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CheckSummaryByCheckItem]**](CheckSummaryByCheckItem.md) |  | 
**total** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.list_check_summary_by_check_response import ListCheckSummaryByCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCheckSummaryByCheckResponse from a JSON string
list_check_summary_by_check_response_instance = ListCheckSummaryByCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ListCheckSummaryByCheckResponse.to_json())

# convert the object into a dict
list_check_summary_by_check_response_dict = list_check_summary_by_check_response_instance.to_dict()
# create an instance of ListCheckSummaryByCheckResponse from a dict
list_check_summary_by_check_response_from_dict = ListCheckSummaryByCheckResponse.from_dict(list_check_summary_by_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


