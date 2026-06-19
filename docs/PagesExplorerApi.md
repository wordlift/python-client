# wordlift_client.PagesExplorerApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_page_artifact_websites_host_pages_page_id_artifacts_artifact_type_get**](PagesExplorerApi.md#get_page_artifact_websites_host_pages_page_id_artifacts_artifact_type_get) | **GET** /websites/{host}/pages/{page_id}/artifacts/{artifact_type} | Get page artifact
[**get_website_page_websites_host_pages_page_id_get**](PagesExplorerApi.md#get_website_page_websites_host_pages_page_id_get) | **GET** /websites/{host}/pages/{page_id} | Get crawled page by host and page id
[**list_website_pages_websites_host_pages_get**](PagesExplorerApi.md#list_website_pages_websites_host_pages_get) | **GET** /websites/{host}/pages | List crawled pages by host
[**query_page_artifacts_websites_host_artifacts_query_post**](PagesExplorerApi.md#query_page_artifacts_websites_host_artifacts_query_post) | **POST** /websites/{host}/artifacts:query | Batch query page artifacts


# **get_page_artifact_websites_host_pages_page_id_artifacts_artifact_type_get**
> WebsitePageArtifactResponse get_page_artifact_websites_host_pages_page_id_artifacts_artifact_type_get(host, page_id, artifact_type, run_id=run_id, as_of=as_of)

Get page artifact

Returns a single page artifact payload (`xhtml` or `markdown`).

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.website_page_artifact_response import WebsitePageArtifactResponse
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
    api_instance = wordlift_client.PagesExplorerApi(api_client)
    host = 'host_example' # str | 
    page_id = 56 # int | 
    artifact_type = 'artifact_type_example' # str | 
    run_id = 'run_id_example' # str |  (optional)
    as_of = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get page artifact
        api_response = await api_instance.get_page_artifact_websites_host_pages_page_id_artifacts_artifact_type_get(host, page_id, artifact_type, run_id=run_id, as_of=as_of)
        print("The response of PagesExplorerApi->get_page_artifact_websites_host_pages_page_id_artifacts_artifact_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesExplorerApi->get_page_artifact_websites_host_pages_page_id_artifacts_artifact_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**|  | 
 **page_id** | **int**|  | 
 **artifact_type** | **str**|  | 
 **run_id** | **str**|  | [optional] 
 **as_of** | **datetime**|  | [optional] 

### Return type

[**WebsitePageArtifactResponse**](WebsitePageArtifactResponse.md)

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

# **get_website_page_websites_host_pages_page_id_get**
> WebsitePageResponse get_website_page_websites_host_pages_page_id_get(host, page_id, run_id=run_id, as_of=as_of)

Get crawled page by host and page id

Returns page metadata and artifact availability flags.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.website_page_response import WebsitePageResponse
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
    api_instance = wordlift_client.PagesExplorerApi(api_client)
    host = 'host_example' # str | 
    page_id = 56 # int | 
    run_id = 'run_id_example' # str |  (optional)
    as_of = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get crawled page by host and page id
        api_response = await api_instance.get_website_page_websites_host_pages_page_id_get(host, page_id, run_id=run_id, as_of=as_of)
        print("The response of PagesExplorerApi->get_website_page_websites_host_pages_page_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesExplorerApi->get_website_page_websites_host_pages_page_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**|  | 
 **page_id** | **int**|  | 
 **run_id** | **str**|  | [optional] 
 **as_of** | **datetime**|  | [optional] 

### Return type

[**WebsitePageResponse**](WebsitePageResponse.md)

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

# **list_website_pages_websites_host_pages_get**
> ResponseListWebsitePagesWebsitesHostPagesGet list_website_pages_websites_host_pages_get(host, limit=limit, offset=offset, cursor=cursor, status=status, url_pattern=url_pattern, url=url, run_id=run_id, as_of=as_of)

List crawled pages by host

Returns crawled pages for a host with optional status, run, time and URL filters. When `url` is provided, returns direct page data in a single response.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.crawl_page_status import CrawlPageStatus
from wordlift_client.models.response_list_website_pages_websites_host_pages_get import ResponseListWebsitePagesWebsitesHostPagesGet
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
    api_instance = wordlift_client.PagesExplorerApi(api_client)
    host = 'host_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    cursor = 56 # int |  (optional)
    status = wordlift_client.CrawlPageStatus() # CrawlPageStatus |  (optional)
    url_pattern = 'url_pattern_example' # str |  (optional)
    url = 'url_example' # str |  (optional)
    run_id = 'run_id_example' # str |  (optional)
    as_of = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # List crawled pages by host
        api_response = await api_instance.list_website_pages_websites_host_pages_get(host, limit=limit, offset=offset, cursor=cursor, status=status, url_pattern=url_pattern, url=url, run_id=run_id, as_of=as_of)
        print("The response of PagesExplorerApi->list_website_pages_websites_host_pages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesExplorerApi->list_website_pages_websites_host_pages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **cursor** | **int**|  | [optional] 
 **status** | [**CrawlPageStatus**](.md)|  | [optional] 
 **url_pattern** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **run_id** | **str**|  | [optional] 
 **as_of** | **datetime**|  | [optional] 

### Return type

[**ResponseListWebsitePagesWebsitesHostPagesGet**](ResponseListWebsitePagesWebsitesHostPagesGet.md)

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

# **query_page_artifacts_websites_host_artifacts_query_post**
> PageArtifactQueryResponse query_page_artifacts_websites_host_artifacts_query_post(host, page_artifact_query_request)

Batch query page artifacts

Returns artifacts for multiple page ids in one request.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.page_artifact_query_request import PageArtifactQueryRequest
from wordlift_client.models.page_artifact_query_response import PageArtifactQueryResponse
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
    api_instance = wordlift_client.PagesExplorerApi(api_client)
    host = 'host_example' # str | 
    page_artifact_query_request = wordlift_client.PageArtifactQueryRequest() # PageArtifactQueryRequest | 

    try:
        # Batch query page artifacts
        api_response = await api_instance.query_page_artifacts_websites_host_artifacts_query_post(host, page_artifact_query_request)
        print("The response of PagesExplorerApi->query_page_artifacts_websites_host_artifacts_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesExplorerApi->query_page_artifacts_websites_host_artifacts_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**|  | 
 **page_artifact_query_request** | [**PageArtifactQueryRequest**](PageArtifactQueryRequest.md)|  | 

### Return type

[**PageArtifactQueryResponse**](PageArtifactQueryResponse.md)

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

