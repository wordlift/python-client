# Wordlift_client.ContentGenerationStatsApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](ContentGenerationStatsApi.md#get) | **GET** /content-generations/{contentGenerationId}/stats | Get


# **get**
> ContentGenerationStats get(content_generation_id)

Get

### Example


```python
import Wordlift_client
from Wordlift_client.models.content_generation_stats import ContentGenerationStats
from Wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = Wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with Wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Wordlift_client.ContentGenerationStatsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.

    try:
        # Get
        api_response = await api_instance.get(content_generation_id)
        print("The response of ContentGenerationStatsApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationStatsApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 

### Return type

[**ContentGenerationStats**](ContentGenerationStats.md)

### Authorization

No authorization required

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

