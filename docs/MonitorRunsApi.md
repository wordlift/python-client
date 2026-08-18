# wordlift_client.MonitorRunsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_run_accounts_account_id_monitoring_runs_run_id_delete**](MonitorRunsApi.md#abort_run_accounts_account_id_monitoring_runs_run_id_delete) | **DELETE** /accounts/{account_id}/monitoring/runs/{run_id} | Abort Run
[**get_run_accounts_account_id_monitoring_runs_run_id_get**](MonitorRunsApi.md#get_run_accounts_account_id_monitoring_runs_run_id_get) | **GET** /accounts/{account_id}/monitoring/runs/{run_id} | Get Run
[**list_runs_accounts_account_id_monitoring_runs_get**](MonitorRunsApi.md#list_runs_accounts_account_id_monitoring_runs_get) | **GET** /accounts/{account_id}/monitoring/runs | List Runs


# **abort_run_accounts_account_id_monitoring_runs_run_id_delete**
> MonitorRunResponse abort_run_accounts_account_id_monitoring_runs_run_id_delete(run_id, account_id)

Abort Run

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.monitor_run_response import MonitorRunResponse
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
    api_instance = wordlift_client.MonitorRunsApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Abort Run
        api_response = await api_instance.abort_run_accounts_account_id_monitoring_runs_run_id_delete(run_id, account_id)
        print("The response of MonitorRunsApi->abort_run_accounts_account_id_monitoring_runs_run_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorRunsApi->abort_run_accounts_account_id_monitoring_runs_run_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**MonitorRunResponse**](MonitorRunResponse.md)

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

# **get_run_accounts_account_id_monitoring_runs_run_id_get**
> MonitorRunResponse get_run_accounts_account_id_monitoring_runs_run_id_get(run_id, account_id)

Get Run

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.monitor_run_response import MonitorRunResponse
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
    api_instance = wordlift_client.MonitorRunsApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Get Run
        api_response = await api_instance.get_run_accounts_account_id_monitoring_runs_run_id_get(run_id, account_id)
        print("The response of MonitorRunsApi->get_run_accounts_account_id_monitoring_runs_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorRunsApi->get_run_accounts_account_id_monitoring_runs_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**MonitorRunResponse**](MonitorRunResponse.md)

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

# **list_runs_accounts_account_id_monitoring_runs_get**
> ListRunsResponse list_runs_accounts_account_id_monitoring_runs_get(account_id, limit=limit, offset=offset)

List Runs

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_runs_response import ListRunsResponse
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
    api_instance = wordlift_client.MonitorRunsApi(api_client)
    account_id = 'account_id_example' # str | 
    limit = 5 # int | Maximum number of items to return. (optional) (default to 5)
    offset = 0 # int | Number of items to skip. (optional) (default to 0)

    try:
        # List Runs
        api_response = await api_instance.list_runs_accounts_account_id_monitoring_runs_get(account_id, limit=limit, offset=offset)
        print("The response of MonitorRunsApi->list_runs_accounts_account_id_monitoring_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorRunsApi->list_runs_accounts_account_id_monitoring_runs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **limit** | **int**| Maximum number of items to return. | [optional] [default to 5]
 **offset** | **int**| Number of items to skip. | [optional] [default to 0]

### Return type

[**ListRunsResponse**](ListRunsResponse.md)

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

