# wordlift_client.EmbeddingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_embeddings**](EmbeddingsApi.md#create_embeddings) | **POST** /api/embeddings | Create Embeddings


# **create_embeddings**
> create_embeddings(create_embeddings_input)

Create Embeddings

Create Embeddings

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.create_embeddings_input import CreateEmbeddingsInput
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.EmbeddingsApi(api_client)
    create_embeddings_input = wordlift_client.CreateEmbeddingsInput() # CreateEmbeddingsInput | 

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

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

