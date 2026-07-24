# SmartContentProject

A Smart Content project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The account id. | [readonly] 
**created_at** | **datetime** | The create date-time. | [optional] [readonly] 
**id** | **int** | The unique id. | [optional] [readonly] 
**model_id** | **int** | The model id. | [optional] [default to 1]
**name** | **str** | The name of the smart content - applicable if bulk. | [optional] [readonly] 
**quantity** | **str** | The type of the Smart Content - single or bulk. | [optional] [readonly] 

## Example

```python
from wordlift_client.models.smart_content_project import SmartContentProject

# TODO update the JSON string below
json = "{}"
# create an instance of SmartContentProject from a JSON string
smart_content_project_instance = SmartContentProject.from_json(json)
# print the JSON string representation of the object
print(SmartContentProject.to_json())

# convert the object into a dict
smart_content_project_dict = smart_content_project_instance.to_dict()
# create an instance of SmartContentProject from a dict
smart_content_project_from_dict = SmartContentProject.from_dict(smart_content_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


