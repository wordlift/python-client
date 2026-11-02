# wordlift_client.JobsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_crawl_job_crawl_jobs_post**](JobsApi.md#create_crawl_job_crawl_jobs_post) | **POST** /crawl-jobs | Create crawl job
[**create_job_kpi_graphs_graph_id_jobs_post**](JobsApi.md#create_job_kpi_graphs_graph_id_jobs_post) | **POST** /kpi/graphs/{graph_id}/jobs | Submit a KPI job
[**get_crawl_job_crawl_jobs_job_id_get**](JobsApi.md#get_crawl_job_crawl_jobs_job_id_get) | **GET** /crawl-jobs/{job_id} | Get crawl job details
[**get_job_kpi_graphs_graph_id_jobs_job_id_get**](JobsApi.md#get_job_kpi_graphs_graph_id_jobs_job_id_get) | **GET** /kpi/graphs/{graph_id}/jobs/{job_id} | Get job status
[**list_crawl_job_pages_crawl_jobs_job_id_pages_get**](JobsApi.md#list_crawl_job_pages_crawl_jobs_job_id_pages_get) | **GET** /crawl-jobs/{job_id}/pages | List crawl job pages
[**list_crawl_jobs_crawl_jobs_get**](JobsApi.md#list_crawl_jobs_crawl_jobs_get) | **GET** /crawl-jobs | List crawl jobs
[**list_jobs_for_graph_kpi_graphs_graph_id_jobs_get**](JobsApi.md#list_jobs_for_graph_kpi_graphs_graph_id_jobs_get) | **GET** /kpi/graphs/{graph_id}/jobs | List jobs for a graph


# **create_crawl_job_crawl_jobs_post**
> CrawlJobCreateResponse create_crawl_job_crawl_jobs_post(crawl_job_input)

Create crawl job

Creates a crawl job and triggers asynchronous execution. The endpoint returns immediately with accepted job metadata.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.crawl_job_create_response import CrawlJobCreateResponse
from wordlift_client.models.crawl_job_input import CrawlJobInput
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
    api_instance = wordlift_client.JobsApi(api_client)
    crawl_job_input = {"website_url":"https://www.example.org/","sitemaps":["https://www.example.org/sitemap.xml"],"discovery_sources":"sitemap-only","js_render_mode":"auto","max_pages":10000,"max_retries":2,"respect_robots":true} # CrawlJobInput | 

    try:
        # Create crawl job
        api_response = await api_instance.create_crawl_job_crawl_jobs_post(crawl_job_input)
        print("The response of JobsApi->create_crawl_job_crawl_jobs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_crawl_job_crawl_jobs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crawl_job_input** | [**CrawlJobInput**](CrawlJobInput.md)|  | 

### Return type

[**CrawlJobCreateResponse**](CrawlJobCreateResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Crawl job accepted for asynchronous processing. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job_kpi_graphs_graph_id_jobs_post**
> JobResponse create_job_kpi_graphs_graph_id_jobs_post(graph_id, submit_job_body)

Submit a KPI job

Creates or reuses a KPI calculation job for the requested graph and snapshot day. When the latest source watermark, worker major.minor version, and validation-policy fingerprint match the newest validated snapshot, the service completes the request immediately by cloning that snapshot instead of running the worker. Set `force_rerun=true` to bypass reuse and require a fresh worker run.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.job_response import JobResponse
from wordlift_client.models.submit_job_body import SubmitJobBody
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
    api_instance = wordlift_client.JobsApi(api_client)
    graph_id = '1506805' # str | Public WordLift graph identifier (`account.id`).
    submit_job_body = wordlift_client.SubmitJobBody() # SubmitJobBody | 

    try:
        # Submit a KPI job
        api_response = await api_instance.create_job_kpi_graphs_graph_id_jobs_post(graph_id, submit_job_body)
        print("The response of JobsApi->create_job_kpi_graphs_graph_id_jobs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_job_kpi_graphs_graph_id_jobs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**| Public WordLift graph identifier (&#x60;account.id&#x60;). | 
 **submit_job_body** | [**SubmitJobBody**](SubmitJobBody.md)|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Job accepted or existing reusable job returned. |  -  |
**400** | The request was syntactically valid but semantically invalid. |  -  |
**403** | The caller is not authorized to operate on the requested graph. |  -  |
**404** | The requested resource was not found. |  -  |
**409** | The request conflicts with current job state or freshness rules. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crawl_job_crawl_jobs_job_id_get**
> CrawlJobResponse get_crawl_job_crawl_jobs_job_id_get(job_id)

Get crawl job details

Returns a single crawl job metadata record (without embedded page payloads).

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.crawl_job_response import CrawlJobResponse
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
    api_instance = wordlift_client.JobsApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get crawl job details
        api_response = await api_instance.get_crawl_job_crawl_jobs_job_id_get(job_id)
        print("The response of JobsApi->get_crawl_job_crawl_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_crawl_job_crawl_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**CrawlJobResponse**](CrawlJobResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Crawl job details. |  -  |
**404** | Crawl job was not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_kpi_graphs_graph_id_jobs_job_id_get**
> JobResponse get_job_kpi_graphs_graph_id_jobs_job_id_get(graph_id, job_id)

Get job status

Returns the current persisted job state, including operational timestamps, stage, heartbeat, counters, and stage timings.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.job_response import JobResponse
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
    api_instance = wordlift_client.JobsApi(api_client)
    graph_id = '1506805' # str | Public WordLift graph identifier (`account.id`).
    job_id = 'job_20260313_5bdaac21' # str | Unique job identifier.

    try:
        # Get job status
        api_response = await api_instance.get_job_kpi_graphs_graph_id_jobs_job_id_get(graph_id, job_id)
        print("The response of JobsApi->get_job_kpi_graphs_graph_id_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_kpi_graphs_graph_id_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**| Public WordLift graph identifier (&#x60;account.id&#x60;). | 
 **job_id** | **str**| Unique job identifier. | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job status. |  -  |
**403** | The caller is not authorized to operate on the requested graph. |  -  |
**404** | The requested resource was not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crawl_job_pages_crawl_jobs_job_id_pages_get**
> CrawlJobPageListResponse list_crawl_job_pages_crawl_jobs_job_id_pages_get(job_id, limit=limit, offset=offset)

List crawl job pages

Returns paginated page summaries for a crawl job without large page artifacts.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.crawl_job_page_list_response import CrawlJobPageListResponse
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
    api_instance = wordlift_client.JobsApi(api_client)
    job_id = 'job_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List crawl job pages
        api_response = await api_instance.list_crawl_job_pages_crawl_jobs_job_id_pages_get(job_id, limit=limit, offset=offset)
        print("The response of JobsApi->list_crawl_job_pages_crawl_jobs_job_id_pages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_crawl_job_pages_crawl_jobs_job_id_pages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**CrawlJobPageListResponse**](CrawlJobPageListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Page summaries. |  -  |
**404** | Crawl job was not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crawl_jobs_crawl_jobs_get**
> CrawlJobListResponse list_crawl_jobs_crawl_jobs_get(limit=limit, offset=offset)

List crawl jobs

Returns crawl jobs ordered by creation time descending (newest first).

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.crawl_job_list_response import CrawlJobListResponse
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
    api_instance = wordlift_client.JobsApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List crawl jobs
        api_response = await api_instance.list_crawl_jobs_crawl_jobs_get(limit=limit, offset=offset)
        print("The response of JobsApi->list_crawl_jobs_crawl_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_crawl_jobs_crawl_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**CrawlJobListResponse**](CrawlJobListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Crawl job summaries. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs_for_graph_kpi_graphs_graph_id_jobs_get**
> JobListResponse list_jobs_for_graph_kpi_graphs_graph_id_jobs_get(graph_id, limit=limit, cursor=cursor)

List jobs for a graph

Returns persisted jobs for one graph ordered by most recently updated first. Use the opaque `cursor` token from a previous page to continue pagination.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.job_list_response import JobListResponse
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
    api_instance = wordlift_client.JobsApi(api_client)
    graph_id = '1506805' # str | Public WordLift graph identifier (`account.id`).
    limit = 56 # int | Maximum number of jobs to return. (optional)
    cursor = 'cursor_example' # str | Opaque cursor returned by a previous page. (optional)

    try:
        # List jobs for a graph
        api_response = await api_instance.list_jobs_for_graph_kpi_graphs_graph_id_jobs_get(graph_id, limit=limit, cursor=cursor)
        print("The response of JobsApi->list_jobs_for_graph_kpi_graphs_graph_id_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_jobs_for_graph_kpi_graphs_graph_id_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**| Public WordLift graph identifier (&#x60;account.id&#x60;). | 
 **limit** | **int**| Maximum number of jobs to return. | [optional] 
 **cursor** | **str**| Opaque cursor returned by a previous page. | [optional] 

### Return type

[**JobListResponse**](JobListResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Graph-specific jobs ordered descending by recency. |  -  |
**403** | The caller is not authorized to operate on the requested graph. |  -  |
**404** | The requested resource was not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

