# MerchantRequest

The Merchant request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Google Merchant access token | [optional] 
**account_id** | **int** | The Knowledge Graph to use for the Merchant. Please note that the Knowledge Graph will be reset. When not provided, this method will use the first available Knowledge Graph. | [optional] 
**dataset_domain** | **str** | The custom domain (for example data.example.org) | [optional] 
**dataset_name** | **str** | The dataset path (for example \&quot;data\&quot;) | [optional] 
**deleted** | **bool** | True if the merchant has been deleted | [optional] [default to False]
**google_merchant_id** | **int** | The Google Merchant id | 
**ignore_brand** | **bool** | Whether to ignore the &#x60;brand&#x60; property during validation | [optional] 
**ignore_image** | **bool** | Whether to ignore the &#x60;image&#x60; property during validation | [optional] 
**publisher_name** | **str** | The publisher name (shows in schema publisher) | 
**refresh_token** | **str** | Google Merchant refresh token | 
**url** | **str** | The website URL | 
**url_strategy** | **str** | Which strategy to use to write the url schema. | [optional] [default to 'canonicalLinkAndLink']
**writer_service** | **str** | How to write the merchant data to the graph, if unsure, do not set anything (by default &#x60;wordpressMerchantWriter&#x60;). | [optional] 

## Example

```python
from wordlift_client.models.merchant_request import MerchantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantRequest from a JSON string
merchant_request_instance = MerchantRequest.from_json(json)
# print the JSON string representation of the object
print(MerchantRequest.to_json())

# convert the object into a dict
merchant_request_dict = merchant_request_instance.to_dict()
# create an instance of MerchantRequest from a dict
merchant_request_from_dict = MerchantRequest.from_dict(merchant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


