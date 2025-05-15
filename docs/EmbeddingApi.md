# wordlift_client.EmbeddingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_embedding**](EmbeddingApi.md#create_embedding) | **POST** /kg/embeddings | Create


# **create_embedding**
> List[Dict[str, str]] create_embedding(kg_embedding_request)

Create

Create the embedding for the IRIs for the provided query.

### Example


```python
import wordlift_client
from wordlift_client.models.kg_embedding_request import KgEmbeddingRequest
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
    api_instance = wordlift_client.EmbeddingApi(api_client)
    kg_embedding_request = wordlift_client.KgEmbeddingRequest() # KgEmbeddingRequest | 

    try:
        # Create
        api_response = await api_instance.create_embedding(kg_embedding_request)
        print("The response of EmbeddingApi->create_embedding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddingApi->create_embedding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kg_embedding_request** | [**KgEmbeddingRequest**](KgEmbeddingRequest.md)|  | 

### Return type

**List[Dict[str, str]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

