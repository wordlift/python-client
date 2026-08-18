# wordlift_client.SegmentsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segment_accounts_account_id_monitoring_segments_post**](SegmentsApi.md#create_segment_accounts_account_id_monitoring_segments_post) | **POST** /accounts/{account_id}/monitoring/segments | Create Segment
[**delete_segment_accounts_account_id_monitoring_segments_segment_id_delete**](SegmentsApi.md#delete_segment_accounts_account_id_monitoring_segments_segment_id_delete) | **DELETE** /accounts/{account_id}/monitoring/segments/{segment_id} | Delete Segment
[**get_segment_accounts_account_id_monitoring_segments_segment_id_get**](SegmentsApi.md#get_segment_accounts_account_id_monitoring_segments_segment_id_get) | **GET** /accounts/{account_id}/monitoring/segments/{segment_id} | Get Segment
[**list_segments_accounts_account_id_monitoring_segments_get**](SegmentsApi.md#list_segments_accounts_account_id_monitoring_segments_get) | **GET** /accounts/{account_id}/monitoring/segments | List Segments
[**update_segment_accounts_account_id_monitoring_segments_segment_id_put**](SegmentsApi.md#update_segment_accounts_account_id_monitoring_segments_segment_id_put) | **PUT** /accounts/{account_id}/monitoring/segments/{segment_id} | Update Segment


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
    api_instance = wordlift_client.SegmentsApi(api_client)
    account_id = 'account_id_example' # str | 
    segment_request = wordlift_client.SegmentRequest() # SegmentRequest | 

    try:
        # Create Segment
        api_response = await api_instance.create_segment_accounts_account_id_monitoring_segments_post(account_id, segment_request)
        print("The response of SegmentsApi->create_segment_accounts_account_id_monitoring_segments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->create_segment_accounts_account_id_monitoring_segments_post: %s\n" % e)
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
    api_instance = wordlift_client.SegmentsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Delete Segment
        await api_instance.delete_segment_accounts_account_id_monitoring_segments_segment_id_delete(segment_id, account_id)
    except Exception as e:
        print("Exception when calling SegmentsApi->delete_segment_accounts_account_id_monitoring_segments_segment_id_delete: %s\n" % e)
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
    api_instance = wordlift_client.SegmentsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Get Segment
        api_response = await api_instance.get_segment_accounts_account_id_monitoring_segments_segment_id_get(segment_id, account_id)
        print("The response of SegmentsApi->get_segment_accounts_account_id_monitoring_segments_segment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->get_segment_accounts_account_id_monitoring_segments_segment_id_get: %s\n" % e)
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

# **list_segments_accounts_account_id_monitoring_segments_get**
> ListSegmentsResponse list_segments_accounts_account_id_monitoring_segments_get(account_id, q=q, order_by=order_by, sort=sort, cursor=cursor, limit=limit)

List Segments

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_segments_response import ListSegmentsResponse
from wordlift_client.models.segment_order_by import SegmentOrderBy
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
    api_instance = wordlift_client.SegmentsApi(api_client)
    account_id = 'account_id_example' # str | 
    q = 'q_example' # str | Case-insensitive substring search across name and description. (optional)
    order_by = wordlift_client.SegmentOrderBy() # SegmentOrderBy | Field to sort by. (optional)
    sort = wordlift_client.SortDirection() # SortDirection | Sort direction. (optional)
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 50 # int | Maximum number of segments to return. (optional) (default to 50)

    try:
        # List Segments
        api_response = await api_instance.list_segments_accounts_account_id_monitoring_segments_get(account_id, q=q, order_by=order_by, sort=sort, cursor=cursor, limit=limit)
        print("The response of SegmentsApi->list_segments_accounts_account_id_monitoring_segments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->list_segments_accounts_account_id_monitoring_segments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **q** | **str**| Case-insensitive substring search across name and description. | [optional] 
 **order_by** | [**SegmentOrderBy**](.md)| Field to sort by. | [optional] 
 **sort** | [**SortDirection**](.md)| Sort direction. | [optional] 
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

# **update_segment_accounts_account_id_monitoring_segments_segment_id_put**
> SegmentResponse update_segment_accounts_account_id_monitoring_segments_segment_id_put(segment_id, account_id, segment_request)

Update Segment

Replace the segment's mutable fields.  PUT replaces *every* mutable field; an omitted field is reset to its default. For ``description``, the default is ``null`` — so a body that omits ``description`` clears any existing value. Clients that want to preserve a field must send it explicitly.

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
    api_instance = wordlift_client.SegmentsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    segment_request = wordlift_client.SegmentRequest() # SegmentRequest | 

    try:
        # Update Segment
        api_response = await api_instance.update_segment_accounts_account_id_monitoring_segments_segment_id_put(segment_id, account_id, segment_request)
        print("The response of SegmentsApi->update_segment_accounts_account_id_monitoring_segments_segment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->update_segment_accounts_account_id_monitoring_segments_segment_id_put: %s\n" % e)
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

