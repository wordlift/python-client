# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytics_client_factory** | **str** |  | [optional] 
**analyzer_id** | **int** |  | [optional] 
**botify_project** | **str** |  | [optional] 
**botify_token** | **str** |  | [optional] 
**botify_username** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**dataset_id** | **str** |  | [optional] 
**dataset_uri** | **str** |  | [optional] 
**domain_uri** | **str** |  | [optional] 
**google_search_console_site_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**indexed** | **bool** |  | [optional] 
**is_wordpress** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**ng_dataset_id** | **str** |  | [optional] 
**resolved_url** | **str** |  | [optional] 
**subscription_id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**wp_admin** | **str** |  | [optional] 
**wp_json** | **str** |  | [optional] 
**wp_include_exclude_default** | **str** |  | [optional] 

## Example

```python
from wordlift-client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


