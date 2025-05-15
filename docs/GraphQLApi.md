# wordlift_client.GraphQLApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graphql_using_post**](GraphQLApi.md#graphql_using_post) | **POST** /graphql | Query


# **graphql_using_post**
> Dict[str, object] graphql_using_post(body)

Query

### Example


```python
import wordlift_client
from wordlift_client.models.graphql_request import GraphqlRequest
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
    api_instance = wordlift_client.GraphQLApi(api_client)
    body = wordlift_client.GraphqlRequest() # GraphqlRequest | body

    try:
        # Query
        api_response = await api_instance.graphql_using_post(body)
        print("The response of GraphQLApi->graphql_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLApi->graphql_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GraphqlRequest**](GraphqlRequest.md)| body | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

