# Wordlift_client.EmbeddingsApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_embeddings**](EmbeddingsApi.md#create_embeddings) | **POST** /api/embeddings | Create Embeddings


# **create_embeddings**
> create_embeddings(create_embeddings_input)

Create Embeddings

Create Embeddings

### Example


```python
import Wordlift_client
from Wordlift_client.models.create_embeddings_input import CreateEmbeddingsInput
from Wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = Wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with Wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Wordlift_client.EmbeddingsApi(api_client)
    create_embeddings_input = Wordlift_client.CreateEmbeddingsInput() # CreateEmbeddingsInput | 

    try:
        # Create Embeddings
        await api_instance.create_embeddings(create_embeddings_input)
    except Exception as e:
        print("Exception when calling EmbeddingsApi->create_embeddings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_embeddings_input** | [**CreateEmbeddingsInput**](CreateEmbeddingsInput.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

