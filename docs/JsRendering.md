# JsRendering


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**framework_detected** | **str** | Detected JavaScript framework (React, Vue, Angular, etc.) | [optional] 
**rendering_type** | **str** | Type of rendering used by the site | [optional] 
**ai_accessibility** | **str** | How accessible the content is to AI agents | [optional] 
**content_availability** | **str** | Description of content availability in HTML | [optional] 
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


