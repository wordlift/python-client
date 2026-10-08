# ResolveCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identity in the dataset: Q312, wd:Q312 or a Wikidata entity URI | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**score** | **float** |  | [optional] 

## Example

```python
from wordlift_client.models.resolve_candidate import ResolveCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveCandidate from a JSON string
resolve_candidate_instance = ResolveCandidate.from_json(json)
# print the JSON string representation of the object
print(ResolveCandidate.to_json())

# convert the object into a dict
resolve_candidate_dict = resolve_candidate_instance.to_dict()
# create an instance of ResolveCandidate from a dict
resolve_candidate_from_dict = ResolveCandidate.from_dict(resolve_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


