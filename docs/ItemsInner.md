# ItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**type** | **str** |  | 
**config** | [**StructuredDataExpectationConfig**](StructuredDataExpectationConfig.md) |  | 

## Example

```python
from wordlift_client.models.items_inner import ItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsInner from a JSON string
items_inner_instance = ItemsInner.from_json(json)
# print the JSON string representation of the object
print(ItemsInner.to_json())

# convert the object into a dict
items_inner_dict = items_inner_instance.to_dict()
# create an instance of ItemsInner from a dict
items_inner_from_dict = ItemsInner.from_dict(items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


