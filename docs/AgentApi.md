# wordlift_client.AgentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ask_request_api_ask_post**](AgentApi.md#ask_request_api_ask_post) | **POST** /ask | Ask Request


# **ask_request_api_ask_post**
> AskResponse ask_request_api_ask_post(ask_request)

Ask Request

Interact with the WordLift Agent to process a message and receive an AI-driven response.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.ask_request import AskRequest
from wordlift_client.models.ask_response import AskResponse
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
    api_instance = wordlift_client.AgentApi(api_client)
    ask_request = wordlift_client.AskRequest() # AskRequest | 

    try:
        # Ask Request
        api_response = await api_instance.ask_request_api_ask_post(ask_request)
        print("The response of AgentApi->ask_request_api_ask_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->ask_request_api_ask_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ask_request** | [**AskRequest**](AskRequest.md)|  | 

### Return type

[**AskResponse**](AskResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

