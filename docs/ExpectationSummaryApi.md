# wordlift_client.ExpectationSummaryApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_expectation_summary_by_expectation_accounts_account_id_monitoring_expectations_summary_by_expectation_get**](ExpectationSummaryApi.md#list_expectation_summary_by_expectation_accounts_account_id_monitoring_expectations_summary_by_expectation_get) | **GET** /accounts/{account_id}/monitoring/expectations/summary/by-expectation | List Expectation Summary By Expectation
[**list_expectation_summary_by_type_accounts_account_id_monitoring_expectations_summary_by_type_get**](ExpectationSummaryApi.md#list_expectation_summary_by_type_accounts_account_id_monitoring_expectations_summary_by_type_get) | **GET** /accounts/{account_id}/monitoring/expectations/summary/by-type | List Expectation Summary By Type


# **list_expectation_summary_by_expectation_accounts_account_id_monitoring_expectations_summary_by_expectation_get**
> ListExpectationSummaryByExpectationResponse list_expectation_summary_by_expectation_accounts_account_id_monitoring_expectations_summary_by_expectation_get(account_id, segment_id=segment_id, cursor=cursor, limit=limit)

List Expectation Summary By Expectation

Account-wide expectation rollup grouped by (segment, expectation), broken down by outcome only — severity and expectation type are derivable from the expectation itself. Omitted or empty `segment_id` returns the account-wide aggregate (`segment_id: null`).

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_expectation_summary_by_expectation_response import ListExpectationSummaryByExpectationResponse
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
    api_instance = wordlift_client.ExpectationSummaryApi(api_client)
    account_id = 'account_id_example' # str | 
    segment_id = 'segment_id_example' # str | Scope to this segment. Omitted or empty returns the account-wide aggregate (`segment_id: null`). (optional)
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 50 # int | Maximum number of items to return. (optional) (default to 50)

    try:
        # List Expectation Summary By Expectation
        api_response = await api_instance.list_expectation_summary_by_expectation_accounts_account_id_monitoring_expectations_summary_by_expectation_get(account_id, segment_id=segment_id, cursor=cursor, limit=limit)
        print("The response of ExpectationSummaryApi->list_expectation_summary_by_expectation_accounts_account_id_monitoring_expectations_summary_by_expectation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpectationSummaryApi->list_expectation_summary_by_expectation_accounts_account_id_monitoring_expectations_summary_by_expectation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **segment_id** | **str**| Scope to this segment. Omitted or empty returns the account-wide aggregate (&#x60;segment_id: null&#x60;). | [optional] 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Maximum number of items to return. | [optional] [default to 50]

### Return type

[**ListExpectationSummaryByExpectationResponse**](ListExpectationSummaryByExpectationResponse.md)

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

# **list_expectation_summary_by_type_accounts_account_id_monitoring_expectations_summary_by_type_get**
> ListExpectationSummaryByTypeResponse list_expectation_summary_by_type_accounts_account_id_monitoring_expectations_summary_by_type_get(account_id, expectation_type=expectation_type, segment_id=segment_id, cursor=cursor, limit=limit)

List Expectation Summary By Type

Account-wide expectation rollup grouped by (segment, expectation type), broken down by (severity, outcome). Omitting both filters returns every segment together with the account-wide aggregate (`segment_id: null`); passing the reserved `segment_id=overall` isolates just that aggregate instead of requiring a full scan to find it.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.expectation_type import ExpectationType
from wordlift_client.models.list_expectation_summary_by_type_response import ListExpectationSummaryByTypeResponse
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
    api_instance = wordlift_client.ExpectationSummaryApi(api_client)
    account_id = 'account_id_example' # str | 
    expectation_type = [wordlift_client.ExpectationType()] # List[ExpectationType] | Filter by expectation type (repeatable). Omitted returns every type. (optional)
    segment_id = ['segment_id_example'] # List[str] | Filter by segment id (repeatable), or the reserved value `overall` to match only the account-wide aggregate row. Omitted returns every segment together with that aggregate. (optional)
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 50 # int | Maximum number of items to return. (optional) (default to 50)

    try:
        # List Expectation Summary By Type
        api_response = await api_instance.list_expectation_summary_by_type_accounts_account_id_monitoring_expectations_summary_by_type_get(account_id, expectation_type=expectation_type, segment_id=segment_id, cursor=cursor, limit=limit)
        print("The response of ExpectationSummaryApi->list_expectation_summary_by_type_accounts_account_id_monitoring_expectations_summary_by_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpectationSummaryApi->list_expectation_summary_by_type_accounts_account_id_monitoring_expectations_summary_by_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **expectation_type** | [**List[ExpectationType]**](ExpectationType.md)| Filter by expectation type (repeatable). Omitted returns every type. | [optional] 
 **segment_id** | [**List[str]**](str.md)| Filter by segment id (repeatable), or the reserved value &#x60;overall&#x60; to match only the account-wide aggregate row. Omitted returns every segment together with that aggregate. | [optional] 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Maximum number of items to return. | [optional] [default to 50]

### Return type

[**ListExpectationSummaryByTypeResponse**](ListExpectationSummaryByTypeResponse.md)

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

