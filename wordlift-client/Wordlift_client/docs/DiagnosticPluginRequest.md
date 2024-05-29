# DiagnosticPluginRequest

Diagnostic Plugin Data Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the plugin is active. | [optional] 
**name** | **str** | The plugin name. | [optional] 
**version** | **str** | The plugin version. | [optional] 

## Example

```python
from Wordlift_client.models.diagnostic_plugin_request import DiagnosticPluginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticPluginRequest from a JSON string
diagnostic_plugin_request_instance = DiagnosticPluginRequest.from_json(json)
# print the JSON string representation of the object
print(DiagnosticPluginRequest.to_json())

# convert the object into a dict
diagnostic_plugin_request_dict = diagnostic_plugin_request_instance.to_dict()
# create an instance of DiagnosticPluginRequest from a dict
diagnostic_plugin_request_from_dict = DiagnosticPluginRequest.from_dict(diagnostic_plugin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


