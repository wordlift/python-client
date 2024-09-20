# wordlift_client.SitemapImportsApi

All URIs are relative to *https://api.wordlift.io/quality-rating*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sitemap_import**](SitemapImportsApi.md#create_sitemap_import) | **POST** /sitemap-imports | Create


# **create_sitemap_import**
> create_sitemap_import(sitemap_import_request)

Create

Create a Sitemap Import

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.sitemap_import_request import SitemapImportRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/quality-rating
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/quality-rating"
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
    api_instance = wordlift_client.SitemapImportsApi(api_client)
    sitemap_import_request = wordlift_client.SitemapImportRequest() # SitemapImportRequest | 

    try:
        # Create
        await api_instance.create_sitemap_import(sitemap_import_request)
    except Exception as e:
        print("Exception when calling SitemapImportsApi->create_sitemap_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sitemap_import_request** | [**SitemapImportRequest**](SitemapImportRequest.md)|  | 

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
**200** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

