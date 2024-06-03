# MerchantSync

A Merchant products data synchronization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The create date-time. | [optional] [readonly] 
**has_errors** | **bool** | Whether the sync encountered errors. | [optional] [readonly] 
**id** | **int** | The unique id. | [optional] [readonly] 
**merchant_id** | **int** | The parent Merchant id. | [readonly] 
**modified_at** | **datetime** | The last modified date-time. | [optional] [readonly] 
**products_created** | **int** | The number of created products | [optional] [readonly] 
**products_deleted** | **int** | The number of deleted products | [optional] [readonly] 
**products_errored** | **int** | The number of errored products | [optional] [readonly] 
**products_skipped** | **int** | The number of skipped products | [optional] [readonly] 
**products_total** | **int** | The total number of processed products, including the skipped and errored. | [optional] [readonly] 
**products_updated** | **int** | The number of update products | [optional] [readonly] 
**started_at** | **datetime** | The started date-time. | [optional] [readonly] 
**stopped_at** | **datetime** | The stopped date-time. | [optional] [readonly] 

## Example

```python
from wordlift_client.models.merchant_sync import MerchantSync

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSync from a JSON string
merchant_sync_instance = MerchantSync.from_json(json)
# print the JSON string representation of the object
print(MerchantSync.to_json())

# convert the object into a dict
merchant_sync_dict = merchant_sync_instance.to_dict()
# create an instance of MerchantSync from a dict
merchant_sync_from_dict = MerchantSync.from_dict(merchant_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


