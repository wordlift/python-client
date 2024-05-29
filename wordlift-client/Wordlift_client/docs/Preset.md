# Preset

An array of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The predefined graphql query. | 
**id** | **int** |  | [optional] 
**label** | **str** | The label of the preset. | 

## Example

```python
from Wordlift_client.models.preset import Preset

# TODO update the JSON string below
json = "{}"
# create an instance of Preset from a JSON string
preset_instance = Preset.from_json(json)
# print the JSON string representation of the object
print(Preset.to_json())

# convert the object into a dict
preset_dict = preset_instance.to_dict()
# create an instance of Preset from a dict
preset_from_dict = Preset.from_dict(preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


