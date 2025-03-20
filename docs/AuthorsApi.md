# wordlift_client.AuthorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_author**](AuthorsApi.md#create_author) | **POST** /data/authors | Create


# **create_author**
> str create_author(author_request)

Create

Creates the structured data for an author.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.author_request import AuthorRequest
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
    api_instance = wordlift_client.AuthorsApi(api_client)
    author_request = wordlift_client.AuthorRequest() # AuthorRequest | 

    try:
        # Create
        api_response = await api_instance.create_author(author_request)
        print("The response of AuthorsApi->create_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorsApi->create_author: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_request** | [**AuthorRequest**](AuthorRequest.md)|  | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/ld+json, application/n-triples, application/rdf+xml, text/turtle

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

