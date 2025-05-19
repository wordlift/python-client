# wordlift_client.AccountStatsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_stats**](AccountStatsApi.md#get_my_stats) | **GET** /accounts/me/stats | Get my Account statistics


# **get_my_stats**
> AccountStats get_my_stats()

Get my Account statistics

Get the Account statistics, such the number of products, product groups and urls in the KG.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.account_stats import AccountStats
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountStatsApi(api_client)

    try:
        # Get my Account statistics
        api_response = await api_instance.get_my_stats()
        print("The response of AccountStatsApi->get_my_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStatsApi->get_my_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountStats**](AccountStats.md)

### Authorization

[OAuth2](../README.md#OAuth2), [ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

