# wordlift_client.SegmentGlobsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post**](SegmentGlobsApi.md#add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post) | **POST** /accounts/{account_id}/monitoring/segments/{segment_id}/globs | Add Segment Glob
[**delete_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_glob_id_delete**](SegmentGlobsApi.md#delete_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_glob_id_delete) | **DELETE** /accounts/{account_id}/monitoring/segments/{segment_id}/globs/{glob_id} | Delete Segment Glob
[**list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get**](SegmentGlobsApi.md#list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get) | **GET** /accounts/{account_id}/monitoring/segments/{segment_id}/globs | List Segment Globs
[**replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put**](SegmentGlobsApi.md#replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put) | **PUT** /accounts/{account_id}/monitoring/segments/{segment_id}/globs | Replace Segment Globs


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
    api_instance = wordlift_client.SegmentGlobsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    add_segment_glob_request = wordlift_client.AddSegmentGlobRequest() # AddSegmentGlobRequest | 

    try:
        # Add Segment Glob
        api_response = await api_instance.add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post(segment_id, account_id, add_segment_glob_request)
        print("The response of SegmentGlobsApi->add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentGlobsApi->add_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_post: %s\n" % e)
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
    api_instance = wordlift_client.SegmentGlobsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    glob_id = 'glob_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Delete Segment Glob
        await api_instance.delete_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_glob_id_delete(segment_id, glob_id, account_id)
    except Exception as e:
        print("Exception when calling SegmentGlobsApi->delete_segment_glob_accounts_account_id_monitoring_segments_segment_id_globs_glob_id_delete: %s\n" % e)
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
    api_instance = wordlift_client.SegmentGlobsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 100 # int | Max glob matchers per page. (optional) (default to 100)

    try:
        # List Segment Globs
        api_response = await api_instance.list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get(segment_id, account_id, cursor=cursor, limit=limit)
        print("The response of SegmentGlobsApi->list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentGlobsApi->list_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_get: %s\n" % e)
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
    api_instance = wordlift_client.SegmentGlobsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    replace_segment_globs_request = wordlift_client.ReplaceSegmentGlobsRequest() # ReplaceSegmentGlobsRequest | 

    try:
        # Replace Segment Globs
        api_response = await api_instance.replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put(segment_id, account_id, replace_segment_globs_request)
        print("The response of SegmentGlobsApi->replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentGlobsApi->replace_segment_globs_accounts_account_id_monitoring_segments_segment_id_globs_put: %s\n" % e)
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

