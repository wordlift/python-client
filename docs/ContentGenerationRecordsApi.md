# wordlift_client.ContentGenerationRecordsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_record**](ContentGenerationRecordsApi.md#get_record) | **GET** /content-generations/{contentGenerationId}/records/{recordId} | Get
[**list_records**](ContentGenerationRecordsApi.md#list_records) | **GET** /content-generations/{contentGenerationId}/records | List
[**list_records_as_events**](ContentGenerationRecordsApi.md#list_records_as_events) | **GET** /content-generations/{contentGenerationId}/records-sse | List as Events
[**update_record**](ContentGenerationRecordsApi.md#update_record) | **PUT** /content-generations/{contentGenerationId}/records/{recordId} | Update
[**update_records**](ContentGenerationRecordsApi.md#update_records) | **PUT** /content-generations/{contentGenerationId}/records | Update
[**update_records_collection**](ContentGenerationRecordsApi.md#update_records_collection) | **PUT** /content-generations/{contentGenerationId}/records-collection | Update


# **get_record**
> Record get_record(content_generation_id, record_id)

Get

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.record import Record
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.ContentGenerationRecordsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    record_id = 56 # int | The Record id.

    try:
        # Get
        api_response = await api_instance.get_record(content_generation_id, record_id)
        print("The response of ContentGenerationRecordsApi->get_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationRecordsApi->get_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **record_id** | **int**| The Record id. | 

### Return type

[**Record**](Record.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_records**
> PageRecord list_records(content_generation_id, cursor=cursor, limit=limit, q=q)

List

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.page_record import PageRecord
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.ContentGenerationRecordsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)
    q = 'q_example' # str | Search query (optional)

    try:
        # List
        api_response = await api_instance.list_records(content_generation_id, cursor=cursor, limit=limit, q=q)
        print("The response of ContentGenerationRecordsApi->list_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationRecordsApi->list_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]
 **q** | **str**| Search query | [optional] 

### Return type

[**PageRecord**](PageRecord.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_records_as_events**
> list_records_as_events(content_generation_id)

List as Events

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.ContentGenerationRecordsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.

    try:
        # List as Events
        await api_instance.list_records_as_events(content_generation_id)
    except Exception as e:
        print("Exception when calling ContentGenerationRecordsApi->list_records_as_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_record**
> Record update_record(content_generation_id, record_id, request2)

Update

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.record import Record
from wordlift_client.models.request2 import Request2
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.ContentGenerationRecordsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    record_id = 56 # int | The Record id.
    request2 = wordlift_client.Request2() # Request2 | 

    try:
        # Update
        api_response = await api_instance.update_record(content_generation_id, record_id, request2)
        print("The response of ContentGenerationRecordsApi->update_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationRecordsApi->update_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **record_id** | **int**| The Record id. | 
 **request2** | [**Request2**](Request2.md)|  | 

### Return type

[**Record**](Record.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_records**
> update_records(content_generation_id, is_accepted, update_records_request)

Update

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.update_records_request import UpdateRecordsRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.ContentGenerationRecordsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    is_accepted = True # bool | Completion accepted
    update_records_request = wordlift_client.UpdateRecordsRequest() # UpdateRecordsRequest | 

    try:
        # Update
        await api_instance.update_records(content_generation_id, is_accepted, update_records_request)
    except Exception as e:
        print("Exception when calling ContentGenerationRecordsApi->update_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **is_accepted** | **bool**| Completion accepted | 
 **update_records_request** | [**UpdateRecordsRequest**](UpdateRecordsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_records_collection**
> List[Record] update_records_collection(content_generation_id, update_record_request)

Update

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.record import Record
from wordlift_client.models.update_record_request import UpdateRecordRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.ContentGenerationRecordsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    update_record_request = [wordlift_client.UpdateRecordRequest()] # List[UpdateRecordRequest] | 

    try:
        # Update
        api_response = await api_instance.update_records_collection(content_generation_id, update_record_request)
        print("The response of ContentGenerationRecordsApi->update_records_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationRecordsApi->update_records_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **update_record_request** | [**List[UpdateRecordRequest]**](UpdateRecordRequest.md)|  | 

### Return type

[**List[Record]**](Record.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

