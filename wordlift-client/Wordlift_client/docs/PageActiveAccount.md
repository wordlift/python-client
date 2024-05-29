# PageActiveAccount

A page object with links to move to other pages and the list of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** | The link to the first page. | 
**items** | [**List[ActiveAccount]**](ActiveAccount.md) | An array of objects. | 
**last** | **str** | The link to the last page. | 
**next** | **str** | The link to the next page or &#x60;null&#x60; if there&#39;s no page. | 
**prev** | **str** | The link to the previous page or &#x60;null&#x60; if there&#39;s no page. | 
**var_self** | **str** | The link to the current page. | 

## Example

```python
from Wordlift_client.models.page_active_account import PageActiveAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PageActiveAccount from a JSON string
page_active_account_instance = PageActiveAccount.from_json(json)
# print the JSON string representation of the object
print(PageActiveAccount.to_json())

# convert the object into a dict
page_active_account_dict = page_active_account_instance.to_dict()
# create an instance of PageActiveAccount from a dict
page_active_account_from_dict = PageActiveAccount.from_dict(page_active_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


