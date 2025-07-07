# LinkGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_groups** | [**List[LinkGroup]**](LinkGroup.md) |  | [optional] 

## Example

```python
from wordlift_client.models.link_group_response import LinkGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkGroupResponse from a JSON string
link_group_response_instance = LinkGroupResponse.from_json(json)
# print the JSON string representation of the object
print(LinkGroupResponse.to_json())

# convert the object into a dict
link_group_response_dict = link_group_response_instance.to_dict()
# create an instance of LinkGroupResponse from a dict
link_group_response_from_dict = LinkGroupResponse.from_dict(link_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


