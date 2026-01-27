# HtmlSemantics

Legacy field - always returns status Unknown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Always returns Unknown as this analysis is integrated into Content Structure | [optional] 
**explanation** | **str** | Explanation that this is integrated into Content Structure | [optional] 

## Example

```python
from wordlift_client.models.html_semantics import HtmlSemantics

# TODO update the JSON string below
json = "{}"
# create an instance of HtmlSemantics from a JSON string
html_semantics_instance = HtmlSemantics.from_json(json)
# print the JSON string representation of the object
print(HtmlSemantics.to_json())

# convert the object into a dict
html_semantics_dict = html_semantics_instance.to_dict()
# create an instance of HtmlSemantics from a dict
html_semantics_from_dict = HtmlSemantics.from_dict(html_semantics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


