# wordlift-client.GraphQLApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graphql_using_post**](GraphQLApi.md#graphql_using_post) | **POST** /graphql | Query


# **graphql_using_post**
> Dict[str, object] graphql_using_post(body)

Query

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift-client
from wordlift-client.models.graphql_request import GraphqlRequest
from wordlift-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift-client.Configuration(
    host = "https://api.wordlift.io/analysis"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift-client.GraphQLApi(api_client)
    body = wordlift-client.GraphqlRequest() # GraphqlRequest | body

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

[ApiKey](../README.md#ApiKey)

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

