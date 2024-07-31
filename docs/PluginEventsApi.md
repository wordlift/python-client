# wordlift_client.PluginEventsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event**](PluginEventsApi.md#create_event) | **POST** /plugin/events | Create
[**list_events**](PluginEventsApi.md#list_events) | **GET** /plugin/events | List


# **create_event**
> Event create_event(request2)

Create

Create an event

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.event import Event
from wordlift_client.models.request2 import Request2
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
    api_instance = wordlift_client.PluginEventsApi(api_client)
    request2 = wordlift_client.Request2() # Request2 | 

    try:
        # Create
        api_response = await api_instance.create_event(request2)
        print("The response of PluginEventsApi->create_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginEventsApi->create_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request2** | [**Request2**](Request2.md)|  | 

### Return type

[**Event**](Event.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** | Authentication failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events**
> Response2 list_events(url=url, date_greater_than=date_greater_than, date_less_than=date_less_than, cursor=cursor, limit=limit)

List

List the events bound to the authenticated account.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.response2 import Response2
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
    api_instance = wordlift_client.PluginEventsApi(api_client)
    url = ['url_example'] # List[str] | URLs to return (optional)
    date_greater_than = '2013-10-20T19:20:30+01:00' # datetime | Event datetime filter to return events with date greater than the parameter (optional)
    date_less_than = '2013-10-20T19:20:30+01:00' # datetime | Event datetime filter to return events with date less than the parameter (optional)
    cursor = 'cursor_example' # str | The pagination cursor (optional)
    limit = 56 # int | The maximum number of results (optional)

    try:
        # List
        api_response = await api_instance.list_events(url=url, date_greater_than=date_greater_than, date_less_than=date_less_than, cursor=cursor, limit=limit)
        print("The response of PluginEventsApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginEventsApi->list_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | [**List[str]**](str.md)| URLs to return | [optional] 
 **date_greater_than** | **datetime**| Event datetime filter to return events with date greater than the parameter | [optional] 
 **date_less_than** | **datetime**| Event datetime filter to return events with date less than the parameter | [optional] 
 **cursor** | **str**| The pagination cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] 

### Return type

[**Response2**](Response2.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

