# Response1

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
from wordlift_client.models.response1 import Response1

# TODO update the JSON string below
json = "{}"
# create an instance of Response1 from a JSON string
response1_instance = Response1.from_json(json)
# print the JSON string representation of the object
print(Response1.to_json())

# convert the object into a dict
response1_dict = response1_instance.to_dict()
# create an instance of Response1 from a dict
response1_from_dict = Response1.from_dict(response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


