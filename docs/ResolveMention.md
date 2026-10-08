# ResolveMention


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**type** | **str** |  | [optional] 
**candidates** | [**List[ResolveCandidate]**](ResolveCandidate.md) |  | [optional] 

## Example

```python
from wordlift_client.models.resolve_mention import ResolveMention

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveMention from a JSON string
resolve_mention_instance = ResolveMention.from_json(json)
# print the JSON string representation of the object
print(ResolveMention.to_json())

# convert the object into a dict
resolve_mention_dict = resolve_mention_instance.to_dict()
# create an instance of ResolveMention from a dict
resolve_mention_from_dict = ResolveMention.from_dict(resolve_mention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


