# NetworkAccountInfo

Network Account Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The Account Id | [optional] [readonly] 
**dataset_id** | **str** | The Dataset Id | [optional] [readonly] 
**dataset_uri** | **str** | The Dataset URI | [readonly] 
**url** | **str** | The website URL | [optional] [readonly] 

## Example

```python
from Wordlift_client.models.network_account_info import NetworkAccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAccountInfo from a JSON string
network_account_info_instance = NetworkAccountInfo.from_json(json)
# print the JSON string representation of the object
print(NetworkAccountInfo.to_json())

# convert the object into a dict
network_account_info_dict = network_account_info_instance.to_dict()
# create an instance of NetworkAccountInfo from a dict
network_account_info_from_dict = NetworkAccountInfo.from_dict(network_account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


