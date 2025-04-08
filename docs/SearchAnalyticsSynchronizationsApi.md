# wordlift_client.SearchAnalyticsSynchronizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sync1**](SearchAnalyticsSynchronizationsApi.md#create_sync1) | **POST** /analytics-syncs | Create analytics sync
[**list_analytics_syncs**](SearchAnalyticsSynchronizationsApi.md#list_analytics_syncs) | **GET** /analytics-syncs | Get the latest syncs


# **create_sync1**
> AnalyticsSync create_sync1(analytics_sync_request)

Create analytics sync

Create and run analytics sync

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.analytics_sync import AnalyticsSync
from wordlift_client.models.analytics_sync_request import AnalyticsSyncRequest
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
    api_instance = wordlift_client.SearchAnalyticsSynchronizationsApi(api_client)
    analytics_sync_request = wordlift_client.AnalyticsSyncRequest() # AnalyticsSyncRequest | 

    try:
        # Create analytics sync
        api_response = await api_instance.create_sync1(analytics_sync_request)
        print("The response of SearchAnalyticsSynchronizationsApi->create_sync1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAnalyticsSynchronizationsApi->create_sync1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analytics_sync_request** | [**AnalyticsSyncRequest**](AnalyticsSyncRequest.md)|  | 

### Return type

[**AnalyticsSync**](AnalyticsSync.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_analytics_syncs**
> List[AnalyticsSync] list_analytics_syncs(account_ids, sort=sort, group_by=group_by)

Get the latest syncs

Retrieve the latest executed syncs

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.analytics_sync import AnalyticsSync
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
    api_instance = wordlift_client.SearchAnalyticsSynchronizationsApi(api_client)
    account_ids = [56] # List[int] | 
    sort = 'sort_example' # str |  (optional)
    group_by = 'group_by_example' # str |  (optional)

    try:
        # Get the latest syncs
        api_response = await api_instance.list_analytics_syncs(account_ids, sort=sort, group_by=group_by)
        print("The response of SearchAnalyticsSynchronizationsApi->list_analytics_syncs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAnalyticsSynchronizationsApi->list_analytics_syncs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**List[int]**](int.md)|  | 
 **sort** | **str**|  | [optional] 
 **group_by** | **str**|  | [optional] 

### Return type

[**List[AnalyticsSync]**](AnalyticsSync.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

