# Response2

Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**Dict[str, Entity1]**](Entity1.md) | A map of entity URI to the respective entity. | [optional] 
**annotations** | [**Dict[str, Annotation]**](Annotation.md) | A map of annotation id to the respective annotation. | [optional] 
**images** | [**List[Image]**](Image.md) | A list of images. | [optional] 
**languages** | **List[str]** | A list of languages. | [optional] 
**topics** | [**List[Topic]**](Topic.md) | A list of topics. | [optional] 
**content** | **str** | The text supplied for analysis. | [optional] 

## Example

```python
from wordlift_client.models.response2 import Response2

# TODO update the JSON string below
json = "{}"
# create an instance of Response2 from a JSON string
response2_instance = Response2.from_json(json)
# print the JSON string representation of the object
print(Response2.to_json())

# convert the object into a dict
response2_dict = response2_instance.to_dict()
# create an instance of Response2 from a dict
response2_from_dict = Response2.from_dict(response2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


