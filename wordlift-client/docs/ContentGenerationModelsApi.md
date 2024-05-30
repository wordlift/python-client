# Wordlift_client.ContentGenerationModelsApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_models**](ContentGenerationModelsApi.md#list_models) | **GET** /models | List


# **list_models**
> PageModel list_models(cursor=cursor, limit=limit)

List

### Example


```python
import Wordlift_client
from Wordlift_client.models.page_model import PageModel
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
    api_instance = Wordlift_client.ContentGenerationModelsApi(api_client)
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)

    try:
        # List
        api_response = await api_instance.list_models(cursor=cursor, limit=limit)
        print("The response of ContentGenerationModelsApi->list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationModelsApi->list_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]

### Return type

[**PageModel**](PageModel.md)

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

