# wordlift_client.PluginDiagnosticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_diagnostic_plugin_collection**](PluginDiagnosticsApi.md#update_diagnostic_plugin_collection) | **PUT** /accounts/me/plugin/diagnostics/plugins-collection | Update


# **update_diagnostic_plugin_collection**
> update_diagnostic_plugin_collection(account, diagnostic_plugin_request)

Update

Replace the list of the plugins for the current account with the one provided by the client

### Example


```python
import wordlift_client
from wordlift_client.models.account import Account
from wordlift_client.models.diagnostic_plugin_request import DiagnosticPluginRequest
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
    api_instance = wordlift_client.PluginDiagnosticsApi(api_client)
    account = wordlift_client.Account() # Account | 
    diagnostic_plugin_request = [wordlift_client.DiagnosticPluginRequest()] # List[DiagnosticPluginRequest] | 

    try:
        # Update
        await api_instance.update_diagnostic_plugin_collection(account, diagnostic_plugin_request)
    except Exception as e:
        print("Exception when calling PluginDiagnosticsApi->update_diagnostic_plugin_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account**](.md)|  | 
 **diagnostic_plugin_request** | [**List[DiagnosticPluginRequest]**](DiagnosticPluginRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**204** | No Content |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

