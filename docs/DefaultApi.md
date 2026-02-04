# wordlift_client.DefaultApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_resource_monitor_graphs_graph_id_resources_put**](DefaultApi.md#add_resource_monitor_graphs_graph_id_resources_put) | **PUT** /monitor/graphs/{graph_id}/resources | Add Resource
[**get_job_status_monitor_graphs_graph_id_jobs_job_id_get**](DefaultApi.md#get_job_status_monitor_graphs_graph_id_jobs_job_id_get) | **GET** /monitor/graphs/{graph_id}/jobs/{job_id} | Get Job Status
[**get_url_results_monitor_graphs_graph_id_urls_results_get**](DefaultApi.md#get_url_results_monitor_graphs_graph_id_urls_results_get) | **GET** /monitor/graphs/{graph_id}/urls/results | Get Url Results
[**get_url_summary_monitor_graphs_graph_id_urls_summary_get**](DefaultApi.md#get_url_summary_monitor_graphs_graph_id_urls_summary_get) | **GET** /monitor/graphs/{graph_id}/urls/summary | Get Url Summary
[**health_health_get**](DefaultApi.md#health_health_get) | **GET** /health | Health
[**list_graph_urls_monitor_graphs_graph_id_urls_get**](DefaultApi.md#list_graph_urls_monitor_graphs_graph_id_urls_get) | **GET** /monitor/graphs/{graph_id}/urls | List Graph Urls
[**list_jobs_monitor_graphs_graph_id_jobs_get**](DefaultApi.md#list_jobs_monitor_graphs_graph_id_jobs_get) | **GET** /monitor/graphs/{graph_id}/jobs | List Jobs


# **add_resource_monitor_graphs_graph_id_resources_put**
> object add_resource_monitor_graphs_graph_id_resources_put(graph_id, resource_request)

Add Resource

Adds a resource to the graph. If it's a sitemap, triggers a discovery job.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.resource_request import ResourceRequest
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
    graph_id = 'graph_id_example' # str | 
    resource_request = wordlift_client.ResourceRequest() # ResourceRequest | 

    try:
        # Add Resource
        api_response = await api_instance.add_resource_monitor_graphs_graph_id_resources_put(graph_id, resource_request)
        print("The response of DefaultApi->add_resource_monitor_graphs_graph_id_resources_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_resource_monitor_graphs_graph_id_resources_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**|  | 
 **resource_request** | [**ResourceRequest**](ResourceRequest.md)|  | 

### Return type

**object**

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

# **get_job_status_monitor_graphs_graph_id_jobs_job_id_get**
> object get_job_status_monitor_graphs_graph_id_jobs_job_id_get(graph_id, job_id)

Get Job Status

Returns the status and progress of a job. Ensures the job belongs to the graph.

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
    graph_id = 'graph_id_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        # Get Job Status
        api_response = await api_instance.get_job_status_monitor_graphs_graph_id_jobs_job_id_get(graph_id, job_id)
        print("The response of DefaultApi->get_job_status_monitor_graphs_graph_id_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_job_status_monitor_graphs_graph_id_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

**object**

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

# **get_url_results_monitor_graphs_graph_id_urls_results_get**
> UrlResultsResponse get_url_results_monitor_graphs_graph_id_urls_results_get(graph_id, url)

Get Url Results

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.url_results_response import UrlResultsResponse
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
    graph_id = 'graph_id_example' # str | 
    url = 'url_example' # str | 

    try:
        # Get Url Results
        api_response = await api_instance.get_url_results_monitor_graphs_graph_id_urls_results_get(graph_id, url)
        print("The response of DefaultApi->get_url_results_monitor_graphs_graph_id_urls_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_url_results_monitor_graphs_graph_id_urls_results_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**|  | 
 **url** | **str**|  | 

### Return type

[**UrlResultsResponse**](UrlResultsResponse.md)

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

# **get_url_summary_monitor_graphs_graph_id_urls_summary_get**
> UrlSummaryResponse get_url_summary_monitor_graphs_graph_id_urls_summary_get(graph_id, url)

Get Url Summary

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.url_summary_response import UrlSummaryResponse
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
    graph_id = 'graph_id_example' # str | 
    url = 'url_example' # str | 

    try:
        # Get Url Summary
        api_response = await api_instance.get_url_summary_monitor_graphs_graph_id_urls_summary_get(graph_id, url)
        print("The response of DefaultApi->get_url_summary_monitor_graphs_graph_id_urls_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_url_summary_monitor_graphs_graph_id_urls_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**|  | 
 **url** | **str**|  | 

### Return type

[**UrlSummaryResponse**](UrlSummaryResponse.md)

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
> object health_health_get()

Health

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

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_graph_urls_monitor_graphs_graph_id_urls_get**
> UrlListResponse list_graph_urls_monitor_graphs_graph_id_urls_get(graph_id, limit=limit, cursor=cursor, status=status, q=q, var_from=var_from, to=to)

List Graph Urls

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.url_list_response import UrlListResponse
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
    graph_id = 'graph_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    cursor = 'cursor_example' # str |  (optional)
    status = ['status_example'] # List[str] |  (optional)
    q = 'q_example' # str |  (optional)
    var_from = 'var_from_example' # str |  (optional)
    to = 'to_example' # str |  (optional)

    try:
        # List Graph Urls
        api_response = await api_instance.list_graph_urls_monitor_graphs_graph_id_urls_get(graph_id, limit=limit, cursor=cursor, status=status, q=q, var_from=var_from, to=to)
        print("The response of DefaultApi->list_graph_urls_monitor_graphs_graph_id_urls_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_graph_urls_monitor_graphs_graph_id_urls_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **cursor** | **str**|  | [optional] 
 **status** | [**List[str]**](str.md)|  | [optional] 
 **q** | **str**|  | [optional] 
 **var_from** | **str**|  | [optional] 
 **to** | **str**|  | [optional] 

### Return type

[**UrlListResponse**](UrlListResponse.md)

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

# **list_jobs_monitor_graphs_graph_id_jobs_get**
> object list_jobs_monitor_graphs_graph_id_jobs_get(graph_id, limit=limit)

List Jobs

Lists recent jobs for a graph.

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
    graph_id = 'graph_id_example' # str | 
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List Jobs
        api_response = await api_instance.list_jobs_monitor_graphs_graph_id_jobs_get(graph_id, limit=limit)
        print("The response of DefaultApi->list_jobs_monitor_graphs_graph_id_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_jobs_monitor_graphs_graph_id_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

**object**

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

