# JsRendering


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | Numeric score for JavaScript rendering (0-15) | [optional] 
**status** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**framework_detected** | **str** | Detected JavaScript framework (None, React, Vue, Angular, Next.js, Nuxt, Gatsby, Other) | [optional] 
**rendering_type** | **str** | Type of rendering used by the site | [optional] 
**content_availability** | **str** | Description of content availability in HTML (e.g., \&quot;All content in HTML\&quot;, \&quot;Mostly in HTML\&quot;, \&quot;Partially in JS\&quot;, \&quot;Mostly in JS\&quot;) | [optional] 
**recommendations** | **List[str]** | Recommendations for improving JS rendering | [optional] 

## Example

```python
from wordlift_client.models.js_rendering import JsRendering

# TODO update the JSON string below
json = "{}"
# create an instance of JsRendering from a JSON string
js_rendering_instance = JsRendering.from_json(json)
# print the JSON string representation of the object
print(JsRendering.to_json())

# convert the object into a dict
js_rendering_dict = js_rendering_instance.to_dict()
# create an instance of JsRendering from a dict
js_rendering_from_dict = JsRendering.from_dict(js_rendering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


