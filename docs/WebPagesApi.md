# wordlift_client.WebPagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_web_page**](WebPagesApi.md#get_web_page) | **GET** /web-pages | Get


# **get_web_page**
> WebPage get_web_page(url)

Get

Get extracted web page content

### Example


```python
import wordlift_client
from wordlift_client.models.web_page import WebPage
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
    api_instance = wordlift_client.WebPagesApi(api_client)
    url = 'url_example' # str | Url to extract

    try:
        # Get
        api_response = await api_instance.get_web_page(url)
        print("The response of WebPagesApi->get_web_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPagesApi->get_web_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Url to extract | 

### Return type

[**WebPage**](WebPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

