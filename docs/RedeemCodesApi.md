# wordlift_client.RedeemCodesApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redeem_code**](RedeemCodesApi.md#redeem_code) | **POST** /redeem-codes | Redeem the provided code and get a key


# **redeem_code**
> Response2 redeem_code(request3)

Redeem the provided code and get a key

### Example


```python
import wordlift_client
from wordlift_client.models.request3 import Request3
from wordlift_client.models.response2 import Response2
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.RedeemCodesApi(api_client)
    request3 = wordlift_client.Request3() # Request3 | 

    try:
        # Redeem the provided code and get a key
        api_response = await api_instance.redeem_code(request3)
        print("The response of RedeemCodesApi->redeem_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedeemCodesApi->redeem_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request3** | [**Request3**](Request3.md)|  | 

### Return type

[**Response2**](Response2.md)

### Authorization

No authorization required

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

