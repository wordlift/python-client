# Wordlift_client.AnalyticsImportsApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_analytics_import**](AnalyticsImportsApi.md#create_analytics_import) | **POST** /analytics-imports | Create


# **create_analytics_import**
> List[Dict[str, str]] create_analytics_import(analytics_import_request)

Create

Create a Analytics Import using Google Search Console or Botify depending on the Account configuration.

### Example

* Api Key Authentication (ApiKey):

```python
import Wordlift_client
from Wordlift_client.models.analytics_import_request import AnalyticsImportRequest
from Wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = Wordlift_client.Configuration(
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
async with Wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Wordlift_client.AnalyticsImportsApi(api_client)
    analytics_import_request = Wordlift_client.AnalyticsImportRequest() # AnalyticsImportRequest | 

    try:
        # Create
        api_response = await api_instance.create_analytics_import(analytics_import_request)
        print("The response of AnalyticsImportsApi->create_analytics_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsImportsApi->create_analytics_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analytics_import_request** | [**AnalyticsImportRequest**](AnalyticsImportRequest.md)|  | 

### Return type

**List[Dict[str, str]]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

