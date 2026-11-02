# ResolveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**dataset_uri** | **str** | The world to resolve against: &#x60;wikidata://public&#x60; (default), &#x60;wordlift://dataset/me&#x60; (your WordLift graph, read with your key), &#x60;inline&#x60; (with &#x60;dataset&#x60;), or a comma-separated ordered list such as &#x60;wordlift://dataset/me,wikidata://public&#x60; (your entities first, Wikidata for the rest). | [optional] [default to 'wikidata://public']
**language** | **str** | ISO 639-1; auto-detected if omitted | [optional] 
**mentions** | [**List[ResolveMention]**](ResolveMention.md) | Explicit spans; if omitted the engine detects mentions | [optional] 
**include** | **List[str]** | Diagnostics: candidates, evidence | [optional] 
**confidence** | **float** | NER threshold when the engine detects mentions | [optional] [default to 0.5]
**dataset** | [**InlineDataset**](InlineDataset.md) | An inline vocabulary (up to 5,000 entities): the answer is one of these ids or unresolved. Implies dataset_uri &#x60;inline&#x60;. | [optional] 

## Example

```python
from wordlift_client.models.resolve_request import ResolveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveRequest from a JSON string
resolve_request_instance = ResolveRequest.from_json(json)
# print the JSON string representation of the object
print(ResolveRequest.to_json())

# convert the object into a dict
resolve_request_dict = resolve_request_instance.to_dict()
# create an instance of ResolveRequest from a dict
resolve_request_from_dict = ResolveRequest.from_dict(resolve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


