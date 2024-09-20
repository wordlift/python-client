# wordlift_client.RedeemCodesApi

All URIs are relative to *https://api.wordlift.io/quality-rating*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redeem_code**](RedeemCodesApi.md#redeem_code) | **POST** /redeem-codes | Redeem the provided code and get a key


# **redeem_code**
> Response2 redeem_code(request2)

Redeem the provided code and get a key

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.request2 import Request2
from wordlift_client.models.response2 import Response2
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/quality-rating
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/quality-rating"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.RedeemCodesApi(api_client)
    request2 = wordlift_client.Request2() # Request2 | 

    try:
        # Redeem the provided code and get a key
        api_response = await api_instance.redeem_code(request2)
        print("The response of RedeemCodesApi->redeem_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedeemCodesApi->redeem_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request2** | [**Request2**](Request2.md)|  | 

### Return type

[**Response2**](Response2.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**404** | Not Found. |  -  |
**409** | Code already redeemed. |  -  |
**500** | Configuration error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

