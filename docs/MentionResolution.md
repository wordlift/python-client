# MentionResolution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**type** | **str** |  | [optional] 
**status** | **str** | resolved | unresolved | 
**entity** | [**ResolvedEntity**](ResolvedEntity.md) |  | [optional] 
**score** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 
**candidates** | **List[Dict[str, object]]** |  | [optional] 
**evidence** | **Dict[str, object]** |  | [optional] 
**dataset_uri** | **str** | The world that answered this mention, e.g. &#x60;wordlift://dataset/me&#x60; or &#x60;wikidata://public&#x60;. | [optional] 
**signals** | [**DecisionSignals**](DecisionSignals.md) |  | [optional] 

## Example

```python
from wordlift_client.models.mention_resolution import MentionResolution

# TODO update the JSON string below
json = "{}"
# create an instance of MentionResolution from a JSON string
mention_resolution_instance = MentionResolution.from_json(json)
# print the JSON string representation of the object
print(MentionResolution.to_json())

# convert the object into a dict
mention_resolution_dict = mention_resolution_instance.to_dict()
# create an instance of MentionResolution from a dict
mention_resolution_from_dict = MentionResolution.from_dict(mention_resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


