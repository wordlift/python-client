# SmartContent

A Smart Content project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The account id. | [readonly] 
**created_at** | **datetime** | The create date-time. | [optional] [readonly] 
**id** | **int** | The unique id. | [optional] [readonly] 
**model_id** | **int** | The model id. | [optional] [default to 1]

## Example

```python
from Wordlift_client.models.smart_content import SmartContent

# TODO update the JSON string below
json = "{}"
# create an instance of SmartContent from a JSON string
smart_content_instance = SmartContent.from_json(json)
# print the JSON string representation of the object
print(SmartContent.to_json())

# convert the object into a dict
smart_content_dict = smart_content_instance.to_dict()
# create an instance of SmartContent from a dict
smart_content_from_dict = SmartContent.from_dict(smart_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


