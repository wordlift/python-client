# wordlift_client.VectorSearchQuestionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vector_search_question**](VectorSearchQuestionsApi.md#create_vector_search_question) | **POST** /vector-search/questions-collection | Create


# **create_vector_search_question**
> PageVectorSearchQuestionResponseItem create_vector_search_question(vector_search_question_request)

Create

### Example


```python
import wordlift_client
from wordlift_client.models.page_vector_search_question_response_item import PageVectorSearchQuestionResponseItem
from wordlift_client.models.vector_search_question_request import VectorSearchQuestionRequest
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

No authorization required

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

