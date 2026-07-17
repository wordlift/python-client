# wordlift_client.GraphSyncControllerApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create1**](GraphSyncControllerApi.md#create1) | **POST** /accounts/{account_id}/graph-sync | 
[**delete**](GraphSyncControllerApi.md#delete) | **DELETE** /accounts/{account_id}/graph-sync | 
[**get3**](GraphSyncControllerApi.md#get3) | **GET** /accounts/{account_id}/graph-sync | 
[**update**](GraphSyncControllerApi.md#update) | **PUT** /accounts/{account_id}/graph-sync | 


# **create1**
> GraphSyncResponse create1(account_id, graph_sync_request)



### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.graph_sync_request import GraphSyncRequest
from wordlift_client.models.graph_sync_response import GraphSyncResponse
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
    api_instance = wordlift_client.GraphSyncControllerApi(api_client)
    account_id = 56 # int | 
    graph_sync_request = wordlift_client.GraphSyncRequest() # GraphSyncRequest | 

    try:
        api_response = await api_instance.create1(account_id, graph_sync_request)
        print("The response of GraphSyncControllerApi->create1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphSyncControllerApi->create1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **graph_sync_request** | [**GraphSyncRequest**](GraphSyncRequest.md)|  | 

### Return type

[**GraphSyncResponse**](GraphSyncResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(account_id, delete_project=delete_project)



### Example

* Api Key Authentication (ApiKey):

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

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.GraphSyncControllerApi(api_client)
    account_id = 56 # int | 
    delete_project = False # bool |  (optional) (default to False)

    try:
        await api_instance.delete(account_id, delete_project=delete_project)
    except Exception as e:
        print("Exception when calling GraphSyncControllerApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **delete_project** | **bool**|  | [optional] [default to False]

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get3**
> GraphSyncResponse get3(account_id)



### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.graph_sync_response import GraphSyncResponse
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
    api_instance = wordlift_client.GraphSyncControllerApi(api_client)
    account_id = 56 # int | 

    try:
        api_response = await api_instance.get3(account_id)
        print("The response of GraphSyncControllerApi->get3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphSyncControllerApi->get3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 

### Return type

[**GraphSyncResponse**](GraphSyncResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> GraphSyncResponse update(account_id, graph_sync_request)



### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.graph_sync_request import GraphSyncRequest
from wordlift_client.models.graph_sync_response import GraphSyncResponse
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
    api_instance = wordlift_client.GraphSyncControllerApi(api_client)
    account_id = 56 # int | 
    graph_sync_request = wordlift_client.GraphSyncRequest() # GraphSyncRequest | 

    try:
        api_response = await api_instance.update(account_id, graph_sync_request)
        print("The response of GraphSyncControllerApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphSyncControllerApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **graph_sync_request** | [**GraphSyncRequest**](GraphSyncRequest.md)|  | 

### Return type

[**GraphSyncResponse**](GraphSyncResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

