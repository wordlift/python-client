# wordlift_client.AddOnsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_configurations**](AddOnsApi.md#list_configurations) | **GET** /addon/configurations | List


# **list_configurations**
> PageAddOnConfiguration list_configurations(token=token, key=key, limit=limit)

List

List the Add-ons configurations

### Example


```python
import wordlift_client
from wordlift_client.models.page_add_on_configuration import PageAddOnConfiguration
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AddOnsApi(api_client)
    token = 'token_example' # str | The access token (optional)
    key = 'key_example' # str | The key (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)

    try:
        # List
        api_response = await api_instance.list_configurations(token=token, key=key, limit=limit)
        print("The response of AddOnsApi->list_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddOnsApi->list_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The access token | [optional] 
 **key** | **str**| The key | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]

### Return type

[**PageAddOnConfiguration**](PageAddOnConfiguration.md)

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

