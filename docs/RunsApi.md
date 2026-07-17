# wordlift_client.RunsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_run_accounts_account_id_graph_sync_runs_post**](RunsApi.md#create_run_accounts_account_id_graph_sync_runs_post) | **POST** /accounts/{account_id}/graph-sync/runs | Create a run
[**finalize_run_accounts_account_id_graph_sync_runs_run_id_patch**](RunsApi.md#finalize_run_accounts_account_id_graph_sync_runs_run_id_patch) | **PATCH** /accounts/{account_id}/graph-sync/runs/{run_id} | Finalize a run
[**get_run_accounts_account_id_graph_sync_runs_run_id_get**](RunsApi.md#get_run_accounts_account_id_graph_sync_runs_run_id_get) | **GET** /accounts/{account_id}/graph-sync/runs/{run_id} | Get a run
[**list_runs_accounts_account_id_graph_sync_runs_get**](RunsApi.md#list_runs_accounts_account_id_graph_sync_runs_get) | **GET** /accounts/{account_id}/graph-sync/runs | List runs
[**update_progress_accounts_account_id_graph_sync_runs_run_id_progress_patch**](RunsApi.md#update_progress_accounts_account_id_graph_sync_runs_run_id_progress_patch) | **PATCH** /accounts/{account_id}/graph-sync/runs/{run_id}/progress | Update run progress


# **create_run_accounts_account_id_graph_sync_runs_post**
> RunResponse create_run_accounts_account_id_graph_sync_runs_post(account_id, run_create, x_api_version=x_api_version)

Create a run

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.run_create import RunCreate
from wordlift_client.models.run_response import RunResponse
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
    api_instance = wordlift_client.RunsApi(api_client)
    account_id = 'account_id_example' # str | 
    run_create = wordlift_client.RunCreate() # RunCreate | 
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Create a run
        api_response = await api_instance.create_run_accounts_account_id_graph_sync_runs_post(account_id, run_create, x_api_version=x_api_version)
        print("The response of RunsApi->create_run_accounts_account_id_graph_sync_runs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->create_run_accounts_account_id_graph_sync_runs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **run_create** | [**RunCreate**](RunCreate.md)|  | 
 **x_api_version** | **date**|  | [optional] 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_run_accounts_account_id_graph_sync_runs_run_id_patch**
> finalize_run_accounts_account_id_graph_sync_runs_run_id_patch(run_id, account_id, run_finalize, x_api_version=x_api_version)

Finalize a run

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.run_finalize import RunFinalize
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
    api_instance = wordlift_client.RunsApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 
    run_finalize = wordlift_client.RunFinalize() # RunFinalize | 
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Finalize a run
        await api_instance.finalize_run_accounts_account_id_graph_sync_runs_run_id_patch(run_id, account_id, run_finalize, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling RunsApi->finalize_run_accounts_account_id_graph_sync_runs_run_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 
 **run_finalize** | [**RunFinalize**](RunFinalize.md)|  | 
 **x_api_version** | **date**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_accounts_account_id_graph_sync_runs_run_id_get**
> RunResponse get_run_accounts_account_id_graph_sync_runs_run_id_get(run_id, account_id, x_api_version=x_api_version)

Get a run

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.run_response import RunResponse
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
    api_instance = wordlift_client.RunsApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Get a run
        api_response = await api_instance.get_run_accounts_account_id_graph_sync_runs_run_id_get(run_id, account_id, x_api_version=x_api_version)
        print("The response of RunsApi->get_run_accounts_account_id_graph_sync_runs_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->get_run_accounts_account_id_graph_sync_runs_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 
 **x_api_version** | **date**|  | [optional] 

### Return type

[**RunResponse**](RunResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runs_accounts_account_id_graph_sync_runs_get**
> List[RunResponse] list_runs_accounts_account_id_graph_sync_runs_get(account_id, profile=profile, status=status, since=since, limit=limit, x_api_version=x_api_version)

List runs

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.run_response import RunResponse
from wordlift_client.models.run_status import RunStatus
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
    api_instance = wordlift_client.RunsApi(api_client)
    account_id = 'account_id_example' # str | 
    profile = 'profile_example' # str |  (optional)
    status = wordlift_client.RunStatus() # RunStatus |  (optional)
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # List runs
        api_response = await api_instance.list_runs_accounts_account_id_graph_sync_runs_get(account_id, profile=profile, status=status, since=since, limit=limit, x_api_version=x_api_version)
        print("The response of RunsApi->list_runs_accounts_account_id_graph_sync_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->list_runs_accounts_account_id_graph_sync_runs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **profile** | **str**|  | [optional] 
 **status** | [**RunStatus**](.md)|  | [optional] 
 **since** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **x_api_version** | **date**|  | [optional] 

### Return type

[**List[RunResponse]**](RunResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_progress_accounts_account_id_graph_sync_runs_run_id_progress_patch**
> update_progress_accounts_account_id_graph_sync_runs_run_id_progress_patch(run_id, account_id, run_progress_update, x_api_version=x_api_version)

Update run progress

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.run_progress_update import RunProgressUpdate
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
    api_instance = wordlift_client.RunsApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 
    run_progress_update = wordlift_client.RunProgressUpdate() # RunProgressUpdate | 
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Update run progress
        await api_instance.update_progress_accounts_account_id_graph_sync_runs_run_id_progress_patch(run_id, account_id, run_progress_update, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling RunsApi->update_progress_accounts_account_id_graph_sync_runs_run_id_progress_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 
 **run_progress_update** | [**RunProgressUpdate**](RunProgressUpdate.md)|  | 
 **x_api_version** | **date**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

