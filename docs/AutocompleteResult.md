# AutocompleteResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**descriptions** | **List[str]** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**urls** | **List[str]** |  | [optional] 
**images** | **List[str]** | A list of image URLs. | [optional] 
**same_ass** | **List[str]** |  | [optional] 
**scope** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**main_type** | **str** | Schema type slug | [optional] 
**value** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**display_types** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.autocomplete_result import AutocompleteResult

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteResult from a JSON string
autocomplete_result_instance = AutocompleteResult.from_json(json)
# print the JSON string representation of the object
print(AutocompleteResult.to_json())

# convert the object into a dict
autocomplete_result_dict = autocomplete_result_instance.to_dict()
# create an instance of AutocompleteResult from a dict
autocomplete_result_from_dict = AutocompleteResult.from_dict(autocomplete_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


