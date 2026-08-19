# wordlift_client.MonitorCheckSummaryApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_check_summary_by_check_accounts_account_id_monitoring_checks_summary_by_check_get**](MonitorCheckSummaryApi.md#list_check_summary_by_check_accounts_account_id_monitoring_checks_summary_by_check_get) | **GET** /accounts/{account_id}/monitoring/checks/summary/by-check | List Check Summary By Check


# **list_check_summary_by_check_accounts_account_id_monitoring_checks_summary_by_check_get**
> ListCheckSummaryByCheckResponse list_check_summary_by_check_accounts_account_id_monitoring_checks_summary_by_check_get(account_id, check_name=check_name, segment_id=segment_id, cursor=cursor, limit=limit)

List Check Summary By Check

Account-wide check rollup grouped by (segment, check name), broken down by state (``CheckSummaryState`` — OK/WARN/FAIL/PENDING). Omitting both filters returns every segment and check together with the account-wide, all-checks-combined aggregate (`segment_id: null`, `check_name: null`); passing the reserved `overall` value isolates just that aggregate on either dimension instead of requiring a full scan to find it.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.check_name_filter_value import CheckNameFilterValue
from wordlift_client.models.list_check_summary_by_check_response import ListCheckSummaryByCheckResponse
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
    api_instance = wordlift_client.MonitorCheckSummaryApi(api_client)
    account_id = 'account_id_example' # str | 
    check_name = [wordlift_client.CheckNameFilterValue()] # List[CheckNameFilterValue] | Filter by check name (repeatable), or the reserved value `overall` to match only the all-checks-combined aggregate row. Omitted returns every check together with that aggregate. (optional)
    segment_id = ['segment_id_example'] # List[str] | Filter by segment id (repeatable), or the reserved value `overall` to match only the account-wide aggregate row. Omitted returns every segment together with that aggregate. (optional)
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    limit = 50 # int | Maximum number of items to return. (optional) (default to 50)

    try:
        # List Check Summary By Check
        api_response = await api_instance.list_check_summary_by_check_accounts_account_id_monitoring_checks_summary_by_check_get(account_id, check_name=check_name, segment_id=segment_id, cursor=cursor, limit=limit)
        print("The response of MonitorCheckSummaryApi->list_check_summary_by_check_accounts_account_id_monitoring_checks_summary_by_check_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorCheckSummaryApi->list_check_summary_by_check_accounts_account_id_monitoring_checks_summary_by_check_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **check_name** | [**List[CheckNameFilterValue]**](CheckNameFilterValue.md)| Filter by check name (repeatable), or the reserved value &#x60;overall&#x60; to match only the all-checks-combined aggregate row. Omitted returns every check together with that aggregate. | [optional] 
 **segment_id** | [**List[str]**](str.md)| Filter by segment id (repeatable), or the reserved value &#x60;overall&#x60; to match only the account-wide aggregate row. Omitted returns every segment together with that aggregate. | [optional] 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **limit** | **int**| Maximum number of items to return. | [optional] [default to 50]

### Return type

[**ListCheckSummaryByCheckResponse**](ListCheckSummaryByCheckResponse.md)

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

