# wordlift_client.SegmentURLsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post**](SegmentURLsApi.md#add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post) | **POST** /accounts/{account_id}/monitoring/segments/{segment_id}/urls | Add Segment Url
[**delete_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_url_id_delete**](SegmentURLsApi.md#delete_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_url_id_delete) | **DELETE** /accounts/{account_id}/monitoring/segments/{segment_id}/urls/{url_id} | Delete Segment Url
[**list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get**](SegmentURLsApi.md#list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get) | **GET** /accounts/{account_id}/monitoring/segments/{segment_id}/urls | List Segment Urls
[**replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put**](SegmentURLsApi.md#replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put) | **PUT** /accounts/{account_id}/monitoring/segments/{segment_id}/urls | Replace Segment Urls


# **add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post**
> SegmentUrlResponse add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post(segment_id, account_id, add_segment_url_request)

Add Segment Url

Add a single URL matcher; idempotent on duplicate.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.add_segment_url_request import AddSegmentUrlRequest
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
    api_instance = wordlift_client.SegmentURLsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    add_segment_url_request = wordlift_client.AddSegmentUrlRequest() # AddSegmentUrlRequest | 

    try:
        # Add Segment Url
        api_response = await api_instance.add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post(segment_id, account_id, add_segment_url_request)
        print("The response of SegmentURLsApi->add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentURLsApi->add_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 
 **add_segment_url_request** | [**AddSegmentUrlRequest**](AddSegmentUrlRequest.md)|  | 

### Return type

[**SegmentUrlResponse**](SegmentUrlResponse.md)

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
    api_instance = wordlift_client.SegmentURLsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    url_id = 'url_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Delete Segment Url
        await api_instance.delete_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_url_id_delete(segment_id, url_id, account_id)
    except Exception as e:
        print("Exception when calling SegmentURLsApi->delete_segment_url_accounts_account_id_monitoring_segments_segment_id_urls_url_id_delete: %s\n" % e)
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
    api_instance = wordlift_client.SegmentURLsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 100 # int | Max URL matchers per page. (optional) (default to 100)

    try:
        # List Segment Urls
        api_response = await api_instance.list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get(segment_id, account_id, cursor=cursor, limit=limit)
        print("The response of SegmentURLsApi->list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentURLsApi->list_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_get: %s\n" % e)
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

# **replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put**
> List[SegmentUrlResponse] replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put(segment_id, account_id, replace_segment_urls_request)

Replace Segment Urls

Wholesale replace all URL matchers for the segment.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.replace_segment_urls_request import ReplaceSegmentUrlsRequest
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
    api_instance = wordlift_client.SegmentURLsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    replace_segment_urls_request = wordlift_client.ReplaceSegmentUrlsRequest() # ReplaceSegmentUrlsRequest | 

    try:
        # Replace Segment Urls
        api_response = await api_instance.replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put(segment_id, account_id, replace_segment_urls_request)
        print("The response of SegmentURLsApi->replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentURLsApi->replace_segment_urls_accounts_account_id_monitoring_segments_segment_id_urls_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 
 **replace_segment_urls_request** | [**ReplaceSegmentUrlsRequest**](ReplaceSegmentUrlsRequest.md)|  | 

### Return type

[**List[SegmentUrlResponse]**](SegmentUrlResponse.md)

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

