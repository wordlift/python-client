# wordlift_client.BootstrapApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_bootstrap_accounts_account_id_graph_sync_bootstrap_delete**](BootstrapApi.md#abort_bootstrap_accounts_account_id_graph_sync_bootstrap_delete) | **DELETE** /accounts/{account_id}/graph-sync/bootstrap | Abort bootstrap
[**get_bootstrap_accounts_account_id_graph_sync_bootstrap_get**](BootstrapApi.md#get_bootstrap_accounts_account_id_graph_sync_bootstrap_get) | **GET** /accounts/{account_id}/graph-sync/bootstrap | Get bootstrap status
[**get_bootstrap_logs_accounts_account_id_graph_sync_bootstrap_job_id_logs_get**](BootstrapApi.md#get_bootstrap_logs_accounts_account_id_graph_sync_bootstrap_job_id_logs_get) | **GET** /accounts/{account_id}/graph-sync/bootstrap/{job_id}/logs | Get paginated logs for a bootstrap job
[**start_bootstrap_accounts_account_id_graph_sync_bootstrap_post**](BootstrapApi.md#start_bootstrap_accounts_account_id_graph_sync_bootstrap_post) | **POST** /accounts/{account_id}/graph-sync/bootstrap | Start bootstrap


# **abort_bootstrap_accounts_account_id_graph_sync_bootstrap_delete**
> abort_bootstrap_accounts_account_id_graph_sync_bootstrap_delete(account_id, x_api_version=x_api_version)

Abort bootstrap

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
    api_instance = wordlift_client.BootstrapApi(api_client)
    account_id = 'account_id_example' # str | 
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Abort bootstrap
        await api_instance.abort_bootstrap_accounts_account_id_graph_sync_bootstrap_delete(account_id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling BootstrapApi->abort_bootstrap_accounts_account_id_graph_sync_bootstrap_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **x_api_version** | **date**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bootstrap_accounts_account_id_graph_sync_bootstrap_get**
> BootstrapJobResponse get_bootstrap_accounts_account_id_graph_sync_bootstrap_get(account_id, x_api_version=x_api_version)

Get bootstrap status

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.bootstrap_job_response import BootstrapJobResponse
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
    api_instance = wordlift_client.BootstrapApi(api_client)
    account_id = 'account_id_example' # str | 
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Get bootstrap status
        api_response = await api_instance.get_bootstrap_accounts_account_id_graph_sync_bootstrap_get(account_id, x_api_version=x_api_version)
        print("The response of BootstrapApi->get_bootstrap_accounts_account_id_graph_sync_bootstrap_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BootstrapApi->get_bootstrap_accounts_account_id_graph_sync_bootstrap_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **x_api_version** | **date**|  | [optional] 

### Return type

[**BootstrapJobResponse**](BootstrapJobResponse.md)

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

# **get_bootstrap_logs_accounts_account_id_graph_sync_bootstrap_job_id_logs_get**
> LogsPage get_bootstrap_logs_accounts_account_id_graph_sync_bootstrap_job_id_logs_get(job_id, account_id, offset=offset, limit=limit, x_api_version=x_api_version)

Get paginated logs for a bootstrap job

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.logs_page import LogsPage
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
    api_instance = wordlift_client.BootstrapApi(api_client)
    job_id = 'job_id_example' # str | 
    account_id = 'account_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Get paginated logs for a bootstrap job
        api_response = await api_instance.get_bootstrap_logs_accounts_account_id_graph_sync_bootstrap_job_id_logs_get(job_id, account_id, offset=offset, limit=limit, x_api_version=x_api_version)
        print("The response of BootstrapApi->get_bootstrap_logs_accounts_account_id_graph_sync_bootstrap_job_id_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BootstrapApi->get_bootstrap_logs_accounts_account_id_graph_sync_bootstrap_job_id_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **account_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **x_api_version** | **date**|  | [optional] 

### Return type

[**LogsPage**](LogsPage.md)

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

# **start_bootstrap_accounts_account_id_graph_sync_bootstrap_post**
> BootstrapJobResponse start_bootstrap_accounts_account_id_graph_sync_bootstrap_post(account_id, x_api_version=x_api_version)

Start bootstrap

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.bootstrap_job_response import BootstrapJobResponse
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
    api_instance = wordlift_client.BootstrapApi(api_client)
    account_id = 'account_id_example' # str | 
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Start bootstrap
        api_response = await api_instance.start_bootstrap_accounts_account_id_graph_sync_bootstrap_post(account_id, x_api_version=x_api_version)
        print("The response of BootstrapApi->start_bootstrap_accounts_account_id_graph_sync_bootstrap_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BootstrapApi->start_bootstrap_accounts_account_id_graph_sync_bootstrap_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **x_api_version** | **date**|  | [optional] 

### Return type

[**BootstrapJobResponse**](BootstrapJobResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

