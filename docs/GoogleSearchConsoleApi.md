# wordlift_client.GoogleSearchConsoleApi

All URIs are relative to *https://api.wordlift.io/quality-rating*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_website_search**](GoogleSearchConsoleApi.md#list_website_search) | **GET** /ext/google/searchconsole/searches | List Website Search data
[**list_websites**](GoogleSearchConsoleApi.md#list_websites) | **GET** /ext/google/searchconsole/websites | List


# **list_website_search**
> PageWebsiteSearch list_website_search(website, since, until, dimensions, google_access_token, cursor=cursor, limit=limit)

List Website Search data

List the Website Search performance data

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.page_website_search import PageWebsiteSearch
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
    api_instance = wordlift_client.GoogleSearchConsoleApi(api_client)
    website = 'website_example' # str | The website URL
    since = 'since_example' # str | The start date, inclusive, in yyyy-MM-dd format.
    until = 'until_example' # str | The end date, inclusive, in yyyy-MM-dd format.
    dimensions = ['dimensions_example'] # List[str] | The dimensions, e.g. `query`, `page`. Must repeat for each dimension.
    google_access_token = 'google_access_token_example' # str | The Google access token, must have access to the Google Search Console scope
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)

    try:
        # List Website Search data
        api_response = await api_instance.list_website_search(website, since, until, dimensions, google_access_token, cursor=cursor, limit=limit)
        print("The response of GoogleSearchConsoleApi->list_website_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleSearchConsoleApi->list_website_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| The website URL | 
 **since** | **str**| The start date, inclusive, in yyyy-MM-dd format. | 
 **until** | **str**| The end date, inclusive, in yyyy-MM-dd format. | 
 **dimensions** | [**List[str]**](str.md)| The dimensions, e.g. &#x60;query&#x60;, &#x60;page&#x60;. Must repeat for each dimension. | 
 **google_access_token** | **str**| The Google access token, must have access to the Google Search Console scope | 
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]

### Return type

[**PageWebsiteSearch**](PageWebsiteSearch.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_websites**
> PageWebsite list_websites(google_access_token, limit=limit)

List

List the Websites

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.page_website import PageWebsite
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
    api_instance = wordlift_client.GoogleSearchConsoleApi(api_client)
    google_access_token = 'google_access_token_example' # str | The Google access token, must have access to the Google Search Console scope
    limit = 10 # int | The maximum number of results (optional) (default to 10)

    try:
        # List
        api_response = await api_instance.list_websites(google_access_token, limit=limit)
        print("The response of GoogleSearchConsoleApi->list_websites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleSearchConsoleApi->list_websites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_access_token** | **str**| The Google access token, must have access to the Google Search Console scope | 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]

### Return type

[**PageWebsite**](PageWebsite.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

