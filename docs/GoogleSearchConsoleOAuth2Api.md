# wordlift_client.GoogleSearchConsoleOAuth2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_code_exchange**](GoogleSearchConsoleOAuth2Api.md#create_auth_code_exchange) | **POST** /google-search-console/oauth2/auth-code-exchanges | Get an Access Code
[**create_authorize_uri**](GoogleSearchConsoleOAuth2Api.md#create_authorize_uri) | **POST** /google-search-console/oauth2/authorize-uris | Create an Authorization URI
[**delete_authorization**](GoogleSearchConsoleOAuth2Api.md#delete_authorization) | **DELETE** /google-search-console/authorization | Delete an authorization
[**duplicate**](GoogleSearchConsoleOAuth2Api.md#duplicate) | **POST** /google-search-console/authorize/duplicate | Duplicate the Google Search Console connection through accounts
[**get_authorizations**](GoogleSearchConsoleOAuth2Api.md#get_authorizations) | **GET** /google-search-console/authorizations | Get the authorizations
[**login**](GoogleSearchConsoleOAuth2Api.md#login) | **GET** /google-search-console/authorize/init | Login to the Google Search Console API client


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
 - **Accept**: application/json

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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization**
> delete_authorization()

Delete an authorization

Retrieve the authorizations of the authenticated user.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
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
    api_instance = wordlift_client.GoogleSearchConsoleOAuth2Api(api_client)

    try:
        # Delete an authorization
        await api_instance.delete_authorization()
    except Exception as e:
        print("Exception when calling GoogleSearchConsoleOAuth2Api->delete_authorization: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Authorization of the account authenticated is deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate**
> object duplicate(duplicate_authorization_request)

Duplicate the Google Search Console connection through accounts

Call this API to duplicate an existing google search console connection to another accounts.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.duplicate_authorization_request import DuplicateAuthorizationRequest
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
    api_instance = wordlift_client.GoogleSearchConsoleOAuth2Api(api_client)
    duplicate_authorization_request = wordlift_client.DuplicateAuthorizationRequest() # DuplicateAuthorizationRequest | 

    try:
        # Duplicate the Google Search Console connection through accounts
        api_response = await api_instance.duplicate(duplicate_authorization_request)
        print("The response of GoogleSearchConsoleOAuth2Api->duplicate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleSearchConsoleOAuth2Api->duplicate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duplicate_authorization_request** | [**DuplicateAuthorizationRequest**](DuplicateAuthorizationRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The connection has been duplicated |  -  |
**422** | The account keys are invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorizations**
> List[Authorization] get_authorizations(account_key=account_key)

Get the authorizations

Retrieve the authorizations of the authenticated user.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.authorization import Authorization
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
    api_instance = wordlift_client.GoogleSearchConsoleOAuth2Api(api_client)
    account_key = ['account_key_example'] # List[str] |  (optional)

    try:
        # Get the authorizations
        api_response = await api_instance.get_authorizations(account_key=account_key)
        print("The response of GoogleSearchConsoleOAuth2Api->get_authorizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleSearchConsoleOAuth2Api->get_authorizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_key** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Authorization]**](Authorization.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authorizations of the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> login(account_key, redirect_uri, state=state)

Login to the Google Search Console API client

Call this API to go to the login page of the Google Search Console.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
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
    api_instance = wordlift_client.GoogleSearchConsoleOAuth2Api(api_client)
    account_key = 'account_key_example' # str | The account key
    redirect_uri = 'redirect_uri_example' # str | The redirect URI to redirect to after the login
    state = 'state_example' # str | The state to maintain after authorize. (optional)

    try:
        # Login to the Google Search Console API client
        await api_instance.login(account_key, redirect_uri, state=state)
    except Exception as e:
        print("Exception when calling GoogleSearchConsoleOAuth2Api->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_key** | **str**| The account key | 
 **redirect_uri** | **str**| The redirect URI to redirect to after the login | 
 **state** | **str**| The state to maintain after authorize. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**307** | Redirect to redirectUri value |  * Location - Redirect to google login page <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

