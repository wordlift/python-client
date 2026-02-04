# UrlListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UrlListItem]**](UrlListItem.md) |  | 
**page** | [**PageInfo**](PageInfo.md) |  | 
**links** | **Dict[str, str]** |  | 

## Example

```python
from wordlift_client.models.url_list_response import UrlListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UrlListResponse from a JSON string
url_list_response_instance = UrlListResponse.from_json(json)
# print the JSON string representation of the object
print(UrlListResponse.to_json())

# convert the object into a dict
url_list_response_dict = url_list_response_instance.to_dict()
# create an instance of UrlListResponse from a dict
url_list_response_from_dict = UrlListResponse.from_dict(url_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


