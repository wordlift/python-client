# wordlift_client.GoogleMerchantsApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_google_merchants**](GoogleMerchantsApi.md#list_google_merchants) | **GET** /ext/google/shopping/merchants | List


# **list_google_merchants**
> PageMerchantEntry list_google_merchants(google_access_token)

List

List the Google Merchants

### Example


```python
import wordlift_client
from wordlift_client.models.page_merchant_entry import PageMerchantEntry
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
    api_instance = wordlift_client.GoogleMerchantsApi(api_client)
    google_access_token = 'google_access_token_example' # str | 

    try:
        # List
        api_response = await api_instance.list_google_merchants(google_access_token)
        print("The response of GoogleMerchantsApi->list_google_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleMerchantsApi->list_google_merchants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_access_token** | **str**|  | 

### Return type

[**PageMerchantEntry**](PageMerchantEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

