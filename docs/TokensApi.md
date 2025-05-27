# wordlift_client.TokensApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token**](TokensApi.md#get_token) | **GET** /tokens | Get


# **get_token**
> TokenResponse get_token(registration_id)

Get

Get a token

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.token_response import TokenResponse
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
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
    api_instance = wordlift_client.TokensApi(api_client)
    registration_id = 'google-search-console' # str | The registration id

    try:
        # Get
        api_response = await api_instance.get_token(registration_id)
        print("The response of TokensApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokensApi->get_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The registration id | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

