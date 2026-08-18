# wordlift_client.MonitorChecksApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_checks_checks_get**](MonitorChecksApi.md#list_checks_checks_get) | **GET** /checks | List Checks


# **list_checks_checks_get**
> List[MonitorCheckName] list_checks_checks_get()

List Checks

List check identifiers — stable ids, not display labels; the UI maps them to its own labels/i18n. Deployment metadata, not tenant data, so the endpoint is unauthenticated like ``/health``.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.monitor_check_name import MonitorCheckName
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
    api_instance = wordlift_client.MonitorChecksApi(api_client)

    try:
        # List Checks
        api_response = await api_instance.list_checks_checks_get()
        print("The response of MonitorChecksApi->list_checks_checks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorChecksApi->list_checks_checks_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MonitorCheckName]**](MonitorCheckName.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

