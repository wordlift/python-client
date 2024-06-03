# PageWord

A page object with links to move to other pages and the list of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** | The link to the first page. | 
**items** | [**List[Word]**](Word.md) | An array of objects. | 
**last** | **str** | The link to the last page. | 
**next** | **str** | The link to the next page or &#x60;null&#x60; if there&#39;s no page. | 
**prev** | **str** | The link to the previous page or &#x60;null&#x60; if there&#39;s no page. | 
**var_self** | **str** | The link to the current page. | 

## Example

```python
from wordlift-client.models.page_word import PageWord

# TODO update the JSON string below
json = "{}"
# create an instance of PageWord from a JSON string
page_word_instance = PageWord.from_json(json)
# print the JSON string representation of the object
print(PageWord.to_json())

# convert the object into a dict
page_word_dict = page_word_instance.to_dict()
# create an instance of PageWord from a dict
page_word_from_dict = PageWord.from_dict(page_word_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


