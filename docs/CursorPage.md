# CursorPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_cursor** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.cursor_page import CursorPage

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPage from a JSON string
cursor_page_instance = CursorPage.from_json(json)
# print the JSON string representation of the object
print(CursorPage.to_json())

# convert the object into a dict
cursor_page_dict = cursor_page_instance.to_dict()
# create an instance of CursorPage from a dict
cursor_page_from_dict = CursorPage.from_dict(cursor_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


