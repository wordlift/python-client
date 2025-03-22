# InternalLinkDestination

InternalLink destinations configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The entity ID, usually a URI. | 
**name** | **str** | The entity&#39;s name, or headline. | 
**position** | **int** | The position of an item in a series or sequence of items. | 
**url** | **str** | The entity&#39;s web page URL. | 

## Example

```python
from wordlift_client.models.internal_link_destination import InternalLinkDestination

# TODO update the JSON string below
json = "{}"
# create an instance of InternalLinkDestination from a JSON string
internal_link_destination_instance = InternalLinkDestination.from_json(json)
# print the JSON string representation of the object
print(InternalLinkDestination.to_json())

# convert the object into a dict
internal_link_destination_dict = internal_link_destination_instance.to_dict()
# create an instance of InternalLinkDestination from a dict
internal_link_destination_from_dict = InternalLinkDestination.from_dict(internal_link_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


