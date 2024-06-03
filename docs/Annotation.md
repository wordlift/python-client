# Annotation

Object representing single annotation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation_id** | **str** | An unique id. | [optional] 
**start** | **int** | The starting posistion of annotation in content (zero-indexed &amp; non negative ). | [optional] 
**end** | **int** | The ending posistion of annotation in content (zero-indexed &amp; non negative ). | [optional] 
**text** | **str** | The annotated text. | [optional] 
**entity_matches** | [**List[EntityMatch]**](EntityMatch.md) | The list of entities which the annotation matches. | [optional] 

## Example

```python
from wordlift_client.models.annotation import Annotation

# TODO update the JSON string below
json = "{}"
# create an instance of Annotation from a JSON string
annotation_instance = Annotation.from_json(json)
# print the JSON string representation of the object
print(Annotation.to_json())

# convert the object into a dict
annotation_dict = annotation_instance.to_dict()
# create an instance of Annotation from a dict
annotation_from_dict = Annotation.from_dict(annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


