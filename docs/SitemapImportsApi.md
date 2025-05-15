# wordlift_client.SitemapImportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sitemap_import**](SitemapImportsApi.md#create_sitemap_import) | **POST** /sitemap-imports | Create


# **create_sitemap_import**
> List[str] create_sitemap_import(sitemap_import_request)

Create

Create a Sitemap Import

### Example


```python
import wordlift_client
from wordlift_client.models.sitemap_import_request import SitemapImportRequest
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
    api_instance = wordlift_client.SitemapImportsApi(api_client)
    sitemap_import_request = wordlift_client.SitemapImportRequest() # SitemapImportRequest | 

    try:
        # Create
        api_response = await api_instance.create_sitemap_import(sitemap_import_request)
        print("The response of SitemapImportsApi->create_sitemap_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitemapImportsApi->create_sitemap_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sitemap_import_request** | [**SitemapImportRequest**](SitemapImportRequest.md)|  | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

