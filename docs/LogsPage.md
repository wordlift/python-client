# LogsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[LogEntryResponse]**](LogEntryResponse.md) |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from wordlift_client.models.logs_page import LogsPage

# TODO update the JSON string below
json = "{}"
# create an instance of LogsPage from a JSON string
logs_page_instance = LogsPage.from_json(json)
# print the JSON string representation of the object
print(LogsPage.to_json())

# convert the object into a dict
logs_page_dict = logs_page_instance.to_dict()
# create an instance of LogsPage from a dict
logs_page_from_dict = LogsPage.from_dict(logs_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


