# wordlift_client.AccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me**](AccountApi.md#get_me) | **GET** /accounts/me | Get


# **get_me**
> AccountInfo get_me()

Get

Get the account data for the current account identified by its key.

### Example


```python
import wordlift_client
from wordlift_client.models.account_info import AccountInfo
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
    api_instance = wordlift_client.AccountApi(api_client)

    try:
        # Get
        api_response = await api_instance.get_me()
        print("The response of AccountApi->get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.wordlift.account-info.v2+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

