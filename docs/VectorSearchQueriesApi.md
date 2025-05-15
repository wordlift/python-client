# wordlift_client.VectorSearchQueriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_query**](VectorSearchQueriesApi.md#create_query) | **POST** /vector-search/queries | Create


# **create_query**
> PageVectorSearchQueryResponseItem create_query(vector_search_query_request)

Create

### Example


```python
import wordlift_client
from wordlift_client.models.page_vector_search_query_response_item import PageVectorSearchQueryResponseItem
from wordlift_client.models.vector_search_query_request import VectorSearchQueryRequest
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
    api_instance = wordlift_client.VectorSearchQueriesApi(api_client)
    vector_search_query_request = wordlift_client.VectorSearchQueryRequest() # VectorSearchQueryRequest | 

    try:
        # Create
        api_response = await api_instance.create_query(vector_search_query_request)
        print("The response of VectorSearchQueriesApi->create_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VectorSearchQueriesApi->create_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vector_search_query_request** | [**VectorSearchQueryRequest**](VectorSearchQueryRequest.md)|  | 

### Return type

[**PageVectorSearchQueryResponseItem**](PageVectorSearchQueryResponseItem.md)

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

