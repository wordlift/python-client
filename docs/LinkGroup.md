# LinkGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**iri** | **str** |  | [optional] 
**items** | [**List[Item]**](Item.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.link_group import LinkGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LinkGroup from a JSON string
link_group_instance = LinkGroup.from_json(json)
# print the JSON string representation of the object
print(LinkGroup.to_json())

# convert the object into a dict
link_group_dict = link_group_instance.to_dict()
# create an instance of LinkGroup from a dict
link_group_from_dict = LinkGroup.from_dict(link_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


