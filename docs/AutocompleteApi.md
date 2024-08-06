# wordlift_client.AutocompleteApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get1**](AutocompleteApi.md#get1) | **GET** /autocomplete | Get


# **get1**
> AutocompleteResult get1(query, language, scope=scope, limit=limit, exclude=exclude)

Get

The autocomplete endpoint suggests entities from Linked Data that match the provided query.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.autocomplete_result import AutocompleteResult
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
    api_instance = wordlift_client.AutocompleteApi(api_client)
    query = 'query_example' # str | Autocomplete query
    language = 'language_example' # str | 2-letter language code, e.g. 'en'.
    scope = 'cloud' # str | Scope (optional) (default to 'cloud')
    limit = '10' # str | Maximum number of results. By default 10. (optional) (default to '10')
    exclude = ['exclude_example'] # List[str] | List of entity URIs to exclude. (optional)

    try:
        # Get
        api_response = await api_instance.get1(query, language, scope=scope, limit=limit, exclude=exclude)
        print("The response of AutocompleteApi->get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->get1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Autocomplete query | 
 **language** | **str**| 2-letter language code, e.g. &#39;en&#39;. | 
 **scope** | **str**| Scope | [optional] [default to &#39;cloud&#39;]
 **limit** | **str**| Maximum number of results. By default 10. | [optional] [default to &#39;10&#39;]
 **exclude** | [**List[str]**](str.md)| List of entity URIs to exclude. | [optional] 

### Return type

[**AutocompleteResult**](AutocompleteResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

