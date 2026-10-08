# wordlift_client.ResolveApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolve_mentions**](ResolveApi.md#resolve_mentions) | **POST** /resolve | Resolve mentions


# **resolve_mentions**
> ResolveResponse resolve_mentions(resolve_request)

Resolve mentions

Resolve mentions to identities in `dataset_uri`, or return unresolved.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.resolve_request import ResolveRequest
from wordlift_client.models.resolve_response import ResolveResponse
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
    api_instance = wordlift_client.ResolveApi(api_client)
    resolve_request = wordlift_client.ResolveRequest() # ResolveRequest | 

    try:
        # Resolve mentions
        api_response = await api_instance.resolve_mentions(resolve_request)
        print("The response of ResolveApi->resolve_mentions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolveApi->resolve_mentions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolve_request** | [**ResolveRequest**](ResolveRequest.md)|  | 

### Return type

[**ResolveResponse**](ResolveResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Wordlift-Consumption - The request&#39;s cost in smart credits: one per request plus one per 1,000 characters of text. <br>  * X-RateLimit-Limit - Monthly allowance of the account for resolve(). <br>  * X-RateLimit-Remaining - Credits left in the current period. <br>  * X-RateLimit-Reset - Seconds until the allowance resets. <br>  |
**401** | Missing or invalid WordLift API key. |  -  |
**422** | Validation Error |  -  |
**429** | The account&#39;s monthly allowance for resolve() is spent. Nothing was resolved. |  * X-RateLimit-Limit - Monthly allowance of the account for resolve(). <br>  * X-RateLimit-Remaining - Credits left in the current period. <br>  * X-RateLimit-Reset - Seconds until the allowance resets. <br>  |
**503** | The engine is loading the account&#39;s knowledge graph (&#x60;dataset_warming&#x60;); retry after the seconds given. |  * Retry-After - Seconds to wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

