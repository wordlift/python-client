# DecisionSignals

How the decision was reached; present whenever the engine ranked candidates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | &#x60;fast&#x60; (exact dictionary hit, model skipped), &#x60;reranked&#x60; (public world), &#x60;vocabulary&#x60; (your dataset) | 
**retrieval_prior** | **float** |  | [optional] 
**match_probability** | **float** |  | [optional] 
**rescued** | **bool** |  | 

## Example

```python
from wordlift_client.models.decision_signals import DecisionSignals

# TODO update the JSON string below
json = "{}"
# create an instance of DecisionSignals from a JSON string
decision_signals_instance = DecisionSignals.from_json(json)
# print the JSON string representation of the object
print(DecisionSignals.to_json())

# convert the object into a dict
decision_signals_dict = decision_signals_instance.to_dict()
# create an instance of DecisionSignals from a dict
decision_signals_from_dict = DecisionSignals.from_dict(decision_signals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


