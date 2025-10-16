# QuickWin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the quick win recommendation | [optional] 
**description** | **str** | Detailed description of the recommendation | [optional] 
**impact** | **str** | Expected impact of implementing this recommendation | [optional] 

## Example

```python
from wordlift_client.models.quick_win import QuickWin

# TODO update the JSON string below
json = "{}"
# create an instance of QuickWin from a JSON string
quick_win_instance = QuickWin.from_json(json)
# print the JSON string representation of the object
print(QuickWin.to_json())

# convert the object into a dict
quick_win_dict = quick_win_instance.to_dict()
# create an instance of QuickWin from a dict
quick_win_from_dict = QuickWin.from_dict(quick_win_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


