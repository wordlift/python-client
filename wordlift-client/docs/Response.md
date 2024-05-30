# Response

Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**Dict[str, Entity]**](Entity.md) | A map of entity URI to the respective entity. | [optional] 
**annotations** | [**Dict[str, Annotation]**](Annotation.md) | A map of annotation id to the respective annotation. | [optional] 
**images** | [**List[Image]**](Image.md) | A list of images. | [optional] 
**languages** | **List[str]** | A list of languages. | [optional] 
**topics** | [**List[Topic]**](Topic.md) | A list of topics. | [optional] 
**content** | **str** | The text supplied for analysis. | [optional] 

## Example

```python
from Wordlift_client.models.response import Response

# TODO update the JSON string below
json = "{}"
# create an instance of Response from a JSON string
response_instance = Response.from_json(json)
# print the JSON string representation of the object
print(Response.to_json())

# convert the object into a dict
response_dict = response_instance.to_dict()
# create an instance of Response from a dict
response_from_dict = Response.from_dict(response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


