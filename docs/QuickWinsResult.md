# QuickWinsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Overall quick wins status | [optional] 
**explanation** | **str** | Explanation of quick wins findings | [optional] 
**wins** | [**List[QuickWin]**](QuickWin.md) | List of quick win recommendations | [optional] 

## Example

```python
from wordlift_client.models.quick_wins_result import QuickWinsResult

# TODO update the JSON string below
json = "{}"
# create an instance of QuickWinsResult from a JSON string
quick_wins_result_instance = QuickWinsResult.from_json(json)
# print the JSON string representation of the object
print(QuickWinsResult.to_json())

# convert the object into a dict
quick_wins_result_dict = quick_wins_result_instance.to_dict()
# create an instance of QuickWinsResult from a dict
quick_wins_result_from_dict = QuickWinsResult.from_dict(quick_wins_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


