# WebpageProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | **List[str]** |  | 
**iri** | **str** |  | 
**query** | **str** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from wordlift-client.models.webpage_properties import WebpageProperties

# TODO update the JSON string below
json = "{}"
# create an instance of WebpageProperties from a JSON string
webpage_properties_instance = WebpageProperties.from_json(json)
# print the JSON string representation of the object
print(WebpageProperties.to_json())

# convert the object into a dict
webpage_properties_dict = webpage_properties_instance.to_dict()
# create an instance of WebpageProperties from a dict
webpage_properties_from_dict = WebpageProperties.from_dict(webpage_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


