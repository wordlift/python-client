# AccountInfo

Account Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The Account Id | [readonly] 
**country_code** | **str** | The country code | [optional] [readonly] 
**dataset_id** | **str** | The Dataset Id | [optional] [readonly] 
**dataset_uri** | **str** | The dataset URI | [readonly] 
**default_data_formatter** | **str** | The default data formatter used by the account to format the JSON+LD of the data from the KG. | [optional] [readonly] 
**features** | **Dict[str, bool]** | A list of features enabled or disabled for the account | [optional] [readonly] 
**google_search_console_site_url** | **str** | Google Search Console Site URL | [optional] [readonly] 
**include_exclude_default** | **str** | The default setting for include/exclude URLs. | [optional] [readonly] [default to 'include']
**key** | **str** | The Key | [optional] [readonly] 
**language** | **str** | The language code | [optional] [readonly] 
**networks** | [**List[NetworkAccountInfo]**](NetworkAccountInfo.md) | A list of connected Account Information | [readonly] 
**ng_dataset_id** | **str** |  | [optional] 
**subscription_id** | **int** | The Subscription Id | [readonly] 
**tokens** | [**Dict[str, Tokens]**](Tokens.md) | Tokens associated with this account/graph. | [optional] [readonly] 
**url** | **str** | The website URL | [optional] [readonly] 
**wp_admin** | **str** | If WordPress, the WP-ADMIN URL | [optional] [readonly] 
**wp_json** | **str** | If WordPress, the WP-JSON end-point | [optional] [readonly] 

## Example

```python
from wordlift_client.models.account_info import AccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfo from a JSON string
account_info_instance = AccountInfo.from_json(json)
# print the JSON string representation of the object
print(AccountInfo.to_json())

# convert the object into a dict
account_info_dict = account_info_instance.to_dict()
# create an instance of AccountInfo from a dict
account_info_from_dict = AccountInfo.from_dict(account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


