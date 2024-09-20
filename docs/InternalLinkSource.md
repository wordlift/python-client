# InternalLinkSource

InternalLink source configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity identifier. | [optional] 
**name** | **str** | Entity name. | 
**url** | **str** | Entity url. | 

## Example

```python
from wordlift_client.models.internal_link_source import InternalLinkSource

# TODO update the JSON string below
json = "{}"
# create an instance of InternalLinkSource from a JSON string
internal_link_source_instance = InternalLinkSource.from_json(json)
# print the JSON string representation of the object
print(InternalLinkSource.to_json())

# convert the object into a dict
internal_link_source_dict = internal_link_source_instance.to_dict()
# create an instance of InternalLinkSource from a dict
internal_link_source_from_dict = InternalLinkSource.from_dict(internal_link_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


