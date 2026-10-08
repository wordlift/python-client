# InlineDataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[UserEntity]**](UserEntity.md) |  | 

## Example

```python
from wordlift_client.models.inline_dataset import InlineDataset

# TODO update the JSON string below
json = "{}"
# create an instance of InlineDataset from a JSON string
inline_dataset_instance = InlineDataset.from_json(json)
# print the JSON string representation of the object
print(InlineDataset.to_json())

# convert the object into a dict
inline_dataset_dict = inline_dataset_instance.to_dict()
# create an instance of InlineDataset from a dict
inline_dataset_from_dict = InlineDataset.from_dict(inline_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


