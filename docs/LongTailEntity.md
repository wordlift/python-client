# LongTailEntity

The list of entities matching the query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | The referenced entity URI | [optional] 
**properties** | [**LongTailProperties**](LongTailProperties.md) |  | [optional] 

## Example

```python
from wordlift_client.models.long_tail_entity import LongTailEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LongTailEntity from a JSON string
long_tail_entity_instance = LongTailEntity.from_json(json)
# print the JSON string representation of the object
print(LongTailEntity.to_json())

# convert the object into a dict
long_tail_entity_dict = long_tail_entity_instance.to_dict()
# create an instance of LongTailEntity from a dict
long_tail_entity_from_dict = LongTailEntity.from_dict(long_tail_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


