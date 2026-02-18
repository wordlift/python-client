# wordlift_client.WebPageScrapeApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web_page_scrape**](WebPageScrapeApi.md#create_web_page_scrape) | **POST** /web-page-scrapes | Web Page Scrape


# **create_web_page_scrape**
> WebPageScrapeResponse create_web_page_scrape(web_page_scrape_request)

Web Page Scrape

Scrape a Web Page.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.web_page_scrape_request import WebPageScrapeRequest
from wordlift_client.models.web_page_scrape_response import WebPageScrapeResponse
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
    api_instance = wordlift_client.WebPageScrapeApi(api_client)
    web_page_scrape_request = wordlift_client.WebPageScrapeRequest() # WebPageScrapeRequest | 

    try:
        # Web Page Scrape
        api_response = await api_instance.create_web_page_scrape(web_page_scrape_request)
        print("The response of WebPageScrapeApi->create_web_page_scrape:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebPageScrapeApi->create_web_page_scrape: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_page_scrape_request** | [**WebPageScrapeRequest**](WebPageScrapeRequest.md)|  | 

### Return type

[**WebPageScrapeResponse**](WebPageScrapeResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web Page Scrape Response |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

