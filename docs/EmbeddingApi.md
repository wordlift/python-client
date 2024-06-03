# wordlift_client.EmbeddingApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_embedding**](EmbeddingApi.md#create_embedding) | **POST** /kg/embeddings | Create


# **create_embedding**
> List[Dict[str, str]] create_embedding(embedding_request)

Create

Create the embedding for the IRIs for the provided query.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.embedding_request import EmbeddingRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
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
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.EmbeddingApi(api_client)
    embedding_request = wordlift_client.EmbeddingRequest() # EmbeddingRequest | 

    try:
        # Create
        api_response = await api_instance.create_embedding(embedding_request)
        print("The response of EmbeddingApi->create_embedding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddingApi->create_embedding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embedding_request** | [**EmbeddingRequest**](EmbeddingRequest.md)|  | 

### Return type

**List[Dict[str, str]]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

