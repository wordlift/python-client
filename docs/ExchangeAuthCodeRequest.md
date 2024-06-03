# ExchangeAuthCodeRequest

The request of the `exchangeAuthCode` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The Authorization Code. The API will use the Authorization Code to exchange it with an Access Token. | 
**google_search_console_resource_id** | **str** | The Google Search Console Resource Id as it shows in the Google Search Console, e.g. sc-domain:example.org. | 

## Example

```python
from wordlift-client.models.exchange_auth_code_request import ExchangeAuthCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeAuthCodeRequest from a JSON string
exchange_auth_code_request_instance = ExchangeAuthCodeRequest.from_json(json)
# print the JSON string representation of the object
print(ExchangeAuthCodeRequest.to_json())

# convert the object into a dict
exchange_auth_code_request_dict = exchange_auth_code_request_instance.to_dict()
# create an instance of ExchangeAuthCodeRequest from a dict
exchange_auth_code_request_from_dict = ExchangeAuthCodeRequest.from_dict(exchange_auth_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


