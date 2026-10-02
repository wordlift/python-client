# ItemsInner1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**type** | **str** |  | 
**config** | [**StructuredDataExpectationConfig**](StructuredDataExpectationConfig.md) |  | 

## Example

```python
from wordlift_client.models.items_inner1 import ItemsInner1

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsInner1 from a JSON string
items_inner1_instance = ItemsInner1.from_json(json)
# print the JSON string representation of the object
print(ItemsInner1.to_json())

# convert the object into a dict
items_inner1_dict = items_inner1_instance.to_dict()
# create an instance of ItemsInner1 from a dict
items_inner1_from_dict = ItemsInner1.from_dict(items_inner1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


