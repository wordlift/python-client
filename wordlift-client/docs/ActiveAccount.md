# ActiveAccount

An array of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | [optional] 
**diagnostic_plugins** | [**List[DiagnosticPlugin]**](DiagnosticPlugin.md) |  | [optional] 
**domain_uri** | **str** |  | [optional] 
**google_search_console_site_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_wordpress** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**ng_dataset_id** | **str** |  | [optional] 
**package_type** | **str** |  | [optional] 
**subscription** | [**AccountSubscription**](AccountSubscription.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] 
**total_entities** | **int** |  | [optional] 
**total_entities_with_schema_url** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**wp_admin** | **str** |  | [optional] 
**wp_include_exclude_default** | **str** |  | [optional] 
**wp_json** | **str** |  | [optional] 

## Example

```python
from Wordlift_client.models.active_account import ActiveAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveAccount from a JSON string
active_account_instance = ActiveAccount.from_json(json)
# print the JSON string representation of the object
print(ActiveAccount.to_json())

# convert the object into a dict
active_account_dict = active_account_instance.to_dict()
# create an instance of ActiveAccount from a dict
active_account_from_dict = ActiveAccount.from_dict(active_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


