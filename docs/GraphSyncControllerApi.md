# wordlift_client.GraphSyncControllerApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](GraphSyncControllerApi.md#cancel) | **DELETE** /accounts/{account_id}/graph-sync/runs/{run_id} | 
[**create1**](GraphSyncControllerApi.md#create1) | **POST** /accounts/{account_id}/graph-sync | 
[**delete**](GraphSyncControllerApi.md#delete) | **DELETE** /accounts/{account_id}/graph-sync | 
[**get4**](GraphSyncControllerApi.md#get4) | **GET** /accounts/{account_id}/graph-sync | 
[**run**](GraphSyncControllerApi.md#run) | **POST** /accounts/{account_id}/graph-sync/runs | 
[**update**](GraphSyncControllerApi.md#update) | **PUT** /accounts/{account_id}/graph-sync | 


# **cancel**
> cancel(account_id, run_id)



### Example


```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.GraphSyncControllerApi(api_client)
    account_id = 56 # int | 
    run_id = 'run_id_example' # str | 

    try:
        await api_instance.cancel(account_id, run_id)
    except Exception as e:
        print("Exception when calling GraphSyncControllerApi->cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **run_id** | **str**|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create1**
> GraphSyncResponse create1(account_id, graph_sync_request)



### Example


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

No authorization required

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


```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get4**
> GraphSyncResponse get4(account_id)



### Example


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


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.GraphSyncControllerApi(api_client)
    account_id = 56 # int | 

    try:
        api_response = await api_instance.get4(account_id)
        print("The response of GraphSyncControllerApi->get4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphSyncControllerApi->get4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 

### Return type

[**GraphSyncResponse**](GraphSyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run**
> GraphSyncRunResponse run(account_id, graph_sync_run_request=graph_sync_run_request)



### Example


```python
import wordlift_client
from wordlift_client.models.graph_sync_run_request import GraphSyncRunRequest
from wordlift_client.models.graph_sync_run_response import GraphSyncRunResponse
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.GraphSyncControllerApi(api_client)
    account_id = 56 # int | 
    graph_sync_run_request = wordlift_client.GraphSyncRunRequest() # GraphSyncRunRequest |  (optional)

    try:
        api_response = await api_instance.run(account_id, graph_sync_run_request=graph_sync_run_request)
        print("The response of GraphSyncControllerApi->run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphSyncControllerApi->run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **graph_sync_run_request** | [**GraphSyncRunRequest**](GraphSyncRunRequest.md)|  | [optional] 

### Return type

[**GraphSyncRunResponse**](GraphSyncRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> GraphSyncResponse update(account_id, graph_sync_request)



### Example


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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

