# AnchorText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_prompt_template** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**max_characters** | **int** |  | [optional] 
**model** | **str** |  | [optional] 
**prompt_template** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.anchor_text import AnchorText

# TODO update the JSON string below
json = "{}"
# create an instance of AnchorText from a JSON string
anchor_text_instance = AnchorText.from_json(json)
# print the JSON string representation of the object
print(AnchorText.to_json())

# convert the object into a dict
anchor_text_dict = anchor_text_instance.to_dict()
# create an instance of AnchorText from a dict
anchor_text_from_dict = AnchorText.from_dict(anchor_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


