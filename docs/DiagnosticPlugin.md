# DiagnosticPlugin

Plugin Data used for diagnostics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The account id. | [optional] [readonly] 
**active** | **bool** | Whether the plugin is active. | [optional] 
**created_at** | **datetime** | The create date-time | [optional] [readonly] 
**id** | **int** | The record id. | [optional] [readonly] 
**name** | **str** | The plugin name. | [optional] 
**version** | **str** | The plugin version. | [optional] 

## Example

```python
from wordlift-client.models.diagnostic_plugin import DiagnosticPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticPlugin from a JSON string
diagnostic_plugin_instance = DiagnosticPlugin.from_json(json)
# print the JSON string representation of the object
print(DiagnosticPlugin.to_json())

# convert the object into a dict
diagnostic_plugin_dict = diagnostic_plugin_instance.to_dict()
# create an instance of DiagnosticPlugin from a dict
diagnostic_plugin_from_dict = DiagnosticPlugin.from_dict(diagnostic_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


