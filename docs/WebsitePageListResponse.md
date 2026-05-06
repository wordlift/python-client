# WebsitePageListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WebsitePageSummary]**](WebsitePageSummary.md) |  | 
**page** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from wordlift_client.models.website_page_list_response import WebsitePageListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebsitePageListResponse from a JSON string
website_page_list_response_instance = WebsitePageListResponse.from_json(json)
# print the JSON string representation of the object
print(WebsitePageListResponse.to_json())

# convert the object into a dict
website_page_list_response_dict = website_page_list_response_instance.to_dict()
# create an instance of WebsitePageListResponse from a dict
website_page_list_response_from_dict = WebsitePageListResponse.from_dict(website_page_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


