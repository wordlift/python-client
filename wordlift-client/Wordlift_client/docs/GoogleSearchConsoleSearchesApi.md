# Wordlift_client.GoogleSearchConsoleSearchesApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_website_search1**](GoogleSearchConsoleSearchesApi.md#list_website_search1) | **GET** /accounts/me/google/searches | List Website Search data


# **list_website_search1**
> PageWebsiteSearch list_website_search1(since, until, dimensions, cursor=cursor, data_state=data_state, limit=limit)

List Website Search data

List the Website Search performance data

### Example

* Api Key Authentication (ApiKey):

```python
import Wordlift_client
from Wordlift_client.models.page_website_search import PageWebsiteSearch
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
    api_instance = Wordlift_client.GoogleSearchConsoleSearchesApi(api_client)
    since = 'since_example' # str | The start date, inclusive, in yyyy-MM-dd format.
    until = 'until_example' # str | The end date, inclusive, in yyyy-MM-dd format.
    dimensions = ['dimensions_example'] # List[str] | The dimensions, e.g. `query`, `page`. Must repeat for each dimension.
    cursor = 'cursor_example' # str | The cursor (optional)
    data_state = 'data_state_example' # str | If \"all\" (case-insensitive), data will include fresh data. If \"final\" (case-insensitive) or if this parameter is omitted, the returned data will include only finalized data. (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)

    try:
        # List Website Search data
        api_response = await api_instance.list_website_search1(since, until, dimensions, cursor=cursor, data_state=data_state, limit=limit)
        print("The response of GoogleSearchConsoleSearchesApi->list_website_search1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleSearchConsoleSearchesApi->list_website_search1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**| The start date, inclusive, in yyyy-MM-dd format. | 
 **until** | **str**| The end date, inclusive, in yyyy-MM-dd format. | 
 **dimensions** | [**List[str]**](str.md)| The dimensions, e.g. &#x60;query&#x60;, &#x60;page&#x60;. Must repeat for each dimension. | 
 **cursor** | **str**| The cursor | [optional] 
 **data_state** | **str**| If \&quot;all\&quot; (case-insensitive), data will include fresh data. If \&quot;final\&quot; (case-insensitive) or if this parameter is omitted, the returned data will include only finalized data. | [optional] 
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

