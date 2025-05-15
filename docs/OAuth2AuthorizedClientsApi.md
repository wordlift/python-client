# wordlift_client.OAuth2AuthorizedClientsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth2_authorized_client**](OAuth2AuthorizedClientsApi.md#create_o_auth2_authorized_client) | **POST** /oauth2/authorized-clients | Create
[**delete_o_auth2_authorized_client**](OAuth2AuthorizedClientsApi.md#delete_o_auth2_authorized_client) | **DELETE** /oauth2/authorized-clients/{id} | Delete
[**get_o_auth2_authorized_client**](OAuth2AuthorizedClientsApi.md#get_o_auth2_authorized_client) | **GET** /oauth2/authorized-clients/{id} | Get
[**list_o_auth2_authorized_clients**](OAuth2AuthorizedClientsApi.md#list_o_auth2_authorized_clients) | **GET** /oauth2/authorized-clients | List
[**update_o_auth2_authorized_client**](OAuth2AuthorizedClientsApi.md#update_o_auth2_authorized_client) | **PUT** /oauth2/authorized-clients/{id} | Update


# **create_o_auth2_authorized_client**
> OAuth2AuthorizedClient create_o_auth2_authorized_client(o_auth2_authorized_client_request)

Create

Create a OAuth2 Authorized Client

### Example


```python
import wordlift_client
from wordlift_client.models.o_auth2_authorized_client import OAuth2AuthorizedClient
from wordlift_client.models.o_auth2_authorized_client_request import OAuth2AuthorizedClientRequest
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
    api_instance = wordlift_client.OAuth2AuthorizedClientsApi(api_client)
    o_auth2_authorized_client_request = wordlift_client.OAuth2AuthorizedClientRequest() # OAuth2AuthorizedClientRequest | 

    try:
        # Create
        api_response = await api_instance.create_o_auth2_authorized_client(o_auth2_authorized_client_request)
        print("The response of OAuth2AuthorizedClientsApi->create_o_auth2_authorized_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2AuthorizedClientsApi->create_o_auth2_authorized_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth2_authorized_client_request** | [**OAuth2AuthorizedClientRequest**](OAuth2AuthorizedClientRequest.md)|  | 

### Return type

[**OAuth2AuthorizedClient**](OAuth2AuthorizedClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth2_authorized_client**
> delete_o_auth2_authorized_client(id)

Delete

Delete a OAuth2 Authorized Client given its client registration id

### Example


```python
import wordlift_client
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
    api_instance = wordlift_client.OAuth2AuthorizedClientsApi(api_client)
    id = 56 # int | The Id

    try:
        # Delete
        await api_instance.delete_o_auth2_authorized_client(id)
    except Exception as e:
        print("Exception when calling OAuth2AuthorizedClientsApi->delete_o_auth2_authorized_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth2_authorized_client**
> OAuth2AuthorizedClient get_o_auth2_authorized_client(id)

Get

Get a OAuth2 Authorized Client given its client registration id

### Example


```python
import wordlift_client
from wordlift_client.models.o_auth2_authorized_client import OAuth2AuthorizedClient
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
    api_instance = wordlift_client.OAuth2AuthorizedClientsApi(api_client)
    id = 56 # int | The Id

    try:
        # Get
        api_response = await api_instance.get_o_auth2_authorized_client(id)
        print("The response of OAuth2AuthorizedClientsApi->get_o_auth2_authorized_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2AuthorizedClientsApi->get_o_auth2_authorized_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Id | 

### Return type

[**OAuth2AuthorizedClient**](OAuth2AuthorizedClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth2_authorized_clients**
> PageOAuth2AuthorizedClient list_o_auth2_authorized_clients(cursor=cursor, limit=limit)

List

List OAuth2 Authorized Clients

### Example


```python
import wordlift_client
from wordlift_client.models.page_o_auth2_authorized_client import PageOAuth2AuthorizedClient
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
    api_instance = wordlift_client.OAuth2AuthorizedClientsApi(api_client)
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)

    try:
        # List
        api_response = await api_instance.list_o_auth2_authorized_clients(cursor=cursor, limit=limit)
        print("The response of OAuth2AuthorizedClientsApi->list_o_auth2_authorized_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2AuthorizedClientsApi->list_o_auth2_authorized_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]

### Return type

[**PageOAuth2AuthorizedClient**](PageOAuth2AuthorizedClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_o_auth2_authorized_client**
> OAuth2AuthorizedClient update_o_auth2_authorized_client(id, o_auth2_authorized_client_request)

Update

Update a OAuth2 Authorized Client given its client registration id

### Example


```python
import wordlift_client
from wordlift_client.models.o_auth2_authorized_client import OAuth2AuthorizedClient
from wordlift_client.models.o_auth2_authorized_client_request import OAuth2AuthorizedClientRequest
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
    api_instance = wordlift_client.OAuth2AuthorizedClientsApi(api_client)
    id = 56 # int | The Id
    o_auth2_authorized_client_request = wordlift_client.OAuth2AuthorizedClientRequest() # OAuth2AuthorizedClientRequest | 

    try:
        # Update
        api_response = await api_instance.update_o_auth2_authorized_client(id, o_auth2_authorized_client_request)
        print("The response of OAuth2AuthorizedClientsApi->update_o_auth2_authorized_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2AuthorizedClientsApi->update_o_auth2_authorized_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Id | 
 **o_auth2_authorized_client_request** | [**OAuth2AuthorizedClientRequest**](OAuth2AuthorizedClientRequest.md)|  | 

### Return type

[**OAuth2AuthorizedClient**](OAuth2AuthorizedClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

