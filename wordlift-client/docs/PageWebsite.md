# PageWebsite

A page object with links to move to other pages and the list of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** | The link to the first page. | 
**items** | [**List[Website]**](Website.md) | An array of objects. | 
**last** | **str** | The link to the last page. | 
**next** | **str** | The link to the next page or &#x60;null&#x60; if there&#39;s no page. | 
**prev** | **str** | The link to the previous page or &#x60;null&#x60; if there&#39;s no page. | 
**var_self** | **str** | The link to the current page. | 

## Example

```python
from Wordlift_client.models.page_website import PageWebsite

# TODO update the JSON string below
json = "{}"
# create an instance of PageWebsite from a JSON string
page_website_instance = PageWebsite.from_json(json)
# print the JSON string representation of the object
print(PageWebsite.to_json())

# convert the object into a dict
page_website_dict = page_website_instance.to_dict()
# create an instance of PageWebsite from a dict
page_website_from_dict = PageWebsite.from_dict(page_website_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


