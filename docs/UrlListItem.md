# UrlListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**resource_type** | [**ResourceType**](ResourceType.md) |  | 
**is_enabled** | **bool** |  | 
**status** | **str** |  | 
**last_run** | **datetime** |  | [optional] 
**last_success** | **datetime** |  | [optional] 
**score** | **float** |  | [optional] 
**ttfb_ms** | **float** |  | [optional] 
**response_time_ms** | **float** |  | [optional] 

## Example

```python
from wordlift_client.models.url_list_item import UrlListItem

# TODO update the JSON string below
json = "{}"
# create an instance of UrlListItem from a JSON string
url_list_item_instance = UrlListItem.from_json(json)
# print the JSON string representation of the object
print(UrlListItem.to_json())

# convert the object into a dict
url_list_item_dict = url_list_item_instance.to_dict()
# create an instance of UrlListItem from a dict
url_list_item_from_dict = UrlListItem.from_dict(url_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


