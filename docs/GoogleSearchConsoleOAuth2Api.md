# wordlift_client.GoogleSearchConsoleOAuth2Api

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_code_exchange**](GoogleSearchConsoleOAuth2Api.md#create_auth_code_exchange) | **POST** /google-search-console/oauth2/auth-code-exchanges | Get an Access Code
[**create_authorize_uri**](GoogleSearchConsoleOAuth2Api.md#create_authorize_uri) | **POST** /google-search-console/oauth2/authorize-uris | Create an Authorization URI


# **create_auth_code_exchange**
> ExchangeAuthCodeResponse create_auth_code_exchange(exchange_auth_code_request)

Get an Access Code

Call this API to have the Platform receive an Authentication Token to access the Analytics data via Google Search Console.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.exchange_auth_code_request import ExchangeAuthCodeRequest
from wordlift_client.models.exchange_auth_code_response import ExchangeAuthCodeResponse
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
    api_instance = wordlift_client.GoogleSearchConsoleOAuth2Api(api_client)
    exchange_auth_code_request = wordlift_client.ExchangeAuthCodeRequest() # ExchangeAuthCodeRequest | 

    try:
        # Get an Access Code
        api_response = await api_instance.create_auth_code_exchange(exchange_auth_code_request)
        print("The response of GoogleSearchConsoleOAuth2Api->create_auth_code_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleSearchConsoleOAuth2Api->create_auth_code_exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_auth_code_request** | [**ExchangeAuthCodeRequest**](ExchangeAuthCodeRequest.md)|  | 

### Return type

[**ExchangeAuthCodeResponse**](ExchangeAuthCodeResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorize_uri**
> BuildAuthorizeUriResponse create_authorize_uri(build_authorize_uri_request)

Create an Authorization URI

Call this API to get an authorization URI needed to interactively get an authorization token. Then call the `exchangeAuthCode` to exchange it with an authorization token.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.build_authorize_uri_request import BuildAuthorizeUriRequest
from wordlift_client.models.build_authorize_uri_response import BuildAuthorizeUriResponse
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
    api_instance = wordlift_client.GoogleSearchConsoleOAuth2Api(api_client)
    build_authorize_uri_request = wordlift_client.BuildAuthorizeUriRequest() # BuildAuthorizeUriRequest | 

    try:
        # Create an Authorization URI
        api_response = await api_instance.create_authorize_uri(build_authorize_uri_request)
        print("The response of GoogleSearchConsoleOAuth2Api->create_authorize_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleSearchConsoleOAuth2Api->create_authorize_uri: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_authorize_uri_request** | [**BuildAuthorizeUriRequest**](BuildAuthorizeUriRequest.md)|  | 

### Return type

[**BuildAuthorizeUriResponse**](BuildAuthorizeUriResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

