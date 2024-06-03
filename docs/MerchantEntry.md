# MerchantEntry

A Merchant Entry with the Google Merchant Id and the Website URL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_merchant_id** | **int** | The Google Merchant id | 
**website_url** | **str** | The Google Merchant Website URL | 

## Example

```python
from wordlift-client.models.merchant_entry import MerchantEntry

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantEntry from a JSON string
merchant_entry_instance = MerchantEntry.from_json(json)
# print the JSON string representation of the object
print(MerchantEntry.to_json())

# convert the object into a dict
merchant_entry_dict = merchant_entry_instance.to_dict()
# create an instance of MerchantEntry from a dict
merchant_entry_from_dict = MerchantEntry.from_dict(merchant_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


