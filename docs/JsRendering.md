# JsRendering


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | Numeric score for JavaScript rendering (0-15) | 
**explanation** | **str** |  | 
**framework_detected** | **str** | Detected JavaScript framework (None, React, Vue, Angular, Next.js, Nuxt, Gatsby) | 
**rendering_type** | **str** | Type of rendering used by the site | 
**content_availability** | **str** | How much of the content is available in the HTML | 
**recommendations** | **List[str]** | Recommendations for improving JS rendering | 
**status** | **str** |  | 

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


