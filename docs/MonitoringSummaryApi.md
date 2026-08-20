# wordlift_client.MonitoringSummaryApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_segment_summary_accounts_account_id_monitoring_summary_by_segment_get**](MonitoringSummaryApi.md#list_segment_summary_accounts_account_id_monitoring_summary_by_segment_get) | **GET** /accounts/{account_id}/monitoring/summary/by-segment | List Segment Summary


# **list_segment_summary_accounts_account_id_monitoring_summary_by_segment_get**
> ListSegmentSummaryResponse list_segment_summary_accounts_account_id_monitoring_summary_by_segment_get(account_id, segment_id=segment_id, cursor=cursor, limit=limit)

List Segment Summary

Account-wide monitor/expectation counters grouped by segment — replaces the N+1 pattern of paginated `monitors`/`expectations` list calls with `segment_id` + `limit=1` just to read their totals. One request returns every segment's counters regardless of how many segments the account has.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.list_segment_summary_response import ListSegmentSummaryResponse
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
    api_instance = wordlift_client.MonitoringSummaryApi(api_client)
    account_id = 'account_id_example' # str | 
    segment_id = ['segment_id_example'] # List[str] | Filter by segment id (repeatable). Omitted returns every segment for the account. (optional)
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 100 # int | Maximum number of segments to return. (optional) (default to 100)

    try:
        # List Segment Summary
        api_response = await api_instance.list_segment_summary_accounts_account_id_monitoring_summary_by_segment_get(account_id, segment_id=segment_id, cursor=cursor, limit=limit)
        print("The response of MonitoringSummaryApi->list_segment_summary_accounts_account_id_monitoring_summary_by_segment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringSummaryApi->list_segment_summary_accounts_account_id_monitoring_summary_by_segment_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **segment_id** | [**List[str]**](str.md)| Filter by segment id (repeatable). Omitted returns every segment for the account. | [optional] 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Maximum number of segments to return. | [optional] [default to 100]

### Return type

[**ListSegmentSummaryResponse**](ListSegmentSummaryResponse.md)

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

