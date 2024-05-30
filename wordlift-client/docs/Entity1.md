# Entity1

The list of entities matching the query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | The referenced entity URI | [optional] 
**properties** | [**Properties1**](Properties1.md) |  | [optional] 

## Example

```python
from Wordlift_client.models.entity1 import Entity1

# TODO update the JSON string below
json = "{}"
# create an instance of Entity1 from a JSON string
entity1_instance = Entity1.from_json(json)
# print the JSON string representation of the object
print(Entity1.to_json())

# convert the object into a dict
entity1_dict = entity1_instance.to_dict()
# create an instance of Entity1 from a dict
entity1_from_dict = Entity1.from_dict(entity1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


