# wordlift_client.ExpectationsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_put**](ExpectationsApi.md#attach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_put) | **PUT** /accounts/{account_id}/monitoring/expectations/{expectation_id}/segments/{segment_id} | Attach Expectation Segment
[**create_expectation_accounts_account_id_monitoring_expectations_post**](ExpectationsApi.md#create_expectation_accounts_account_id_monitoring_expectations_post) | **POST** /accounts/{account_id}/monitoring/expectations | Create Expectation
[**delete_expectation_accounts_account_id_monitoring_expectations_expectation_id_delete**](ExpectationsApi.md#delete_expectation_accounts_account_id_monitoring_expectations_expectation_id_delete) | **DELETE** /accounts/{account_id}/monitoring/expectations/{expectation_id} | Delete Expectation
[**detach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_delete**](ExpectationsApi.md#detach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_delete) | **DELETE** /accounts/{account_id}/monitoring/expectations/{expectation_id}/segments/{segment_id} | Detach Expectation Segment
[**get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get**](ExpectationsApi.md#get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get) | **GET** /accounts/{account_id}/monitoring/expectations/{expectation_id} | Get Expectation
[**list_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_get**](ExpectationsApi.md#list_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_get) | **GET** /accounts/{account_id}/monitoring/expectations/{expectation_id}/segments | List Expectation Segments
[**list_expectations_accounts_account_id_monitoring_expectations_get**](ExpectationsApi.md#list_expectations_accounts_account_id_monitoring_expectations_get) | **GET** /accounts/{account_id}/monitoring/expectations | List Expectations
[**list_segment_expectations_accounts_account_id_monitoring_segments_segment_id_expectations_get**](ExpectationsApi.md#list_segment_expectations_accounts_account_id_monitoring_segments_segment_id_expectations_get) | **GET** /accounts/{account_id}/monitoring/segments/{segment_id}/expectations | List Segment Expectations
[**replace_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_put**](ExpectationsApi.md#replace_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_put) | **PUT** /accounts/{account_id}/monitoring/expectations/{expectation_id}/segments | Replace Expectation Segments


# **attach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_put**
> SegmentSeverityResponse attach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_put(expectation_id, segment_id, account_id, attach_expectation_segment_request)

Attach Expectation Segment

Attach a segment to a rule with the given severity. Idempotent — a repeated attach updates the severity. Returns confirmation of what was written — the caller already has both fields, and no endpoint on this resource hydrates the full segment (see the segment catalog for that).

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.attach_expectation_segment_request import AttachExpectationSegmentRequest
from wordlift_client.models.segment_severity_response import SegmentSeverityResponse
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
    api_instance = wordlift_client.ExpectationsApi(api_client)
    expectation_id = 'expectation_id_example' # str | 
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    attach_expectation_segment_request = wordlift_client.AttachExpectationSegmentRequest() # AttachExpectationSegmentRequest | 

    try:
        # Attach Expectation Segment
        api_response = await api_instance.attach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_put(expectation_id, segment_id, account_id, attach_expectation_segment_request)
        print("The response of ExpectationsApi->attach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpectationsApi->attach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expectation_id** | **str**|  | 
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 
 **attach_expectation_segment_request** | [**AttachExpectationSegmentRequest**](AttachExpectationSegmentRequest.md)|  | 

### Return type

[**SegmentSeverityResponse**](SegmentSeverityResponse.md)

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

# **create_expectation_accounts_account_id_monitoring_expectations_post**
> Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost create_expectation_accounts_account_id_monitoring_expectations_post(account_id, body)

Create Expectation

Create a rule. Idempotent on conflict: an identical (type, config) rule returns the existing rule with 200; a new rule returns 201. Attachments (and their severity) are managed via the segments sub-resource.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.body import Body
from wordlift_client.models.response200_create_expectation_accounts_account_id_monitoring_expectations_post import Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost
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
    api_instance = wordlift_client.ExpectationsApi(api_client)
    account_id = 'account_id_example' # str | 
    body = wordlift_client.Body() # Body | 

    try:
        # Create Expectation
        api_response = await api_instance.create_expectation_accounts_account_id_monitoring_expectations_post(account_id, body)
        print("The response of ExpectationsApi->create_expectation_accounts_account_id_monitoring_expectations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpectationsApi->create_expectation_accounts_account_id_monitoring_expectations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

[**Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost**](Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An identical (type, config) rule already existed |  -  |
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_expectation_accounts_account_id_monitoring_expectations_expectation_id_delete**
> delete_expectation_accounts_account_id_monitoring_expectations_expectation_id_delete(expectation_id, account_id)

Delete Expectation

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
    api_instance = wordlift_client.ExpectationsApi(api_client)
    expectation_id = 'expectation_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Delete Expectation
        await api_instance.delete_expectation_accounts_account_id_monitoring_expectations_expectation_id_delete(expectation_id, account_id)
    except Exception as e:
        print("Exception when calling ExpectationsApi->delete_expectation_accounts_account_id_monitoring_expectations_expectation_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expectation_id** | **str**|  | 
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

# **detach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_delete**
> detach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_delete(expectation_id, segment_id, account_id)

Detach Expectation Segment

Detach a segment from a rule. Idempotent.

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
    api_instance = wordlift_client.ExpectationsApi(api_client)
    expectation_id = 'expectation_id_example' # str | 
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Detach Expectation Segment
        await api_instance.detach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_delete(expectation_id, segment_id, account_id)
    except Exception as e:
        print("Exception when calling ExpectationsApi->detach_expectation_segment_accounts_account_id_monitoring_expectations_expectation_id_segments_segment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expectation_id** | **str**|  | 
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

# **get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get**
> ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get(expectation_id, account_id)

Get Expectation

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.response_get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get import ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet
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
    api_instance = wordlift_client.ExpectationsApi(api_client)
    expectation_id = 'expectation_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Get Expectation
        api_response = await api_instance.get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get(expectation_id, account_id)
        print("The response of ExpectationsApi->get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpectationsApi->get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expectation_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet**](ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet.md)

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

# **list_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_get**
> ListSegmentSeverityResponse list_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_get(expectation_id, account_id, cursor=cursor, limit=limit)

List Expectation Segments

Return a page of segment ids attached to the rule, ordered by the segment's own ``(created_at, id)``, each carrying the severity of its attachment. Not hydrated — pair with the segment catalog you already have (segments are a small, bounded set) to resolve names/descriptions.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_segment_severity_response import ListSegmentSeverityResponse
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
    api_instance = wordlift_client.ExpectationsApi(api_client)
    expectation_id = 'expectation_id_example' # str | 
    account_id = 'account_id_example' # str | 
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 50 # int | Maximum number of segments to return. (optional) (default to 50)

    try:
        # List Expectation Segments
        api_response = await api_instance.list_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_get(expectation_id, account_id, cursor=cursor, limit=limit)
        print("The response of ExpectationsApi->list_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpectationsApi->list_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expectation_id** | **str**|  | 
 **account_id** | **str**|  | 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Maximum number of segments to return. | [optional] [default to 50]

### Return type

[**ListSegmentSeverityResponse**](ListSegmentSeverityResponse.md)

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

# **list_expectations_accounts_account_id_monitoring_expectations_get**
> ListExpectationsResponse list_expectations_accounts_account_id_monitoring_expectations_get(account_id, q=q, id=id, segment_id=segment_id, cursor=cursor, limit=limit)

List Expectations

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_expectations_response import ListExpectationsResponse
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
    api_instance = wordlift_client.ExpectationsApi(api_client)
    account_id = 'account_id_example' # str | 
    q = 'q_example' # str | Case-insensitive substring search across each expectation type's searchable config fields. (optional)
    id = ['id_example'] # List[str] | Return only expectations with one of the given ids (repeatable). (optional)
    segment_id = ['segment_id_example'] # List[str] | Return only expectations attached to at least one of the given segments (repeatable). (optional)
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 50 # int | Maximum number of expectations to return. (optional) (default to 50)

    try:
        # List Expectations
        api_response = await api_instance.list_expectations_accounts_account_id_monitoring_expectations_get(account_id, q=q, id=id, segment_id=segment_id, cursor=cursor, limit=limit)
        print("The response of ExpectationsApi->list_expectations_accounts_account_id_monitoring_expectations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpectationsApi->list_expectations_accounts_account_id_monitoring_expectations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **q** | **str**| Case-insensitive substring search across each expectation type&#39;s searchable config fields. | [optional] 
 **id** | [**List[str]**](str.md)| Return only expectations with one of the given ids (repeatable). | [optional] 
 **segment_id** | [**List[str]**](str.md)| Return only expectations attached to at least one of the given segments (repeatable). | [optional] 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Maximum number of expectations to return. | [optional] [default to 50]

### Return type

[**ListExpectationsResponse**](ListExpectationsResponse.md)

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

# **list_segment_expectations_accounts_account_id_monitoring_segments_segment_id_expectations_get**
> ListExpectationSeverityResponse list_segment_expectations_accounts_account_id_monitoring_segments_segment_id_expectations_get(segment_id, account_id, expectation_id=expectation_id, cursor=cursor, limit=limit)

List Segment Expectations

Return a page of expectation ids attached to the segment, ordered by the expectation's own ``(created_at, id)``, each carrying the severity of its attachment — the reverse of ``GET /expectations/{id}/segments``.  Pass ``expectation_id`` (repeatable) to batch a known, bounded set of severity lookups in one call instead of one request per expectation: since the junction key is ``(expectation_id, segment_id)``, a filtered page can never return more rows than ids supplied. Not hydrated — pair with the expectation catalog you already have (or fetch via ``GET /expectations?id=...``) to resolve type/config.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_expectation_severity_response import ListExpectationSeverityResponse
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
    api_instance = wordlift_client.ExpectationsApi(api_client)
    segment_id = 'segment_id_example' # str | 
    account_id = 'account_id_example' # str | 
    expectation_id = ['expectation_id_example'] # List[str] | Filter to these expectation ids (repeatable). Omitted returns every expectation attached to the segment. (optional)
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 50 # int | Maximum number of expectations to return. (optional) (default to 50)

    try:
        # List Segment Expectations
        api_response = await api_instance.list_segment_expectations_accounts_account_id_monitoring_segments_segment_id_expectations_get(segment_id, account_id, expectation_id=expectation_id, cursor=cursor, limit=limit)
        print("The response of ExpectationsApi->list_segment_expectations_accounts_account_id_monitoring_segments_segment_id_expectations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpectationsApi->list_segment_expectations_accounts_account_id_monitoring_segments_segment_id_expectations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**|  | 
 **account_id** | **str**|  | 
 **expectation_id** | [**List[str]**](str.md)| Filter to these expectation ids (repeatable). Omitted returns every expectation attached to the segment. | [optional] 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Maximum number of expectations to return. | [optional] [default to 50]

### Return type

[**ListExpectationSeverityResponse**](ListExpectationSeverityResponse.md)

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

# **replace_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_put**
> List[SegmentSeverityResponse] replace_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_put(expectation_id, account_id, replace_expectation_segments_request)

Replace Expectation Segments

Replace the rule's set of attached segments (and their severities) wholesale. Returns confirmation of the new attached set, not re-fetched segments — no endpoint on this resource hydrates the full segment.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.replace_expectation_segments_request import ReplaceExpectationSegmentsRequest
from wordlift_client.models.segment_severity_response import SegmentSeverityResponse
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
    api_instance = wordlift_client.ExpectationsApi(api_client)
    expectation_id = 'expectation_id_example' # str | 
    account_id = 'account_id_example' # str | 
    replace_expectation_segments_request = wordlift_client.ReplaceExpectationSegmentsRequest() # ReplaceExpectationSegmentsRequest | 

    try:
        # Replace Expectation Segments
        api_response = await api_instance.replace_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_put(expectation_id, account_id, replace_expectation_segments_request)
        print("The response of ExpectationsApi->replace_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpectationsApi->replace_expectation_segments_accounts_account_id_monitoring_expectations_expectation_id_segments_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expectation_id** | **str**|  | 
 **account_id** | **str**|  | 
 **replace_expectation_segments_request** | [**ReplaceExpectationSegmentsRequest**](ReplaceExpectationSegmentsRequest.md)|  | 

### Return type

[**List[SegmentSeverityResponse]**](SegmentSeverityResponse.md)

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

