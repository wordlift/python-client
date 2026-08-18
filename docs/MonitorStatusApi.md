# wordlift_client.MonitorStatusApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get**](MonitorStatusApi.md#get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get) | **GET** /accounts/{account_id}/monitoring/monitors/{monitor_id}/checks/{check_name} | Get Check Timeseries
[**get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get**](MonitorStatusApi.md#get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get) | **GET** /accounts/{account_id}/monitoring/monitors/{monitor_id}/status | Get Monitor Status
[**list_monitor_statuses_accounts_account_id_monitoring_status_get**](MonitorStatusApi.md#list_monitor_statuses_accounts_account_id_monitoring_status_get) | **GET** /accounts/{account_id}/monitoring/status | List Monitor Statuses


# **get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get**
> CheckTimeseriesResponse get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get(monitor_id, check_name, account_id, since=since, to=to, limit=limit, sort=sort)

Get Check Timeseries

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.check_timeseries_response import CheckTimeseriesResponse
from wordlift_client.models.sort_direction import SortDirection
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
    api_instance = wordlift_client.MonitorStatusApi(api_client)
    monitor_id = 'monitor_id_example' # str | 
    check_name = 'check_name_example' # str | 
    account_id = 'account_id_example' # str | 
    since = '2013-10-20T19:20:30+01:00' # datetime | Return results on or after this RFC 3339 timestamp (inclusive). (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Return results on or before this RFC 3339 timestamp (inclusive). (optional)
    limit = 100 # int | Maximum number of data points to return. (optional) (default to 100)
    sort = wordlift_client.SortDirection() # SortDirection | Sort order: 'asc' for oldest-first (graphs), 'desc' for newest-first (history). (optional)

    try:
        # Get Check Timeseries
        api_response = await api_instance.get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get(monitor_id, check_name, account_id, since=since, to=to, limit=limit, sort=sort)
        print("The response of MonitorStatusApi->get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorStatusApi->get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **str**|  | 
 **check_name** | **str**|  | 
 **account_id** | **str**|  | 
 **since** | **datetime**| Return results on or after this RFC 3339 timestamp (inclusive). | [optional] 
 **to** | **datetime**| Return results on or before this RFC 3339 timestamp (inclusive). | [optional] 
 **limit** | **int**| Maximum number of data points to return. | [optional] [default to 100]
 **sort** | [**SortDirection**](.md)| Sort order: &#39;asc&#39; for oldest-first (graphs), &#39;desc&#39; for newest-first (history). | [optional] 

### Return type

[**CheckTimeseriesResponse**](CheckTimeseriesResponse.md)

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

# **get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get**
> MonitorStatusResponse get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get(monitor_id, account_id, segment_id=segment_id)

Get Monitor Status

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.monitor_status_response import MonitorStatusResponse
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
    api_instance = wordlift_client.MonitorStatusApi(api_client)
    monitor_id = 'monitor_id_example' # str | 
    account_id = 'account_id_example' # str | 
    segment_id = 'segment_id_example' # str | Return the monitor's status scoped to this segment instead of the aggregate view. Omitted or empty returns the aggregate view. (optional)

    try:
        # Get Monitor Status
        api_response = await api_instance.get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get(monitor_id, account_id, segment_id=segment_id)
        print("The response of MonitorStatusApi->get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorStatusApi->get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **str**|  | 
 **account_id** | **str**|  | 
 **segment_id** | **str**| Return the monitor&#39;s status scoped to this segment instead of the aggregate view. Omitted or empty returns the aggregate view. | [optional] 

### Return type

[**MonitorStatusResponse**](MonitorStatusResponse.md)

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

# **list_monitor_statuses_accounts_account_id_monitoring_status_get**
> ListMonitorStatusResponse list_monitor_statuses_accounts_account_id_monitoring_status_get(account_id, url=url, status=status, score_min=score_min, score_max=score_max, segment_id=segment_id, order_by=order_by, sort=sort, cursor=cursor, limit=limit)

List Monitor Statuses

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_monitor_status_response import ListMonitorStatusResponse
from wordlift_client.models.monitor_status_check_status import MonitorStatusCheckStatus
from wordlift_client.models.monitor_status_order_by import MonitorStatusOrderBy
from wordlift_client.models.sort_direction import SortDirection
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
    api_instance = wordlift_client.MonitorStatusApi(api_client)
    account_id = 'account_id_example' # str | 
    url = 'url_example' # str | Glob pattern to filter by URL (e.g. `*example.com*`). (optional)
    status = [wordlift_client.MonitorStatusCheckStatus()] # List[MonitorStatusCheckStatus] | Filter by check status (repeatable, e.g. `?status=ERROR&status=WARNING`). (optional)
    score_min = 3.4 # float | Minimum score (inclusive). (optional)
    score_max = 3.4 # float | Maximum score (inclusive). (optional)
    segment_id = 'segment_id_example' # str | Return only monitor statuses matched by the given segment's matchers. Pass 'unassigned' to match monitor statuses matched by no segment. Omitted or empty returns the aggregate (unscoped) view. (optional)
    order_by = wordlift_client.MonitorStatusOrderBy() # MonitorStatusOrderBy | Field to sort by. (optional)
    sort = wordlift_client.SortDirection() # SortDirection | Sort direction. (optional)
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 20 # int | Maximum number of items to return. (optional) (default to 20)

    try:
        # List Monitor Statuses
        api_response = await api_instance.list_monitor_statuses_accounts_account_id_monitoring_status_get(account_id, url=url, status=status, score_min=score_min, score_max=score_max, segment_id=segment_id, order_by=order_by, sort=sort, cursor=cursor, limit=limit)
        print("The response of MonitorStatusApi->list_monitor_statuses_accounts_account_id_monitoring_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorStatusApi->list_monitor_statuses_accounts_account_id_monitoring_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **url** | **str**| Glob pattern to filter by URL (e.g. &#x60;*example.com*&#x60;). | [optional] 
 **status** | [**List[MonitorStatusCheckStatus]**](MonitorStatusCheckStatus.md)| Filter by check status (repeatable, e.g. &#x60;?status&#x3D;ERROR&amp;status&#x3D;WARNING&#x60;). | [optional] 
 **score_min** | **float**| Minimum score (inclusive). | [optional] 
 **score_max** | **float**| Maximum score (inclusive). | [optional] 
 **segment_id** | **str**| Return only monitor statuses matched by the given segment&#39;s matchers. Pass &#39;unassigned&#39; to match monitor statuses matched by no segment. Omitted or empty returns the aggregate (unscoped) view. | [optional] 
 **order_by** | [**MonitorStatusOrderBy**](.md)| Field to sort by. | [optional] 
 **sort** | [**SortDirection**](.md)| Sort direction. | [optional] 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Maximum number of items to return. | [optional] [default to 20]

### Return type

[**ListMonitorStatusResponse**](ListMonitorStatusResponse.md)

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

