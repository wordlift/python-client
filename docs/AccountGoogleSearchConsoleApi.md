# wordlift_client.AccountGoogleSearchConsoleApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_account_config**](AccountGoogleSearchConsoleApi.md#update_account_config) | **PATCH** /accounts/me/google-search-console | Account configuration update


# **update_account_config**
> AccountConfig update_account_config(update_site_url_request)

Account configuration update

Update the Google Search Console siteUrl for the authenticated account.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.account_config import AccountConfig
from wordlift_client.models.update_site_url_request import UpdateSiteUrlRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
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
    api_instance = wordlift_client.AccountGoogleSearchConsoleApi(api_client)
    update_site_url_request = wordlift_client.UpdateSiteUrlRequest() # UpdateSiteUrlRequest | 

    try:
        # Account configuration update
        api_response = await api_instance.update_account_config(update_site_url_request)
        print("The response of AccountGoogleSearchConsoleApi->update_account_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGoogleSearchConsoleApi->update_account_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_site_url_request** | [**UpdateSiteUrlRequest**](UpdateSiteUrlRequest.md)|  | 

### Return type

[**AccountConfig**](AccountConfig.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Google Search Console configuration updated on the account |  -  |
**401** | Unauthorized |  -  |
**412** | GSC api denied or missing |  -  |
**422** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

