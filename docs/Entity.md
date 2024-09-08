# Entity

Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | The entity URI. | [optional] 
**confidence** | **float** | Confidence score representing the entity match level. | [optional] 
**main_type** | **str** | The main schema type for the current entity. | [optional] 
**types** | **List[str]** | The list of schema types which the entity can be classified to. | [optional] 
**label** | **str** | The title of the entity. | [optional] 
**description** | **str** | The description about the entity. | [optional] 
**images** | **List[str]** | The list of entity image URIs. | [optional] 
**same_as** | **List[str]** | The list of entity sameas URIs. | [optional] 
**properties** | [**Properties**](Properties.md) |  | [optional] 
**synonyms** | **List[str]** |  | [optional] 

## Example

```python
from wordlift_client.models.entity import Entity

# TODO update the JSON string below
json = "{}"
# create an instance of Entity from a JSON string
entity_instance = Entity.from_json(json)
# print the JSON string representation of the object
print(Entity.to_json())

# convert the object into a dict
entity_dict = entity_instance.to_dict()
# create an instance of Entity from a dict
entity_from_dict = Entity.from_dict(entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


