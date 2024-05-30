# Html

The html fragment or html page to analyze.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fragment** | **str** | The html fragment to analyze. | [optional] 
**page** | **str** | The html page to analyze, either fragment or page should be present | [optional] 

## Example

```python
from Wordlift_client.models.html import Html

# TODO update the JSON string below
json = "{}"
# create an instance of Html from a JSON string
html_instance = Html.from_json(json)
# print the JSON string representation of the object
print(Html.to_json())

# convert the object into a dict
html_dict = html_instance.to_dict()
# create an instance of Html from a dict
html_from_dict = Html.from_dict(html_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


