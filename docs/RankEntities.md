# RankEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | [optional] 
**entities** | [**List[Entity1]**](Entity1.md) |  | [optional] 

## Example

```python
from wordlift_client.models.rank_entities import RankEntities

# TODO update the JSON string below
json = "{}"
# create an instance of RankEntities from a JSON string
rank_entities_instance = RankEntities.from_json(json)
# print the JSON string representation of the object
print(RankEntities.to_json())

# convert the object into a dict
rank_entities_dict = rank_entities_instance.to_dict()
# create an instance of RankEntities from a dict
rank_entities_from_dict = RankEntities.from_dict(rank_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


