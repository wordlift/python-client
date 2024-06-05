# wordlift_client.ContentGenerationFieldsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_fields**](ContentGenerationFieldsApi.md#list_fields) | **GET** /content-generations/{contentGenerationId}/fields | List
[**list_fields_for_graph_ql_query**](ContentGenerationFieldsApi.md#list_fields_for_graph_ql_query) | **POST** /fields | List for GraphQl Query


# **list_fields**
> PageField list_fields(content_generation_id, cursor=cursor, limit=limit)

List

### Example


```python
import wordlift_client
from wordlift_client.models.page_field import PageField
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.ContentGenerationFieldsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)

    try:
        # List
        api_response = await api_instance.list_fields(content_generation_id, cursor=cursor, limit=limit)
        print("The response of ContentGenerationFieldsApi->list_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationFieldsApi->list_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]

### Return type

[**PageField**](PageField.md)

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

# **list_fields_for_graph_ql_query**
> List[ModelField] list_fields_for_graph_ql_query(body)

List for GraphQl Query

### Example


```python
import wordlift_client
from wordlift_client.models.model_field import ModelField
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.ContentGenerationFieldsApi(api_client)
    body = 'body_example' # str | 

    try:
        # List for GraphQl Query
        api_response = await api_instance.list_fields_for_graph_ql_query(body)
        print("The response of ContentGenerationFieldsApi->list_fields_for_graph_ql_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationFieldsApi->list_fields_for_graph_ql_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**List[ModelField]**](ModelField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/graphql
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

