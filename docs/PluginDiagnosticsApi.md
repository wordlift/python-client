# wordlift-client.PluginDiagnosticsApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_diagnostic_plugin_collection**](PluginDiagnosticsApi.md#update_diagnostic_plugin_collection) | **PUT** /accounts/me/plugin/diagnostics/plugins-collection | Update


# **update_diagnostic_plugin_collection**
> update_diagnostic_plugin_collection(account, diagnostic_plugin_request)

Update

Replace the list of the plugins for the current account with the one provided by the client

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift-client
from wordlift-client.models.account import Account
from wordlift-client.models.diagnostic_plugin_request import DiagnosticPluginRequest
from wordlift-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift-client.Configuration(
    host = "https://api.wordlift.io/analysis"
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
async with wordlift-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift-client.PluginDiagnosticsApi(api_client)
    account = wordlift-client.Account() # Account | 
    diagnostic_plugin_request = [wordlift-client.DiagnosticPluginRequest()] # List[DiagnosticPluginRequest] | 

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

[ApiKey](../README.md#ApiKey)

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

