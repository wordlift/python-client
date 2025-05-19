# wordlift_client.ContentGenerationStatsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get3**](ContentGenerationStatsApi.md#get3) | **GET** /content-generations/{contentGenerationId}/stats | Get


# **get3**
> ContentGenerationStats get3(content_generation_id)

Get

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.content_generation_stats import ContentGenerationStats
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
    api_instance = wordlift_client.ContentGenerationStatsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.

    try:
        # Get
        api_response = await api_instance.get3(content_generation_id)
        print("The response of ContentGenerationStatsApi->get3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationStatsApi->get3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 

### Return type

[**ContentGenerationStats**](ContentGenerationStats.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

