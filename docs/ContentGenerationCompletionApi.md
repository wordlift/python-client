# wordlift_client.ContentGenerationCompletionApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_completion**](ContentGenerationCompletionApi.md#create_completion) | **POST** /completions | Create a completion


# **create_completion**
> str create_completion(completion_request)

Create a completion

[GET with body payload](https://opensource.zalando.com/restful-api-guidelines/#get-with-body) - no resources created

### Example


```python
import wordlift_client
from wordlift_client.models.completion_request import CompletionRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.ContentGenerationCompletionApi(api_client)
    completion_request = wordlift_client.CompletionRequest() # CompletionRequest | 

    try:
        # Create a completion
        api_response = await api_instance.create_completion(completion_request)
        print("The response of ContentGenerationCompletionApi->create_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationCompletionApi->create_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **completion_request** | [**CompletionRequest**](CompletionRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

