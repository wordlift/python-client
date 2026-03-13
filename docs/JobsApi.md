# wordlift_client.JobsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job_kpis_graphs_graph_id_jobs_post**](JobsApi.md#create_job_kpis_graphs_graph_id_jobs_post) | **POST** /kpis/graphs/{graph_id}/jobs | Create Job
[**get_job_kpis_graphs_graph_id_jobs_job_id_get**](JobsApi.md#get_job_kpis_graphs_graph_id_jobs_job_id_get) | **GET** /kpis/graphs/{graph_id}/jobs/{job_id} | Get Job


# **create_job_kpis_graphs_graph_id_jobs_post**
> Dict[str, object] create_job_kpis_graphs_graph_id_jobs_post(graph_id, submit_job_body, x_ng_dataset_id=x_ng_dataset_id)

Create Job

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
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
    graph_id = 'graph_id_example' # str | 
    submit_job_body = wordlift_client.SubmitJobBody() # SubmitJobBody | 
    x_ng_dataset_id = 'x_ng_dataset_id_example' # str |  (optional)

    try:
        # Create Job
        api_response = await api_instance.create_job_kpis_graphs_graph_id_jobs_post(graph_id, submit_job_body, x_ng_dataset_id=x_ng_dataset_id)
        print("The response of JobsApi->create_job_kpis_graphs_graph_id_jobs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_job_kpis_graphs_graph_id_jobs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**|  | 
 **submit_job_body** | [**SubmitJobBody**](SubmitJobBody.md)|  | 
 **x_ng_dataset_id** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_kpis_graphs_graph_id_jobs_job_id_get**
> Dict[str, object] get_job_kpis_graphs_graph_id_jobs_job_id_get(graph_id, job_id)

Get Job

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
    api_instance = wordlift_client.JobsApi(api_client)
    graph_id = 'graph_id_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        # Get Job
        api_response = await api_instance.get_job_kpis_graphs_graph_id_jobs_job_id_get(graph_id, job_id)
        print("The response of JobsApi->get_job_kpis_graphs_graph_id_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_kpis_graphs_graph_id_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**|  | 
 **job_id** | **str**|  | 

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

