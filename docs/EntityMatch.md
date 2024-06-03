# EntityMatch

Entity Match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **float** | Confidence score for the current entity. | [optional] 
**entity_id** | **str** | The entity URI. | [optional] 

## Example

```python
from wordlift-client.models.entity_match import EntityMatch

# TODO update the JSON string below
json = "{}"
# create an instance of EntityMatch from a JSON string
entity_match_instance = EntityMatch.from_json(json)
# print the JSON string representation of the object
print(EntityMatch.to_json())

# convert the object into a dict
entity_match_dict = entity_match_instance.to_dict()
# create an instance of EntityMatch from a dict
entity_match_from_dict = EntityMatch.from_dict(entity_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


