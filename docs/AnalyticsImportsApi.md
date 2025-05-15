# wordlift_client.AnalyticsImportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_analytics_import**](AnalyticsImportsApi.md#create_analytics_import) | **POST** /analytics-imports | Create


# **create_analytics_import**
> List[Dict[str, str]] create_analytics_import(analytics_import_request)

Create

Create a Analytics Import using Google Search Console or Botify depending on the Account configuration.

### Example


```python
import wordlift_client
from wordlift_client.models.analytics_import_request import AnalyticsImportRequest
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
    api_instance = wordlift_client.AnalyticsImportsApi(api_client)
    analytics_import_request = wordlift_client.AnalyticsImportRequest() # AnalyticsImportRequest | 

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

