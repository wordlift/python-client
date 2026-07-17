# wordlift_client.FailuresApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_failure_accounts_account_id_graph_sync_runs_run_id_failures_post**](FailuresApi.md#create_failure_accounts_account_id_graph_sync_runs_run_id_failures_post) | **POST** /accounts/{account_id}/graph-sync/runs/{run_id}/failures | Append a failure to a run
[**list_failures_accounts_account_id_graph_sync_runs_run_id_failures_get**](FailuresApi.md#list_failures_accounts_account_id_graph_sync_runs_run_id_failures_get) | **GET** /accounts/{account_id}/graph-sync/runs/{run_id}/failures | List failures for a run


# **create_failure_accounts_account_id_graph_sync_runs_run_id_failures_post**
> FailureResponse create_failure_accounts_account_id_graph_sync_runs_run_id_failures_post(run_id, account_id, failure_create, x_api_version=x_api_version)

Append a failure to a run

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.failure_create import FailureCreate
from wordlift_client.models.failure_response import FailureResponse
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
    api_instance = wordlift_client.FailuresApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 
    failure_create = wordlift_client.FailureCreate() # FailureCreate | 
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Append a failure to a run
        api_response = await api_instance.create_failure_accounts_account_id_graph_sync_runs_run_id_failures_post(run_id, account_id, failure_create, x_api_version=x_api_version)
        print("The response of FailuresApi->create_failure_accounts_account_id_graph_sync_runs_run_id_failures_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailuresApi->create_failure_accounts_account_id_graph_sync_runs_run_id_failures_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 
 **failure_create** | [**FailureCreate**](FailureCreate.md)|  | 
 **x_api_version** | **date**|  | [optional] 

### Return type

[**FailureResponse**](FailureResponse.md)

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

# **list_failures_accounts_account_id_graph_sync_runs_run_id_failures_get**
> List[FailureResponse] list_failures_accounts_account_id_graph_sync_runs_run_id_failures_get(run_id, account_id, limit=limit, offset=offset, x_api_version=x_api_version)

List failures for a run

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.failure_response import FailureResponse
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
    api_instance = wordlift_client.FailuresApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # List failures for a run
        api_response = await api_instance.list_failures_accounts_account_id_graph_sync_runs_run_id_failures_get(run_id, account_id, limit=limit, offset=offset, x_api_version=x_api_version)
        print("The response of FailuresApi->list_failures_accounts_account_id_graph_sync_runs_run_id_failures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailuresApi->list_failures_accounts_account_id_graph_sync_runs_run_id_failures_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **x_api_version** | **date**|  | [optional] 

### Return type

[**List[FailureResponse]**](FailureResponse.md)

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

