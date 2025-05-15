# wordlift_client.PlatformLimitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_platform_limit**](PlatformLimitsApi.md#create_platform_limit) | **POST** /platform-limit/limits | Create Platform Limit
[**delete_platform_limit**](PlatformLimitsApi.md#delete_platform_limit) | **DELETE** /platform-limit/limits/{id} | Delete Platform Limit
[**get_platform_limit**](PlatformLimitsApi.md#get_platform_limit) | **GET** /platform-limit/limits/{id} | Get Platform Limit
[**list_platform_limits**](PlatformLimitsApi.md#list_platform_limits) | **GET** /platform-limit/limits | List Platform Limits
[**update_platform_limit**](PlatformLimitsApi.md#update_platform_limit) | **PUT** /platform-limit/limits/{id} | Update Platform Limit


# **create_platform_limit**
> PlatformLimit create_platform_limit(platform_limit_request)

Create Platform Limit

Create a platform limit.

### Example


```python
import wordlift_client
from wordlift_client.models.platform_limit import PlatformLimit
from wordlift_client.models.platform_limit_request import PlatformLimitRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.PlatformLimitsApi(api_client)
    platform_limit_request = wordlift_client.PlatformLimitRequest() # PlatformLimitRequest | 

    try:
        # Create Platform Limit
        api_response = await api_instance.create_platform_limit(platform_limit_request)
        print("The response of PlatformLimitsApi->create_platform_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformLimitsApi->create_platform_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_limit_request** | [**PlatformLimitRequest**](PlatformLimitRequest.md)|  | 

### Return type

[**PlatformLimit**](PlatformLimit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_platform_limit**
> delete_platform_limit(id)

Delete Platform Limit

Delete a platform limit.

### Example


```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.PlatformLimitsApi(api_client)
    id = 56 # int | Platform Limit id

    try:
        # Delete Platform Limit
        await api_instance.delete_platform_limit(id)
    except Exception as e:
        print("Exception when calling PlatformLimitsApi->delete_platform_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Platform Limit id | 

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
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platform_limit**
> PlatformLimit get_platform_limit(id)

Get Platform Limit

Get a platform limit.

### Example


```python
import wordlift_client
from wordlift_client.models.platform_limit import PlatformLimit
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.PlatformLimitsApi(api_client)
    id = 56 # int | Platform Limit id

    try:
        # Get Platform Limit
        api_response = await api_instance.get_platform_limit(id)
        print("The response of PlatformLimitsApi->get_platform_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformLimitsApi->get_platform_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Platform Limit id | 

### Return type

[**PlatformLimit**](PlatformLimit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_platform_limits**
> PagePlatformLimit list_platform_limits(based_on_in=based_on_in, based_on_value_in=based_on_value_in, applies_to_in=applies_to_in, scope_in=scope_in)

List Platform Limits

List the platform limits.

### Example


```python
import wordlift_client
from wordlift_client.models.page_platform_limit import PagePlatformLimit
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.PlatformLimitsApi(api_client)
    based_on_in = ['based_on_in_example'] # List[str] | The type of based on, e.g. `sku`. (optional)
    based_on_value_in = ['based_on_value_in_example'] # List[str] | The based on values. (optional)
    applies_to_in = ['applies_to_in_example'] # List[str] | The applies to (e.g. API name). (optional)
    scope_in = ['scope_in_example'] # List[str] | The scope. (optional)

    try:
        # List Platform Limits
        api_response = await api_instance.list_platform_limits(based_on_in=based_on_in, based_on_value_in=based_on_value_in, applies_to_in=applies_to_in, scope_in=scope_in)
        print("The response of PlatformLimitsApi->list_platform_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformLimitsApi->list_platform_limits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **based_on_in** | [**List[str]**](str.md)| The type of based on, e.g. &#x60;sku&#x60;. | [optional] 
 **based_on_value_in** | [**List[str]**](str.md)| The based on values. | [optional] 
 **applies_to_in** | [**List[str]**](str.md)| The applies to (e.g. API name). | [optional] 
 **scope_in** | [**List[str]**](str.md)| The scope. | [optional] 

### Return type

[**PagePlatformLimit**](PagePlatformLimit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_platform_limit**
> PlatformLimit update_platform_limit(id, platform_limit_request)

Update Platform Limit

Update a platform limit.

### Example


```python
import wordlift_client
from wordlift_client.models.platform_limit import PlatformLimit
from wordlift_client.models.platform_limit_request import PlatformLimitRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.PlatformLimitsApi(api_client)
    id = 56 # int | Platform Limit id
    platform_limit_request = wordlift_client.PlatformLimitRequest() # PlatformLimitRequest | 

    try:
        # Update Platform Limit
        api_response = await api_instance.update_platform_limit(id, platform_limit_request)
        print("The response of PlatformLimitsApi->update_platform_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformLimitsApi->update_platform_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Platform Limit id | 
 **platform_limit_request** | [**PlatformLimitRequest**](PlatformLimitRequest.md)|  | 

### Return type

[**PlatformLimit**](PlatformLimit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

