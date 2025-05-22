# wordlift_client.WebPagesImportsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web_page_imports**](WebPagesImportsApi.md#create_web_page_imports) | **POST** /web-page-imports | Create


# **create_web_page_imports**
> WebPageImportResponse create_web_page_imports(web_page_import_request)

Create

Create a Web Page Import

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.web_page_import_request import WebPageImportRequest
from wordlift_client.models.web_page_import_response import WebPageImportResponse
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
    api_instance = wordlift_client.WebPagesImportsApi(api_client)
    web_page_import_request = wordlift_client.WebPageImportRequest() # WebPageImportRequest | 

    try:
        # Create
        api_response = await api_instance.create_web_page_imports(web_page_import_request)
        print("The response of WebPagesImportsApi->create_web_page_imports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPagesImportsApi->create_web_page_imports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_page_import_request** | [**WebPageImportRequest**](WebPageImportRequest.md)|  | 

### Return type

[**WebPageImportResponse**](WebPageImportResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

