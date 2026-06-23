# wordlift_client.AccountGraphKPIsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_graph_kpi_snapshot**](AccountGraphKPIsApi.md#create_account_graph_kpi_snapshot) | **POST** /accounts/{account_id}/graph-kpis | Create a graph KPI snapshot
[**get_account_graph_kpi_snapshot**](AccountGraphKPIsApi.md#get_account_graph_kpi_snapshot) | **GET** /accounts/{account_id}/graph-kpis/{snapshot_date} | Get a graph KPI snapshot
[**list_account_graph_kpi_snapshots**](AccountGraphKPIsApi.md#list_account_graph_kpi_snapshots) | **GET** /accounts/{account_id}/graph-kpis | List graph KPI snapshots
[**put_account_graph_kpi_snapshot**](AccountGraphKPIsApi.md#put_account_graph_kpi_snapshot) | **PUT** /accounts/{account_id}/graph-kpis/{snapshot_date} | Create or replace a graph KPI snapshot


# **create_account_graph_kpi_snapshot**
> GraphKpiSnapshot create_account_graph_kpi_snapshot(account_id, graph_kpi_snapshot_request)

Create a graph KPI snapshot

Creates a graph KPI snapshot. Intended for graph-sync ingestion after a graph-sync run completes. Requires an account key for the same account or a privileged token. The request body must include `snapshot_date`. 

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.graph_kpi_snapshot import GraphKpiSnapshot
from wordlift_client.models.graph_kpi_snapshot_request import GraphKpiSnapshotRequest
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
    api_instance = wordlift_client.AccountGraphKPIsApi(api_client)
    account_id = 1506805 # int | WordLift account id.
    graph_kpi_snapshot_request = wordlift_client.GraphKpiSnapshotRequest() # GraphKpiSnapshotRequest | 

    try:
        # Create a graph KPI snapshot
        api_response = await api_instance.create_account_graph_kpi_snapshot(account_id, graph_kpi_snapshot_request)
        print("The response of AccountGraphKPIsApi->create_account_graph_kpi_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGraphKPIsApi->create_account_graph_kpi_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| WordLift account id. | 
 **graph_kpi_snapshot_request** | [**GraphKpiSnapshotRequest**](GraphKpiSnapshotRequest.md)|  | 

### Return type

[**GraphKpiSnapshot**](GraphKpiSnapshot.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Graph KPI snapshot created. |  -  |
**400** | Required identity fields are missing or invalid. |  -  |
**401** | Authentication is required. |  -  |
**403** | The caller cannot write KPI snapshots for this account. |  -  |
**409** | A snapshot already exists for the account and date. |  -  |
**422** | The KPI payload is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_graph_kpi_snapshot**
> GraphKpiSnapshot get_account_graph_kpi_snapshot(account_id, snapshot_date)

Get a graph KPI snapshot

Gets one graph KPI snapshot by account and snapshot date. Reads support account-owned bearer tokens, account keys, and privileged tokens. 

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.graph_kpi_snapshot import GraphKpiSnapshot
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
    api_instance = wordlift_client.AccountGraphKPIsApi(api_client)
    account_id = 1506805 # int | WordLift account id.
    snapshot_date = '2026-06-23T00:00:00.000Z' # date | Snapshot date.

    try:
        # Get a graph KPI snapshot
        api_response = await api_instance.get_account_graph_kpi_snapshot(account_id, snapshot_date)
        print("The response of AccountGraphKPIsApi->get_account_graph_kpi_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGraphKPIsApi->get_account_graph_kpi_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| WordLift account id. | 
 **snapshot_date** | **date**| Snapshot date. | 

### Return type

[**GraphKpiSnapshot**](GraphKpiSnapshot.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Graph KPI snapshot. |  -  |
**401** | Authentication is required. |  -  |
**403** | The account key does not match the requested account. |  -  |
**404** | The snapshot or account was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_graph_kpi_snapshots**
> GraphKpiSnapshotPage list_account_graph_kpi_snapshots(account_id, date_from=date_from, date_to=date_to, limit=limit)

List graph KPI snapshots

Lists dated graph KPI snapshots for the account. Reads support account-owned bearer tokens, account keys, and privileged tokens. 

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.graph_kpi_snapshot_page import GraphKpiSnapshotPage
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
    api_instance = wordlift_client.AccountGraphKPIsApi(api_client)
    account_id = 1506805 # int | WordLift account id.
    date_from = '2026-06-01T00:00:00.000Z' # date | Earliest snapshot date to include. (optional)
    date_to = '2026-06-23T00:00:00.000Z' # date | Latest snapshot date to include. (optional)
    limit = 30 # int | Maximum number of snapshots to return. Allowed range: 1-365. (optional) (default to 30)

    try:
        # List graph KPI snapshots
        api_response = await api_instance.list_account_graph_kpi_snapshots(account_id, date_from=date_from, date_to=date_to, limit=limit)
        print("The response of AccountGraphKPIsApi->list_account_graph_kpi_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGraphKPIsApi->list_account_graph_kpi_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| WordLift account id. | 
 **date_from** | **date**| Earliest snapshot date to include. | [optional] 
 **date_to** | **date**| Latest snapshot date to include. | [optional] 
 **limit** | **int**| Maximum number of snapshots to return. Allowed range: 1-365. | [optional] [default to 30]

### Return type

[**GraphKpiSnapshotPage**](GraphKpiSnapshotPage.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Graph KPI snapshots. |  -  |
**400** | Invalid query parameters. |  -  |
**401** | Authentication is required. |  -  |
**403** | The account key does not match the requested account. |  -  |
**404** | The authenticated user cannot access the requested account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_account_graph_kpi_snapshot**
> GraphKpiSnapshot put_account_graph_kpi_snapshot(account_id, snapshot_date, graph_kpi_snapshot_request)

Create or replace a graph KPI snapshot

Idempotently creates or replaces the graph KPI snapshot identified by the path account and snapshot date. Intended for graph-sync ingestion. Requires an account key for the same account or a privileged token. If `snapshot_date` is present in the body, it must match the path value. 

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.graph_kpi_snapshot import GraphKpiSnapshot
from wordlift_client.models.graph_kpi_snapshot_request import GraphKpiSnapshotRequest
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
    api_instance = wordlift_client.AccountGraphKPIsApi(api_client)
    account_id = 1506805 # int | WordLift account id.
    snapshot_date = '2026-06-23T00:00:00.000Z' # date | Snapshot date.
    graph_kpi_snapshot_request = wordlift_client.GraphKpiSnapshotRequest() # GraphKpiSnapshotRequest | 

    try:
        # Create or replace a graph KPI snapshot
        api_response = await api_instance.put_account_graph_kpi_snapshot(account_id, snapshot_date, graph_kpi_snapshot_request)
        print("The response of AccountGraphKPIsApi->put_account_graph_kpi_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountGraphKPIsApi->put_account_graph_kpi_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| WordLift account id. | 
 **snapshot_date** | **date**| Snapshot date. | 
 **graph_kpi_snapshot_request** | [**GraphKpiSnapshotRequest**](GraphKpiSnapshotRequest.md)|  | 

### Return type

[**GraphKpiSnapshot**](GraphKpiSnapshot.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Graph KPI snapshot replaced. |  -  |
**201** | Graph KPI snapshot created. |  -  |
**400** | The body snapshot date does not match the path date. |  -  |
**401** | Authentication is required. |  -  |
**403** | The caller cannot write KPI snapshots for this account. |  -  |
**422** | The KPI payload is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

