# Request2

The request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | [**Html**](Html.md) |  | [optional] 
**url** | **str** | The url of the page to analyze. | [optional] 
**url_client** | **str** | The client which the analysis should use to extract the content, by default chrome is used. | [optional] 
**language** | **str** | The content language, 2 letters code, e.g. &#39;en&#39;. | 
**text** | **str** | A textual fragment. | [optional] 
**exclude** | **List[str]** | An array of item IDs to exclude from the analysis results. | [optional] 
**scope** | **str** | The scope of the analysis, one of &#39;local&#39;, &#39;network&#39;, &#39;cloud-only&#39;, &#39;network-only&#39; or &#39;all&#39;. | 
**matches** | **int** | Filter out results that don&#39;t have at least the specified number of occurrences. By default 1. | [optional] 
**links** | **str** | When returning an interpolated HTML results, matches should have the &#39;wl-link&#39; class. By default &#39;no&#39;. | [optional] 

## Example

```python
from wordlift_client.models.request2 import Request2

# TODO update the JSON string below
json = "{}"
# create an instance of Request2 from a JSON string
request2_instance = Request2.from_json(json)
# print the JSON string representation of the object
print(Request2.to_json())

# convert the object into a dict
request2_dict = request2_instance.to_dict()
# create an instance of Request2 from a dict
request2_from_dict = Request2.from_dict(request2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


