# wordlift_client.MonitorsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_monitor_accounts_account_id_monitoring_monitors_post**](MonitorsApi.md#add_monitor_accounts_account_id_monitoring_monitors_post) | **POST** /accounts/{account_id}/monitoring/monitors | Add Monitor
[**delete_monitor_accounts_account_id_monitoring_monitors_monitor_id_delete**](MonitorsApi.md#delete_monitor_accounts_account_id_monitoring_monitors_monitor_id_delete) | **DELETE** /accounts/{account_id}/monitoring/monitors/{monitor_id} | Delete Monitor
[**get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get**](MonitorsApi.md#get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get) | **GET** /accounts/{account_id}/monitoring/monitors/{monitor_id} | Get Monitor
[**list_monitors_accounts_account_id_monitoring_monitors_get**](MonitorsApi.md#list_monitors_accounts_account_id_monitoring_monitors_get) | **GET** /accounts/{account_id}/monitoring/monitors | List Monitors
[**replace_monitors_accounts_account_id_monitoring_monitors_put**](MonitorsApi.md#replace_monitors_accounts_account_id_monitoring_monitors_put) | **PUT** /accounts/{account_id}/monitoring/monitors | Replace Monitors
[**update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put**](MonitorsApi.md#update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put) | **PUT** /accounts/{account_id}/monitoring/monitors/{monitor_id} | Update Monitor


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
    api_instance = wordlift_client.MonitorsApi(api_client)
    account_id = 'account_id_example' # str | 
    add_resource_request = wordlift_client.AddResourceRequest() # AddResourceRequest | 

    try:
        # Add Monitor
        api_response = await api_instance.add_monitor_accounts_account_id_monitoring_monitors_post(account_id, add_resource_request)
        print("The response of MonitorsApi->add_monitor_accounts_account_id_monitoring_monitors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorsApi->add_monitor_accounts_account_id_monitoring_monitors_post: %s\n" % e)
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
    api_instance = wordlift_client.MonitorsApi(api_client)
    monitor_id = 'monitor_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Delete Monitor
        await api_instance.delete_monitor_accounts_account_id_monitoring_monitors_monitor_id_delete(monitor_id, account_id)
    except Exception as e:
        print("Exception when calling MonitorsApi->delete_monitor_accounts_account_id_monitoring_monitors_monitor_id_delete: %s\n" % e)
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
    api_instance = wordlift_client.MonitorsApi(api_client)
    monitor_id = 'monitor_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Get Monitor
        api_response = await api_instance.get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get(monitor_id, account_id)
        print("The response of MonitorsApi->get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorsApi->get_monitor_accounts_account_id_monitoring_monitors_monitor_id_get: %s\n" % e)
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

# **list_monitors_accounts_account_id_monitoring_monitors_get**
> ListMonitorsResponse list_monitors_accounts_account_id_monitoring_monitors_get(account_id, status=status, segment_id=segment_id, limit=limit, offset=offset)

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
    api_instance = wordlift_client.MonitorsApi(api_client)
    account_id = 'account_id_example' # str | 
    status = wordlift_client.MonitorStatus() # MonitorStatus | Filter by monitor status. (optional)
    segment_id = 'segment_id_example' # str | Return only monitors whose URL is matched by the given segment's matchers. (optional)
    limit = 100 # int | Maximum number of items to return. (optional) (default to 100)
    offset = 0 # int | Number of items to skip. (optional) (default to 0)

    try:
        # List Monitors
        api_response = await api_instance.list_monitors_accounts_account_id_monitoring_monitors_get(account_id, status=status, segment_id=segment_id, limit=limit, offset=offset)
        print("The response of MonitorsApi->list_monitors_accounts_account_id_monitoring_monitors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorsApi->list_monitors_accounts_account_id_monitoring_monitors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **status** | [**MonitorStatus**](.md)| Filter by monitor status. | [optional] 
 **segment_id** | **str**| Return only monitors whose URL is matched by the given segment&#39;s matchers. | [optional] 
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
    api_instance = wordlift_client.MonitorsApi(api_client)
    account_id = 'account_id_example' # str | 
    replace_monitors_request = wordlift_client.ReplaceMonitorsRequest() # ReplaceMonitorsRequest | 

    try:
        # Replace Monitors
        api_response = await api_instance.replace_monitors_accounts_account_id_monitoring_monitors_put(account_id, replace_monitors_request)
        print("The response of MonitorsApi->replace_monitors_accounts_account_id_monitoring_monitors_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorsApi->replace_monitors_accounts_account_id_monitoring_monitors_put: %s\n" % e)
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
    api_instance = wordlift_client.MonitorsApi(api_client)
    monitor_id = 'monitor_id_example' # str | 
    account_id = 'account_id_example' # str | 
    add_resource_request = wordlift_client.AddResourceRequest() # AddResourceRequest | 

    try:
        # Update Monitor
        api_response = await api_instance.update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put(monitor_id, account_id, add_resource_request)
        print("The response of MonitorsApi->update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorsApi->update_monitor_accounts_account_id_monitoring_monitors_monitor_id_put: %s\n" % e)
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

