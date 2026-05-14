# wordlift_client.AccountChunksetsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account_chunkset**](AccountChunksetsApi.md#delete_account_chunkset) | **DELETE** /accounts/{account-id}/chunksets/{chunkset-slug} | Delete account chunkset
[**get_account_chunkset**](AccountChunksetsApi.md#get_account_chunkset) | **GET** /accounts/{account-id}/chunksets/{chunkset-slug} | Get account chunkset
[**list_account_chunksets**](AccountChunksetsApi.md#list_account_chunksets) | **GET** /accounts/{account-id}/chunksets | List account chunksets
[**put_account_chunkset**](AccountChunksetsApi.md#put_account_chunkset) | **PUT** /accounts/{account-id}/chunksets/{chunkset-slug} | Create or replace account chunkset


# **delete_account_chunkset**
> delete_account_chunkset(account_id, chunkset_slug)

Delete account chunkset

### Example

* OAuth Authentication (OAuth2):

```python
import wordlift_client
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountChunksetsApi(api_client)
    account_id = 56 # int | The account id
    chunkset_slug = 'chunkset_slug_example' # str | The chunkset slug

    try:
        # Delete account chunkset
        await api_instance.delete_account_chunkset(account_id, chunkset_slug)
    except Exception as e:
        print("Exception when calling AccountChunksetsApi->delete_account_chunkset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The account id | 
 **chunkset_slug** | **str**| The chunkset slug | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**401** | Authentication Failure |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**502** | Bad Gateway |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_chunkset**
> ChunksetResponse get_account_chunkset(account_id, chunkset_slug)

Get account chunkset

### Example

* OAuth Authentication (OAuth2):

```python
import wordlift_client
from wordlift_client.models.chunkset_response import ChunksetResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountChunksetsApi(api_client)
    account_id = 56 # int | The account id
    chunkset_slug = 'chunkset_slug_example' # str | The chunkset slug

    try:
        # Get account chunkset
        api_response = await api_instance.get_account_chunkset(account_id, chunkset_slug)
        print("The response of AccountChunksetsApi->get_account_chunkset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountChunksetsApi->get_account_chunkset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The account id | 
 **chunkset_slug** | **str**| The chunkset slug | 

### Return type

[**ChunksetResponse**](ChunksetResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**502** | Bad Gateway |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_chunksets**
> ChunksetListResponse list_account_chunksets(account_id)

List account chunksets

### Example

* OAuth Authentication (OAuth2):

```python
import wordlift_client
from wordlift_client.models.chunkset_list_response import ChunksetListResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountChunksetsApi(api_client)
    account_id = 56 # int | The account id

    try:
        # List account chunksets
        api_response = await api_instance.list_account_chunksets(account_id)
        print("The response of AccountChunksetsApi->list_account_chunksets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountChunksetsApi->list_account_chunksets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The account id | 

### Return type

[**ChunksetListResponse**](ChunksetListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**502** | Bad Gateway |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_account_chunkset**
> ChunksetResponse put_account_chunkset(account_id, chunkset_slug, chunkset_request)

Create or replace account chunkset

### Example

* OAuth Authentication (OAuth2):

```python
import wordlift_client
from wordlift_client.models.chunkset_request import ChunksetRequest
from wordlift_client.models.chunkset_response import ChunksetResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountChunksetsApi(api_client)
    account_id = 56 # int | The account id
    chunkset_slug = 'chunkset_slug_example' # str | The chunkset slug
    chunkset_request = wordlift_client.ChunksetRequest() # ChunksetRequest | 

    try:
        # Create or replace account chunkset
        api_response = await api_instance.put_account_chunkset(account_id, chunkset_slug, chunkset_request)
        print("The response of AccountChunksetsApi->put_account_chunkset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountChunksetsApi->put_account_chunkset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The account id | 
 **chunkset_slug** | **str**| The chunkset slug | 
 **chunkset_request** | [**ChunksetRequest**](ChunksetRequest.md)|  | 

### Return type

[**ChunksetResponse**](ChunksetResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**400** | Bad Request |  -  |
**401** | Authentication Failure |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**415** | Unsupported Media Type |  -  |
**502** | Bad Gateway |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

