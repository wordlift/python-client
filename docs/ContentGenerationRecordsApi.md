# wordlift-client.ContentGenerationRecordsApi

All URIs are relative to *https://api.wordlift.io/analysis*

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


```python
import wordlift-client
from wordlift-client.models.record import Record
from wordlift-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift-client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift-client.ContentGenerationRecordsApi(api_client)
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

No authorization required

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


```python
import wordlift-client
from wordlift-client.models.page_record import PageRecord
from wordlift-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift-client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift-client.ContentGenerationRecordsApi(api_client)
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

No authorization required

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


```python
import wordlift-client
from wordlift-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift-client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift-client.ContentGenerationRecordsApi(api_client)
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

No authorization required

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
> Record update_record(content_generation_id, record_id, request1)

Update

### Example


```python
import wordlift-client
from wordlift-client.models.record import Record
from wordlift-client.models.request1 import Request1
from wordlift-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift-client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift-client.ContentGenerationRecordsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    record_id = 56 # int | The Record id.
    request1 = wordlift-client.Request1() # Request1 | 

    try:
        # Update
        api_response = await api_instance.update_record(content_generation_id, record_id, request1)
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
 **request1** | [**Request1**](Request1.md)|  | 

### Return type

[**Record**](Record.md)

### Authorization

No authorization required

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


```python
import wordlift-client
from wordlift-client.models.update_records_request import UpdateRecordsRequest
from wordlift-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift-client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift-client.ContentGenerationRecordsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    is_accepted = True # bool | Completion accepted
    update_records_request = wordlift-client.UpdateRecordsRequest() # UpdateRecordsRequest | 

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

No authorization required

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


```python
import wordlift-client
from wordlift-client.models.record import Record
from wordlift-client.models.update_record_request import UpdateRecordRequest
from wordlift-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift-client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift-client.ContentGenerationRecordsApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    update_record_request = [wordlift-client.UpdateRecordRequest()] # List[UpdateRecordRequest] | 

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

No authorization required

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

