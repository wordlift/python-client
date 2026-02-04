# Neighbors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **str** |  | [optional] 
**next** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.neighbors import Neighbors

# TODO update the JSON string below
json = "{}"
# create an instance of Neighbors from a JSON string
neighbors_instance = Neighbors.from_json(json)
# print the JSON string representation of the object
print(Neighbors.to_json())

# convert the object into a dict
neighbors_dict = neighbors_instance.to_dict()
# create an instance of Neighbors from a dict
neighbors_from_dict = Neighbors.from_dict(neighbors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


