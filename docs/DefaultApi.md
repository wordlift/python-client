# wordlift_client.DefaultApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_run_accounts_account_id_monitoring_runs_run_id_delete**](DefaultApi.md#abort_run_accounts_account_id_monitoring_runs_run_id_delete) | **DELETE** /accounts/{account_id}/monitoring/runs/{run_id} | Abort Run
[**add_monitor_accounts_account_id_monitoring_monitors_post**](DefaultApi.md#add_monitor_accounts_account_id_monitoring_monitors_post) | **POST** /accounts/{account_id}/monitoring/monitors | Add Monitor
[**add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post**](DefaultApi.md#add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post) | **POST** /accounts/{account_id}/monitoring/segments/{segment_id}/globs | Add Segment Glob
[**add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post**](DefaultApi.md#add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post) | **POST** /accounts/{account_id}/monitoring/segments/{segment_id}/urls | Add Segment Url
[**create_segment_accounts_account_id_monitoring_segments_post**](DefaultApi.md#create_segment_accounts_account_id_monitoring_segments_post) | **POST** /accounts/{account_id}/monitoring/segments | Create Segment
[**delete_monitor_accounts_account_id_monitoring_monitors_monitor_id_delete**](DefaultApi.md#delete_monitor_accounts_account_id_monitoring_monitors_monitor_id_delete) | **DELETE** /accounts/{account_id}/monitoring/monitors/{monitor_id} | Delete Monitor
[**delete_segment_accounts_account_id_monitoring_segments_segment_id_delete**](DefaultApi.md#delete_segment_accounts_account_id_monitoring_segments_segment_id_delete) | **DELETE** /accounts/{account_id}/monitoring/segments/{segment_id} | Delete Segment
[**delete_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_glob_id_delete**](DefaultApi.md#delete_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_glob_id_delete) | **DELETE** /accounts/{account_id}/monitoring/segments/{segment_id}/globs/{glob_id} | Delete Segment Glob
[**delete_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_url_id_delete**](DefaultApi.md#delete_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_url_id_delete) | **DELETE** /accounts/{account_id}/monitoring/segments/{segment_id}/urls/{url_id} | Delete Segment Url
[**get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get**](DefaultApi.md#get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get) | **GET** /accounts/{account_id}/monitoring/monitors/{monitor_id}/checks/{check_name} | Get Check Timeseries
[**get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get**](DefaultApi.md#get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get) | **GET** /accounts/{account_id}/monitoring/monitors/{monitor_id} | Get Monitor
[**get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get**](DefaultApi.md#get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get) | **GET** /accounts/{account_id}/monitoring/monitors/{monitor_id}/status | Get Monitor Status
[**get_run_accounts_account_id_monitoring_runs_run_id_get**](DefaultApi.md#get_run_accounts_account_id_monitoring_runs_run_id_get) | **GET** /accounts/{account_id}/monitoring/runs/{run_id} | Get Run
[**get_segment_accounts_account_id_monitoring_segments_segment_id_get**](DefaultApi.md#get_segment_accounts_account_id_monitoring_segments_segment_id_get) | **GET** /accounts/{account_id}/monitoring/segments/{segment_id} | Get Segment
[**health_health_get**](DefaultApi.md#health_health_get) | **GET** /health | Health
[**list_monitor_statuses_accounts_account_id_monitoring_status_get**](DefaultApi.md#list_monitor_statuses_accounts_account_id_monitoring_status_get) | **GET** /accounts/{account_id}/monitoring/status | List Monitor Statuses
[**list_monitors_accounts_account_id_monitoring_monitors_get**](DefaultApi.md#list_monitors_accounts_account_id_monitoring_monitors_get) | **GET** /accounts/{account_id}/monitoring/monitors | List Monitors
[**list_runs_accounts_account_id_monitoring_runs_get**](DefaultApi.md#list_runs_accounts_account_id_monitoring_runs_get) | **GET** /accounts/{account_id}/monitoring/runs | List Runs
[**list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get**](DefaultApi.md#list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get) | **GET** /accounts/{account_id}/monitoring/segments/{segment_id}/globs | List Segment Globs
[**list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get**](DefaultApi.md#list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get) | **GET** /accounts/{account_id}/monitoring/segments/{segment_id}/urls | List Segment Urls
[**list_segments_accounts_account_id_monitoring_segments_get**](DefaultApi.md#list_segments_accounts_account_id_monitoring_segments_get) | **GET** /accounts/{account_id}/monitoring/segments | List Segments
[**readiness_health_ready_get**](DefaultApi.md#readiness_health_ready_get) | **GET** /health/ready | Readiness
[**replace_monitors_accounts_account_id_monitoring_monitors_put**](DefaultApi.md#replace_monitors_accounts_account_id_monitoring_monitors_put) | **PUT** /accounts/{account_id}/monitoring/monitors | Replace Monitors
[**replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put**](DefaultApi.md#replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put) | **PUT** /accounts/{account_id}/monitoring/segments/{segment_id}/globs | Replace Segment Globs
[**replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put**](DefaultApi.md#replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put) | **PUT** /accounts/{account_id}/monitoring/segments/{segment_id}/urls | Replace Segment Urls
[**update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put**](DefaultApi.md#update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put) | **PUT** /accounts/{account_id}/monitoring/monitors/{monitor_id} | Update Monitor
[**update_segment_accounts_account_id_monitoring_segments_segment_id_put**](DefaultApi.md#update_segment_accounts_account_id_monitoring_segments_segment_id_put) | **PUT** /accounts/{account_id}/monitoring/segments/{segment_id} | Update Segment


# **abort_run_accounts_account_id_monitoring_runs_run_id_delete**
> RunResponse abort_run_accounts_account_id_monitoring_runs_run_id_delete(run_id, account_id)

Abort Run

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
    api_instance = wordlift_client.DefaultApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Abort Run
        api_response = await api_instance.abort_run_accounts_account_id_monitoring_runs_run_id_delete(run_id, account_id)
        print("The response of DefaultApi->abort_run_accounts_account_id_monitoring_runs_run_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->abort_run_accounts_account_id_monitoring_runs_run_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 

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

# **add_monitor_accounts_account_id_monitoring_monitors_post**
> MonitorResponse add_monitor_accounts_account_id_monitoring_monitors_post(account_id, add_resource_request)

Add Monitor

Adds a URL to the monitoring list for the given account.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.add_resource_request import AddResourceRequest
from wordlift_client.models.monitor_response import MonitorResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    add_resource_request = wordlift_client.AddResourceRequest() # AddResourceRequest | 

    try:
        # Add Monitor
        api_response = await api_instance.add_monitor_accounts_account_id_monitoring_monitors_post(account_id, add_resource_request)
        print("The response of DefaultApi->add_monitor_accounts_account_id_monitoring_monitors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_monitor_accounts_account_id_monitoring_monitors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **add_resource_request** | [**AddResourceRequest**](AddResourceRequest.md)|  | 

### Return type

[**MonitorResponse**](MonitorResponse.md)

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

# **add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post**
> SegmentGlobResponse add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post(segment_id, account_id, add_segment_glob_request)

Add Segment Glob

Add a single glob matcher; idempotent on duplicate.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.add_segment_glob_request import AddSegmentGlobRequest
from wordlift_client.models.segment_glob_response import SegmentGlobResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    add_segment_glob_request = wordlift_client.AddSegmentGlobRequest() # AddSegmentGlobRequest | 

    try:
        # Add Segment Glob
        api_response = await api_instance.add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post(segment_id, account_id, add_segment_glob_request)
        print("The response of DefaultApi->add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 
 **add_segment_glob_request** | [**AddSegmentGlobRequest**](AddSegmentGlobRequest.md)|  | 

### Return type

[**SegmentGlobResponse**](SegmentGlobResponse.md)

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

# **add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post**
> SegmentUrlResponse add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post(segment_id, account_id)

Add Segment Url

Add a single URL matcher; idempotent on duplicate.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.segment_url_response import SegmentUrlResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Add Segment Url
        api_response = await api_instance.add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post(segment_id, account_id)
        print("The response of DefaultApi->add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**SegmentUrlResponse**](SegmentUrlResponse.md)

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

# **create_segment_accounts_account_id_monitoring_segments_post**
> SegmentResponse create_segment_accounts_account_id_monitoring_segments_post(account_id, segment_request)

Create Segment

Create a segment for the account.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.segment_request import SegmentRequest
from wordlift_client.models.segment_response import SegmentResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    segment_request = wordlift_client.SegmentRequest() # SegmentRequest | 

    try:
        # Create Segment
        api_response = await api_instance.create_segment_accounts_account_id_monitoring_segments_post(account_id, segment_request)
        print("The response of DefaultApi->create_segment_accounts_account_id_monitoring_segments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_segment_accounts_account_id_monitoring_segments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **segment_request** | [**SegmentRequest**](SegmentRequest.md)|  | 

### Return type

[**SegmentResponse**](SegmentResponse.md)

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

# **delete_monitor_accounts_account_id_monitoring_monitors_monitor_id_delete**
> delete_monitor_accounts_account_id_monitoring_monitors_monitor_id_delete(monitor_id, account_id)

Delete Monitor

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
    api_instance = wordlift_client.DefaultApi(api_client)
    monitor_id = 'monitor_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Delete Monitor
        await api_instance.delete_monitor_accounts_account_id_monitoring_monitors_monitor_id_delete(monitor_id, account_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_monitor_accounts_account_id_monitoring_monitors_monitor_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **str**|  | 
 **account_id** | **str**|  | 

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

# **delete_segment_accounts_account_id_monitoring_segments_segment_id_delete**
> delete_segment_accounts_account_id_monitoring_segments_segment_id_delete(segment_id, account_id)

Delete Segment

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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Delete Segment
        await api_instance.delete_segment_accounts_account_id_monitoring_segments_segment_id_delete(segment_id, account_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_segment_accounts_account_id_monitoring_segments_segment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 

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

# **delete_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_glob_id_delete**
> delete_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_glob_id_delete(segment_id, glob_id, account_id)

Delete Segment Glob

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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    glob_id = 'glob_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Delete Segment Glob
        await api_instance.delete_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_glob_id_delete(segment_id, glob_id, account_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_glob_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **glob_id** | **str**|  | 
 **account_id** | **str**|  | 

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

# **delete_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_url_id_delete**
> delete_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_url_id_delete(segment_id, url_id, account_id)

Delete Segment Url

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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    url_id = 'url_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Delete Segment Url
        await api_instance.delete_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_url_id_delete(segment_id, url_id, account_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_url_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **url_id** | **str**|  | 
 **account_id** | **str**|  | 

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
    api_instance = wordlift_client.DefaultApi(api_client)
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
        print("The response of DefaultApi->get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_check_timeseries_accounts_account_id_monitoring_monitors_monitor_id_checks_check_name_get: %s\n" % e)
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

# **get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get**
> MonitorResponse get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get(monitor_id, account_id)

Get Monitor

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.monitor_response import MonitorResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    monitor_id = 'monitor_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Get Monitor
        api_response = await api_instance.get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get(monitor_id, account_id)
        print("The response of DefaultApi->get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**MonitorResponse**](MonitorResponse.md)

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
> MonitorStatusResponse get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get(monitor_id, account_id)

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
    api_instance = wordlift_client.DefaultApi(api_client)
    monitor_id = 'monitor_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Get Monitor Status
        api_response = await api_instance.get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get(monitor_id, account_id)
        print("The response of DefaultApi->get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_monitor_status_accounts_account_id_monitoring_monitors_monitor_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **str**|  | 
 **account_id** | **str**|  | 

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

# **get_run_accounts_account_id_monitoring_runs_run_id_get**
> RunResponse get_run_accounts_account_id_monitoring_runs_run_id_get(run_id, account_id)

Get Run

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
    api_instance = wordlift_client.DefaultApi(api_client)
    run_id = 'run_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Get Run
        api_response = await api_instance.get_run_accounts_account_id_monitoring_runs_run_id_get(run_id, account_id)
        print("The response of DefaultApi->get_run_accounts_account_id_monitoring_runs_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_run_accounts_account_id_monitoring_runs_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **account_id** | **str**|  | 

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

# **get_segment_accounts_account_id_monitoring_segments_segment_id_get**
> SegmentResponse get_segment_accounts_account_id_monitoring_segments_segment_id_get(segment_id, account_id)

Get Segment

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.segment_response import SegmentResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Get Segment
        api_response = await api_instance.get_segment_accounts_account_id_monitoring_segments_segment_id_get(segment_id, account_id)
        print("The response of DefaultApi->get_segment_accounts_account_id_monitoring_segments_segment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_segment_accounts_account_id_monitoring_segments_segment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**SegmentResponse**](SegmentResponse.md)

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

# **health_health_get**
> HealthResponse health_health_get()

Health

### Example


```python
import wordlift_client
from wordlift_client.models.health_response import HealthResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)

    try:
        # Health
        api_response = await api_instance.health_health_get()
        print("The response of DefaultApi->health_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_monitor_statuses_accounts_account_id_monitoring_status_get**
> ListMonitorStatusResponse list_monitor_statuses_accounts_account_id_monitoring_status_get(account_id, url=url, status=status, score_min=score_min, score_max=score_max, order_by=order_by, sort=sort, cursor=cursor, limit=limit)

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
    api_instance = wordlift_client.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    url = 'url_example' # str | Glob pattern to filter by URL (e.g. `*example.com*`). (optional)
    status = [wordlift_client.MonitorStatusCheckStatus()] # List[MonitorStatusCheckStatus] | Filter by check status (repeatable, e.g. `?status=ERROR&status=WARNING`). (optional)
    score_min = 3.4 # float | Minimum score (inclusive). (optional)
    score_max = 3.4 # float | Maximum score (inclusive). (optional)
    order_by = wordlift_client.MonitorStatusOrderBy() # MonitorStatusOrderBy | Field to sort by. (optional)
    sort = wordlift_client.SortDirection() # SortDirection | Sort direction. (optional)
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 20 # int | Maximum number of items to return. (optional) (default to 20)

    try:
        # List Monitor Statuses
        api_response = await api_instance.list_monitor_statuses_accounts_account_id_monitoring_status_get(account_id, url=url, status=status, score_min=score_min, score_max=score_max, order_by=order_by, sort=sort, cursor=cursor, limit=limit)
        print("The response of DefaultApi->list_monitor_statuses_accounts_account_id_monitoring_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_monitor_statuses_accounts_account_id_monitoring_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **url** | **str**| Glob pattern to filter by URL (e.g. &#x60;*example.com*&#x60;). | [optional] 
 **status** | [**List[MonitorStatusCheckStatus]**](MonitorStatusCheckStatus.md)| Filter by check status (repeatable, e.g. &#x60;?status&#x3D;ERROR&amp;status&#x3D;WARNING&#x60;). | [optional] 
 **score_min** | **float**| Minimum score (inclusive). | [optional] 
 **score_max** | **float**| Maximum score (inclusive). | [optional] 
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

# **list_monitors_accounts_account_id_monitoring_monitors_get**
> ListMonitorsResponse list_monitors_accounts_account_id_monitoring_monitors_get(account_id, status=status, limit=limit, offset=offset)

List Monitors

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_monitors_response import ListMonitorsResponse
from wordlift_client.models.monitor_status import MonitorStatus
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
    api_instance = wordlift_client.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    status = wordlift_client.MonitorStatus() # MonitorStatus | Filter by monitor status. (optional)
    limit = 100 # int | Maximum number of items to return. (optional) (default to 100)
    offset = 0 # int | Number of items to skip. (optional) (default to 0)

    try:
        # List Monitors
        api_response = await api_instance.list_monitors_accounts_account_id_monitoring_monitors_get(account_id, status=status, limit=limit, offset=offset)
        print("The response of DefaultApi->list_monitors_accounts_account_id_monitoring_monitors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_monitors_accounts_account_id_monitoring_monitors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **status** | [**MonitorStatus**](.md)| Filter by monitor status. | [optional] 
 **limit** | **int**| Maximum number of items to return. | [optional] [default to 100]
 **offset** | **int**| Number of items to skip. | [optional] [default to 0]

### Return type

[**ListMonitorsResponse**](ListMonitorsResponse.md)

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
    api_instance = wordlift_client.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    limit = 5 # int | Maximum number of items to return. (optional) (default to 5)
    offset = 0 # int | Number of items to skip. (optional) (default to 0)

    try:
        # List Runs
        api_response = await api_instance.list_runs_accounts_account_id_monitoring_runs_get(account_id, limit=limit, offset=offset)
        print("The response of DefaultApi->list_runs_accounts_account_id_monitoring_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_runs_accounts_account_id_monitoring_runs_get: %s\n" % e)
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

# **list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get**
> ListSegmentGlobsResponse list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get(segment_id, account_id, cursor=cursor, limit=limit)

List Segment Globs

Return a page of glob matchers, ordered by ``(created_at, id)``.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_segment_globs_response import ListSegmentGlobsResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 100 # int | Max glob matchers per page. (optional) (default to 100)

    try:
        # List Segment Globs
        api_response = await api_instance.list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get(segment_id, account_id, cursor=cursor, limit=limit)
        print("The response of DefaultApi->list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Max glob matchers per page. | [optional] [default to 100]

### Return type

[**ListSegmentGlobsResponse**](ListSegmentGlobsResponse.md)

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

# **list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get**
> ListSegmentUrlsResponse list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get(segment_id, account_id, cursor=cursor, limit=limit)

List Segment Urls

Return a page of URL matchers, ordered by ``(created_at, id)``.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_segment_urls_response import ListSegmentUrlsResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 100 # int | Max URL matchers per page. (optional) (default to 100)

    try:
        # List Segment Urls
        api_response = await api_instance.list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get(segment_id, account_id, cursor=cursor, limit=limit)
        print("The response of DefaultApi->list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Max URL matchers per page. | [optional] [default to 100]

### Return type

[**ListSegmentUrlsResponse**](ListSegmentUrlsResponse.md)

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

# **list_segments_accounts_account_id_monitoring_segments_get**
> ListSegmentsResponse list_segments_accounts_account_id_monitoring_segments_get(account_id, cursor=cursor, limit=limit)

List Segments

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_segments_response import ListSegmentsResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 50 # int | Maximum number of segments to return. (optional) (default to 50)

    try:
        # List Segments
        api_response = await api_instance.list_segments_accounts_account_id_monitoring_segments_get(account_id, cursor=cursor, limit=limit)
        print("The response of DefaultApi->list_segments_accounts_account_id_monitoring_segments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_segments_accounts_account_id_monitoring_segments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Maximum number of segments to return. | [optional] [default to 50]

### Return type

[**ListSegmentsResponse**](ListSegmentsResponse.md)

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

# **readiness_health_ready_get**
> ReadinessResponse readiness_health_ready_get()

Readiness

### Example


```python
import wordlift_client
from wordlift_client.models.readiness_response import ReadinessResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)

    try:
        # Readiness
        api_response = await api_instance.readiness_health_ready_get()
        print("The response of DefaultApi->readiness_health_ready_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->readiness_health_ready_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReadinessResponse**](ReadinessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_monitors_accounts_account_id_monitoring_monitors_put**
> List[MonitorResponse] replace_monitors_accounts_account_id_monitoring_monitors_put(account_id, replace_monitors_request)

Replace Monitors

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.monitor_response import MonitorResponse
from wordlift_client.models.replace_monitors_request import ReplaceMonitorsRequest
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
    api_instance = wordlift_client.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    replace_monitors_request = wordlift_client.ReplaceMonitorsRequest() # ReplaceMonitorsRequest | 

    try:
        # Replace Monitors
        api_response = await api_instance.replace_monitors_accounts_account_id_monitoring_monitors_put(account_id, replace_monitors_request)
        print("The response of DefaultApi->replace_monitors_accounts_account_id_monitoring_monitors_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->replace_monitors_accounts_account_id_monitoring_monitors_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **replace_monitors_request** | [**ReplaceMonitorsRequest**](ReplaceMonitorsRequest.md)|  | 

### Return type

[**List[MonitorResponse]**](MonitorResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put**
> List[SegmentGlobResponse] replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put(segment_id, account_id, replace_segment_globs_request)

Replace Segment Globs

Wholesale replace all glob matchers for the segment.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.replace_segment_globs_request import ReplaceSegmentGlobsRequest
from wordlift_client.models.segment_glob_response import SegmentGlobResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    replace_segment_globs_request = wordlift_client.ReplaceSegmentGlobsRequest() # ReplaceSegmentGlobsRequest | 

    try:
        # Replace Segment Globs
        api_response = await api_instance.replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put(segment_id, account_id, replace_segment_globs_request)
        print("The response of DefaultApi->replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 
 **replace_segment_globs_request** | [**ReplaceSegmentGlobsRequest**](ReplaceSegmentGlobsRequest.md)|  | 

### Return type

[**List[SegmentGlobResponse]**](SegmentGlobResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put**
> List[SegmentUrlResponse] replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put(segment_id, account_id)

Replace Segment Urls

Wholesale replace all URL matchers for the segment.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.segment_url_response import SegmentUrlResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Replace Segment Urls
        api_response = await api_instance.replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put(segment_id, account_id)
        print("The response of DefaultApi->replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**List[SegmentUrlResponse]**](SegmentUrlResponse.md)

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

# **update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put**
> MonitorResponse update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put(monitor_id, account_id, add_resource_request)

Update Monitor

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.add_resource_request import AddResourceRequest
from wordlift_client.models.monitor_response import MonitorResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    monitor_id = 'monitor_id_example' # str | 
    account_id = 'account_id_example' # str | 
    add_resource_request = wordlift_client.AddResourceRequest() # AddResourceRequest | 

    try:
        # Update Monitor
        api_response = await api_instance.update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put(monitor_id, account_id, add_resource_request)
        print("The response of DefaultApi->update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **str**|  | 
 **account_id** | **str**|  | 
 **add_resource_request** | [**AddResourceRequest**](AddResourceRequest.md)|  | 

### Return type

[**MonitorResponse**](MonitorResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_segment_accounts_account_id_monitoring_segments_segment_id_put**
> SegmentResponse update_segment_accounts_account_id_monitoring_segments_segment_id_put(segment_id, account_id, segment_request)

Update Segment

Replace the segment's mutable fields.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.segment_request import SegmentRequest
from wordlift_client.models.segment_response import SegmentResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    segment_request = wordlift_client.SegmentRequest() # SegmentRequest | 

    try:
        # Update Segment
        api_response = await api_instance.update_segment_accounts_account_id_monitoring_segments_segment_id_put(segment_id, account_id, segment_request)
        print("The response of DefaultApi->update_segment_accounts_account_id_monitoring_segments_segment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_segment_accounts_account_id_monitoring_segments_segment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 
 **segment_request** | [**SegmentRequest**](SegmentRequest.md)|  | 

### Return type

[**SegmentResponse**](SegmentResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

