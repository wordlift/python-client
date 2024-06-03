# wordlift-client.ContentGenerationPresetsApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_presets**](ContentGenerationPresetsApi.md#list_presets) | **GET** /graphql-query-presets | List


# **list_presets**
> PagePreset list_presets(cursor=cursor, limit=limit)

List

### Example


```python
import wordlift-client
from wordlift-client.models.page_preset import PagePreset
from wordlift-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift-client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift-client.ContentGenerationPresetsApi(api_client)
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)

    try:
        # List
        api_response = await api_instance.list_presets(cursor=cursor, limit=limit)
        print("The response of ContentGenerationPresetsApi->list_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationPresetsApi->list_presets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]

### Return type

[**PagePreset**](PagePreset.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
