# MonitorCheckName

Identifier of a monitor check plugin.  Mirrors the ``name`` returned by SDK monitor plugins and the ``check_name`` column on ``monitor_check_results``. Listed here for type-safety on the domain and API models that reference a check. Each value imports its string from the plugin package that owns it, so writer (this enum) and reader (the plugin's ``Monitor.name``) can't drift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


