# InternalLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Item]**](Item.md) |  | [optional] 
**template** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.internal_link_request import InternalLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalLinkRequest from a JSON string
internal_link_request_instance = InternalLinkRequest.from_json(json)
# print the JSON string representation of the object
print(InternalLinkRequest.to_json())

# convert the object into a dict
internal_link_request_dict = internal_link_request_instance.to_dict()
# create an instance of InternalLinkRequest from a dict
internal_link_request_from_dict = InternalLinkRequest.from_dict(internal_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


