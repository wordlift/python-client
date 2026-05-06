# wordlift_client.FetchApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_page_fetch_get**](FetchApi.md#fetch_page_fetch_get) | **GET** /crawler/fetch | Fetch a single page


# **fetch_page_fetch_get**
> FetchResponse fetch_page_fetch_get(url, js_render_mode=js_render_mode, force=force, proxy_mode=proxy_mode)

Fetch a single page

Fetches a URL synchronously and returns its content.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.fetch_js_render_mode import FetchJsRenderMode
from wordlift_client.models.fetch_response import FetchResponse
from wordlift_client.models.proxy_mode import ProxyMode
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
    api_instance = wordlift_client.FetchApi(api_client)
    url = 'url_example' # str | The URL to fetch. Must be an HTML or text page; binary resource URLs (PDFs, images, archives, media, fonts, stylesheets) are rejected.
    js_render_mode = wordlift_client.FetchJsRenderMode() # FetchJsRenderMode | JS rendering mode: auto lets the system decide, disabled forces static fetch, enabled forces JS rendering. (optional)
    force = False # bool | When true, bypasses the result cache and forces a fresh fetch. (optional) (default to False)
    proxy_mode = wordlift_client.ProxyMode() # ProxyMode | Proxy mode to use for this fetch. (optional)

    try:
        # Fetch a single page
        api_response = await api_instance.fetch_page_fetch_get(url, js_render_mode=js_render_mode, force=force, proxy_mode=proxy_mode)
        print("The response of FetchApi->fetch_page_fetch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FetchApi->fetch_page_fetch_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| The URL to fetch. Must be an HTML or text page; binary resource URLs (PDFs, images, archives, media, fonts, stylesheets) are rejected. | 
 **js_render_mode** | [**FetchJsRenderMode**](.md)| JS rendering mode: auto lets the system decide, disabled forces static fetch, enabled forces JS rendering. | [optional] 
 **force** | **bool**| When true, bypasses the result cache and forces a fresh fetch. | [optional] [default to False]
 **proxy_mode** | [**ProxyMode**](.md)| Proxy mode to use for this fetch. | [optional] 

### Return type

[**FetchResponse**](FetchResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

