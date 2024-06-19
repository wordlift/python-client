# wordlift_client.SummarizationsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**microdata_to_json_ld_using_post**](SummarizationsApi.md#microdata_to_json_ld_using_post) | **POST** /summarize | Create


# **microdata_to_json_ld_using_post**
> Dict[str, str] microdata_to_json_ld_using_post(body, max_length=max_length, min_length=min_length, ratio=ratio)

Create

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import wordlift_client
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.SummarizationsApi(api_client)
    body = 'body_example' # str | body
    max_length = 500 # int | Maximum text length (optional) (default to 500)
    min_length = 25 # int | Minimum text length (optional) (default to 25)
    ratio = 0.2 # float | Ratio (optional) (default to 0.2)

    try:
        # Create
        api_response = await api_instance.microdata_to_json_ld_using_post(body, max_length=max_length, min_length=min_length, ratio=ratio)
        print("The response of SummarizationsApi->microdata_to_json_ld_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizationsApi->microdata_to_json_ld_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| body | 
 **max_length** | **int**| Maximum text length | [optional] [default to 500]
 **min_length** | **int**| Minimum text length | [optional] [default to 25]
 **ratio** | **float**| Ratio | [optional] [default to 0.2]

### Return type

**Dict[str, str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/ld+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

