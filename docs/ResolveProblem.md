# ResolveProblem

RFC 9457 Problem Details, Content-Type application/problem+json. `code` is the engine's stable error code and `type` is derived from it; extension members carry what the route knows (dataset_uri, mention, accepted, retry_after_s, errors).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | https://docs.wordlift.io/problems/&lt;code&gt; | 
**title** | **str** |  | 
**status** | **int** |  | 
**detail** | **str** | A human-readable sentence, when the engine has one. | [optional] 
**instance** | **str** | The request path. | [optional] 
**code** | **str** | Stable error code: unauthorized, invalid_request, invalid_span, invalid_identity, dataset_not_supported, dataset_required, invalid_dataset, unknown_include, candidates_not_supported, dataset_warming, dataset_unavailable. | 
**errors** | [**List[ResolveValidationError]**](ResolveValidationError.md) | On invalid_request: one entry per failing field. | [optional] 

## Example

```python
from wordlift_client.models.resolve_problem import ResolveProblem

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveProblem from a JSON string
resolve_problem_instance = ResolveProblem.from_json(json)
# print the JSON string representation of the object
print(ResolveProblem.to_json())

# convert the object into a dict
resolve_problem_dict = resolve_problem_instance.to_dict()
# create an instance of ResolveProblem from a dict
resolve_problem_from_dict = ResolveProblem.from_dict(resolve_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


