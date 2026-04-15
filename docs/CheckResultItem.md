# CheckResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**run_id** | **str** |  | 
**state** | **str** |  | 
**score** | **float** |  | [optional] 
**details** | **str** |  | [optional] 
**execution_ms** | **float** |  | 

## Example

```python
from wordlift_client.models.check_result_item import CheckResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of CheckResultItem from a JSON string
check_result_item_instance = CheckResultItem.from_json(json)
# print the JSON string representation of the object
print(CheckResultItem.to_json())

# convert the object into a dict
check_result_item_dict = check_result_item_instance.to_dict()
# create an instance of CheckResultItem from a dict
check_result_item_from_dict = CheckResultItem.from_dict(check_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


