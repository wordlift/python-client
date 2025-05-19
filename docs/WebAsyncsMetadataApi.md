# wordlift_client.WebAsyncsMetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get2**](WebAsyncsMetadataApi.md#get2) | **GET** /webasyncs/{id} | Get by id
[**list**](WebAsyncsMetadataApi.md#list) | **GET** /webasyncs | List


# **get2**
> WebAsync get2(id)

Get by id

Get a Web Async operation by its id.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.web_async import WebAsync
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
    api_instance = wordlift_client.WebAsyncsMetadataApi(api_client)
    id = 'id_example' # str | The Web Async id

    try:
        # Get by id
        api_response = await api_instance.get2(id)
        print("The response of WebAsyncsMetadataApi->get2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAsyncsMetadataApi->get2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Web Async id | 

### Return type

[**WebAsync**](WebAsync.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> List[WebAsync] list()

List

List all Web Async operations.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.web_async import WebAsync
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
    api_instance = wordlift_client.WebAsyncsMetadataApi(api_client)

    try:
        # List
        api_response = await api_instance.list()
        print("The response of WebAsyncsMetadataApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebAsyncsMetadataApi->list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WebAsync]**](WebAsync.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

