# wordlift_client.RedeemCodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redeem_code**](RedeemCodesApi.md#redeem_code) | **POST** /redeem-codes | Redeem the provided code and get a key


# **redeem_code**
> Response redeem_code(request)

Redeem the provided code and get a key

### Example


```python
import wordlift_client
from wordlift_client.models.request import Request
from wordlift_client.models.response import Response
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.RedeemCodesApi(api_client)
    request = wordlift_client.Request() # Request | 

    try:
        # Redeem the provided code and get a key
        api_response = await api_instance.redeem_code(request)
        print("The response of RedeemCodesApi->redeem_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedeemCodesApi->redeem_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)|  | 

### Return type

[**Response**](Response.md)

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

