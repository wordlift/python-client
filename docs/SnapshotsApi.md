# wordlift_client.SnapshotsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_snapshot_kpi_graphs_graph_id_snapshots_date_get**](SnapshotsApi.md#get_snapshot_kpi_graphs_graph_id_snapshots_date_get) | **GET** /kpi/graphs/{graph_id}/snapshots/{date} | Get one daily KPI snapshot
[**list_snapshots_kpi_graphs_graph_id_snapshots_get**](SnapshotsApi.md#list_snapshots_kpi_graphs_graph_id_snapshots_get) | **GET** /kpi/graphs/{graph_id}/snapshots | List daily KPI snapshots


# **get_snapshot_kpi_graphs_graph_id_snapshots_date_get**
> SnapshotResponse get_snapshot_kpi_graphs_graph_id_snapshots_date_get(graph_id, var_date)

Get one daily KPI snapshot

Returns the complete daily KPI snapshot for a graph, including graph-wide `all_` / `public_` / `private_` metrics and the public-only SHACL validation outputs.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.snapshot_response import SnapshotResponse
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
    api_instance = wordlift_client.SnapshotsApi(api_client)
    graph_id = '1506805' # str | Public WordLift graph identifier (`account.id`).
    var_date = '2026-03-13' # str | Logical KPI day in `YYYY-MM-DD` format.

    try:
        # Get one daily KPI snapshot
        api_response = await api_instance.get_snapshot_kpi_graphs_graph_id_snapshots_date_get(graph_id, var_date)
        print("The response of SnapshotsApi->get_snapshot_kpi_graphs_graph_id_snapshots_date_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->get_snapshot_kpi_graphs_graph_id_snapshots_date_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**| Public WordLift graph identifier (&#x60;account.id&#x60;). | 
 **var_date** | **str**| Logical KPI day in &#x60;YYYY-MM-DD&#x60; format. | 

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complete daily snapshot payload. |  -  |
**400** | The request was syntactically valid but semantically invalid. |  -  |
**403** | The caller is not authorized to operate on the requested graph. |  -  |
**404** | The requested resource was not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshots_kpi_graphs_graph_id_snapshots_get**
> SnapshotListResponse list_snapshots_kpi_graphs_graph_id_snapshots_get(graph_id, date_from=date_from, date_to=date_to, limit=limit, metrics=metrics)

List daily KPI snapshots

Returns a time-series of daily graph KPI snapshots for a single public graph identifier. Use the `metrics` query parameter to request a compact projection suitable for charts.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.snapshot_list_response import SnapshotListResponse
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
    api_instance = wordlift_client.SnapshotsApi(api_client)
    graph_id = '1506805' # str | Public WordLift graph identifier (`account.id`).
    date_from = 'date_from_example' # str | Inclusive lower snapshot date bound in `YYYY-MM-DD` format. (optional)
    date_to = 'date_to_example' # str | Inclusive upper snapshot date bound in `YYYY-MM-DD` format. (optional)
    limit = 56 # int | Maximum number of snapshot rows to return. (optional)
    metrics = 'metrics_example' # str | Comma-separated KPI field projection for compact chart responses. (optional)

    try:
        # List daily KPI snapshots
        api_response = await api_instance.list_snapshots_kpi_graphs_graph_id_snapshots_get(graph_id, date_from=date_from, date_to=date_to, limit=limit, metrics=metrics)
        print("The response of SnapshotsApi->list_snapshots_kpi_graphs_graph_id_snapshots_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->list_snapshots_kpi_graphs_graph_id_snapshots_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**| Public WordLift graph identifier (&#x60;account.id&#x60;). | 
 **date_from** | **str**| Inclusive lower snapshot date bound in &#x60;YYYY-MM-DD&#x60; format. | [optional] 
 **date_to** | **str**| Inclusive upper snapshot date bound in &#x60;YYYY-MM-DD&#x60; format. | [optional] 
 **limit** | **int**| Maximum number of snapshot rows to return. | [optional] 
 **metrics** | **str**| Comma-separated KPI field projection for compact chart responses. | [optional] 

### Return type

[**SnapshotListResponse**](SnapshotListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Daily KPI snapshot history for the graph. |  -  |
**400** | The request was syntactically valid but semantically invalid. |  -  |
**403** | The caller is not authorized to operate on the requested graph. |  -  |
**404** | The requested resource was not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

