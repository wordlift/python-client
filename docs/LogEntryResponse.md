# LogEntryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**entry** | **Dict[str, object]** |  | 
**logged_at** | **datetime** |  | 

## Example

```python
from wordlift_client.models.log_entry_response import LogEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogEntryResponse from a JSON string
log_entry_response_instance = LogEntryResponse.from_json(json)
# print the JSON string representation of the object
print(LogEntryResponse.to_json())

# convert the object into a dict
log_entry_response_dict = log_entry_response_instance.to_dict()
# create an instance of LogEntryResponse from a dict
log_entry_response_from_dict = LogEntryResponse.from_dict(log_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


