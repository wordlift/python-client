# wordlift_client.SnapshotsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_snapshot_kpis_graphs_graph_id_snapshots_date_get**](SnapshotsApi.md#get_snapshot_kpis_graphs_graph_id_snapshots_date_get) | **GET** /kpis/graphs/{graph_id}/snapshots/{date} | Get Snapshot
[**list_snapshots_kpis_graphs_graph_id_snapshots_get**](SnapshotsApi.md#list_snapshots_kpis_graphs_graph_id_snapshots_get) | **GET** /kpis/graphs/{graph_id}/snapshots | List Snapshots


# **get_snapshot_kpis_graphs_graph_id_snapshots_date_get**
> Dict[str, object] get_snapshot_kpis_graphs_graph_id_snapshots_date_get(graph_id, var_date)

Get Snapshot

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
    api_instance = wordlift_client.SnapshotsApi(api_client)
    graph_id = 'graph_id_example' # str | 
    var_date = 'var_date_example' # str | 

    try:
        # Get Snapshot
        api_response = await api_instance.get_snapshot_kpis_graphs_graph_id_snapshots_date_get(graph_id, var_date)
        print("The response of SnapshotsApi->get_snapshot_kpis_graphs_graph_id_snapshots_date_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->get_snapshot_kpis_graphs_graph_id_snapshots_date_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**|  | 
 **var_date** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **list_snapshots_kpis_graphs_graph_id_snapshots_get**
> Dict[str, object] list_snapshots_kpis_graphs_graph_id_snapshots_get(graph_id, date_from=date_from, date_to=date_to, limit=limit, metrics=metrics)

List Snapshots

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
    api_instance = wordlift_client.SnapshotsApi(api_client)
    graph_id = 'graph_id_example' # str | 
    date_from = 'date_from_example' # str |  (optional)
    date_to = 'date_to_example' # str |  (optional)
    limit = 56 # int |  (optional)
    metrics = 'metrics_example' # str |  (optional)

    try:
        # List Snapshots
        api_response = await api_instance.list_snapshots_kpis_graphs_graph_id_snapshots_get(graph_id, date_from=date_from, date_to=date_to, limit=limit, metrics=metrics)
        print("The response of SnapshotsApi->list_snapshots_kpis_graphs_graph_id_snapshots_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->list_snapshots_kpis_graphs_graph_id_snapshots_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**|  | 
 **date_from** | **str**|  | [optional] 
 **date_to** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **metrics** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

