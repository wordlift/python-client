# wordlift_client.ContentGenerationSyncsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sync1**](ContentGenerationSyncsApi.md#create_sync1) | **POST** /content-generations/{contentGenerationId}/syncs | Create


# **create_sync1**
> create_sync1(content_generation_id)

Create

### Example


```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.ContentGenerationSyncsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.

    try:
        # Create
        await api_instance.create_sync1(content_generation_id)
    except Exception as e:
        print("Exception when calling ContentGenerationSyncsApi->create_sync1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

