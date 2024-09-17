# InternalLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | [**List[InternalLinkDestination]**](InternalLinkDestination.md) | InternalLink destinations configuration. | 
**source** | [**InternalLinkSource**](InternalLinkSource.md) |  | 

## Example

```python
from wordlift_client.models.internal_link import InternalLink

# TODO update the JSON string below
json = "{}"
# create an instance of InternalLink from a JSON string
internal_link_instance = InternalLink.from_json(json)
# print the JSON string representation of the object
print(InternalLink.to_json())

# convert the object into a dict
internal_link_dict = internal_link_instance.to_dict()
# create an instance of InternalLink from a dict
internal_link_from_dict = InternalLink.from_dict(internal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


