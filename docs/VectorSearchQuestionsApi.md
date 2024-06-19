# wordlift_client.VectorSearchQuestionsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vector_search_question**](VectorSearchQuestionsApi.md#create_vector_search_question) | **POST** /vector-search/questions-collection | Create


# **create_vector_search_question**
> PageVectorSearchQuestionResponseItem create_vector_search_question(vector_search_question_request)

Create

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import wordlift_client
from wordlift_client.models.page_vector_search_question_response_item import PageVectorSearchQuestionResponseItem
from wordlift_client.models.vector_search_question_request import VectorSearchQuestionRequest
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
    api_instance = wordlift_client.VectorSearchQuestionsApi(api_client)
    vector_search_question_request = wordlift_client.VectorSearchQuestionRequest() # VectorSearchQuestionRequest | 

    try:
        # Create
        api_response = await api_instance.create_vector_search_question(vector_search_question_request)
        print("The response of VectorSearchQuestionsApi->create_vector_search_question:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorSearchQuestionsApi->create_vector_search_question: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vector_search_question_request** | [**VectorSearchQuestionRequest**](VectorSearchQuestionRequest.md)|  | 

### Return type

[**PageVectorSearchQuestionResponseItem**](PageVectorSearchQuestionResponseItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

