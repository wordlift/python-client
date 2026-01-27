# InternalLinking

Legacy field - always returns status Unknown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Always returns Unknown as this analysis is integrated into Content Structure | [optional] 
**explanation** | **str** | Explanation that this is integrated into Content Structure | [optional] 

## Example

```python
from wordlift_client.models.internal_linking import InternalLinking

# TODO update the JSON string below
json = "{}"
# create an instance of InternalLinking from a JSON string
internal_linking_instance = InternalLinking.from_json(json)
# print the JSON string representation of the object
print(InternalLinking.to_json())

# convert the object into a dict
internal_linking_dict = internal_linking_instance.to_dict()
# create an instance of InternalLinking from a dict
internal_linking_from_dict = InternalLinking.from_dict(internal_linking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


