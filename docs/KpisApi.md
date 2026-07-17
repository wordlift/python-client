# wordlift_client.KpisApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_post**](KpisApi.md#create_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_post) | **POST** /accounts/{account_id}/graph-sync/runs/{run_id}/kpis | Store KPI data for a run
[**get_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_get**](KpisApi.md#get_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_get) | **GET** /accounts/{account_id}/graph-sync/runs/{run_id}/kpis | Get KPI data for a run


# **create_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_post**
> KpiResponse create_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_post(run_id, account_id, kpi_create, x_api_version=x_api_version)

Store KPI data for a run

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.kpi_create import KpiCreate
from wordlift_client.models.kpi_response import KpiResponse
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
    api_instance = wordlift_client.KpisApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 
    kpi_create = wordlift_client.KpiCreate() # KpiCreate | 
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Store KPI data for a run
        api_response = await api_instance.create_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_post(run_id, account_id, kpi_create, x_api_version=x_api_version)
        print("The response of KpisApi->create_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KpisApi->create_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 
 **kpi_create** | [**KpiCreate**](KpiCreate.md)|  | 
 **x_api_version** | **date**|  | [optional] 

### Return type

[**KpiResponse**](KpiResponse.md)

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

# **get_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_get**
> KpiResponse get_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_get(run_id, account_id, x_api_version=x_api_version)

Get KPI data for a run

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.kpi_response import KpiResponse
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
    api_instance = wordlift_client.KpisApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 
    x_api_version = '2026-06-01' # date |  (optional)

    try:
        # Get KPI data for a run
        api_response = await api_instance.get_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_get(run_id, account_id, x_api_version=x_api_version)
        print("The response of KpisApi->get_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KpisApi->get_kpi_accounts_account_id_graph_sync_runs_run_id_kpis_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 
 **x_api_version** | **date**|  | [optional] 

### Return type

[**KpiResponse**](KpiResponse.md)

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

