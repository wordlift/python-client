# wordlift_client.BotifyCrawlImportsApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_botify_crawl_import**](BotifyCrawlImportsApi.md#create_botify_crawl_import) | **POST** /botify-crawl-imports | Create


# **create_botify_crawl_import**
> List[WebPage] create_botify_crawl_import(botify_crawl_import_request)

Create

Create a Botify Crawl Import

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.botify_crawl_import_request import BotifyCrawlImportRequest
from wordlift_client.models.web_page import WebPage
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
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
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.BotifyCrawlImportsApi(api_client)
    botify_crawl_import_request = wordlift_client.BotifyCrawlImportRequest() # BotifyCrawlImportRequest | 

    try:
        # Create
        api_response = await api_instance.create_botify_crawl_import(botify_crawl_import_request)
        print("The response of BotifyCrawlImportsApi->create_botify_crawl_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BotifyCrawlImportsApi->create_botify_crawl_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **botify_crawl_import_request** | [**BotifyCrawlImportRequest**](BotifyCrawlImportRequest.md)|  | 

### Return type

[**List[WebPage]**](WebPage.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

