# MerchantView

An array of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The Google merchant access token | 
**account_id** | **int** | The account id | [optional] [readonly] 
**automatic_synchronization** | **bool** | Whether the Merchant data will be synchronized automatically | [optional] 
**created_at** | **datetime** | The create date-time | [optional] [readonly] 
**custom_seller** | **str** | Custom seller entity - if applicable. | [optional] 
**dataset_domain** | **str** | The custom domain (for example data.example.org) | [optional] 
**dataset_name** | **str** | The dataset path (for example /data) | [optional] 
**default_products_filter_action** | **str** | Default Products filter action to apply during sync process. | [default to 'PROCESS']
**deleted** | **bool** | True if the merchant has been deleted | [default to False]
**deleted_at** | **datetime** | The delete date-time | [optional] [readonly] 
**google_merchant_id** | **int** | The Google Merchant id | 
**id** | **int** | The unique id | [optional] [readonly] 
**ignore_brand** | **bool** | Whether to ignore the &#x60;brand&#x60; property during validation | [optional] 
**ignore_image** | **bool** | Whether to ignore the &#x60;image&#x60; property during validation | [optional] 
**modified_at** | **datetime** | The last modified date-time | [optional] [readonly] 
**publisher_name** | **str** | The publisher name (shows in schema publisher) | 
**refresh_token** | **str** | The Google merchant refresh token | 
**sid** | **str** |  | [optional] 
**sync_has_errors** | **bool** |  | [optional] 
**sync_id** | **int** |  | [optional] 
**sync_products_created** | **int** |  | [optional] 
**sync_products_deleted** | **int** |  | [optional] 
**sync_products_errored** | **int** |  | [optional] 
**sync_products_skipped** | **int** |  | [optional] 
**sync_products_total** | **int** |  | [optional] 
**sync_products_unchanged** | **int** |  | [optional] 
**sync_products_updated** | **int** |  | [optional] 
**sync_started_at** | **datetime** | The started date-time. | [optional] [readonly] 
**sync_stopped_at** | **datetime** | The stopped date-time. | [optional] [readonly] 
**url** | **str** | The website URL | [optional] 
**url_strategy** | **str** | Which strategy to use to write the url schema. | [optional] [default to 'canonicalLinkAndLink']
**writer_service** | **str** | How to write the merchant data to the graph, if unsure, do not set anything (by default &#x60;wordpressMerchantWriter&#x60;). | [optional] 

## Example

```python
from wordlift_client.models.merchant_view import MerchantView

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantView from a JSON string
merchant_view_instance = MerchantView.from_json(json)
# print the JSON string representation of the object
print(MerchantView.to_json())

# convert the object into a dict
merchant_view_dict = merchant_view_instance.to_dict()
# create an instance of MerchantView from a dict
merchant_view_from_dict = MerchantView.from_dict(merchant_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


