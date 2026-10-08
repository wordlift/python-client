# ResolvedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**label** | **str** |  | 
**description** | **str** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**same_as** | **List[str]** |  | [optional] 

## Example

```python
from wordlift_client.models.resolved_entity import ResolvedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedEntity from a JSON string
resolved_entity_instance = ResolvedEntity.from_json(json)
# print the JSON string representation of the object
print(ResolvedEntity.to_json())

# convert the object into a dict
resolved_entity_dict = resolved_entity_instance.to_dict()
# create an instance of ResolvedEntity from a dict
resolved_entity_from_dict = ResolvedEntity.from_dict(resolved_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


