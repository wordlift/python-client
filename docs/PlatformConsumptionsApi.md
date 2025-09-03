# wordlift_client.PlatformConsumptionsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_my_platform_consumption**](PlatformConsumptionsApi.md#create_or_update_my_platform_consumption) | **PUT** /platform-limit/consumptions/me | Create or update the Platform Consumption
[**delete_platform_consumption**](PlatformConsumptionsApi.md#delete_platform_consumption) | **DELETE** /platform-limit/consumptions/{referenceType}/{referenceId}/{appliesTo} | Delete Platform Consumption
[**delete_platform_consumption_by_id**](PlatformConsumptionsApi.md#delete_platform_consumption_by_id) | **DELETE** /platform-limit/consumptions/{id} | Delete Platform Consumption by ID
[**get_my_platform_consumption**](PlatformConsumptionsApi.md#get_my_platform_consumption) | **GET** /platform-limit/consumptions/me | Get the Platform Consumption


# **create_or_update_my_platform_consumption**
> PageWithLimits create_or_update_my_platform_consumption(applies_to, consumption_to_add=consumption_to_add)

Create or update the Platform Consumption

Create or update the Platform Consumption for the authenticated user.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.page_with_limits import PageWithLimits
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.PlatformConsumptionsApi(api_client)
    applies_to = 'applies_to_example' # str | 
    consumption_to_add = 1 # int |  (optional) (default to 1)

    try:
        # Create or update the Platform Consumption
        api_response = await api_instance.create_or_update_my_platform_consumption(applies_to, consumption_to_add=consumption_to_add)
        print("The response of PlatformConsumptionsApi->create_or_update_my_platform_consumption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformConsumptionsApi->create_or_update_my_platform_consumption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applies_to** | **str**|  | 
 **consumption_to_add** | **int**|  | [optional] [default to 1]

### Return type

[**PageWithLimits**](PageWithLimits.md)

### Authorization

[OAuth2](../README.md#OAuth2), [ApiKey](../README.md#ApiKey)

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

# **delete_platform_consumption**
> delete_platform_consumption(reference_type, reference_id, applies_to)

Delete Platform Consumption

Allow admins to delete platform consumptions.

### Example

* OAuth Authentication (OAuth2):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.PlatformConsumptionsApi(api_client)
    reference_type = 'reference_type_example' # str | 
    reference_id = 56 # int | 
    applies_to = 'applies_to_example' # str | 

    try:
        # Delete Platform Consumption
        await api_instance.delete_platform_consumption(reference_type, reference_id, applies_to)
    except Exception as e:
        print("Exception when calling PlatformConsumptionsApi->delete_platform_consumption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_type** | **str**|  | 
 **reference_id** | **int**|  | 
 **applies_to** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Done |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_platform_consumption_by_id**
> delete_platform_consumption_by_id(id)

Delete Platform Consumption by ID

Allow admins to delete platform consumptions.

### Example

* OAuth Authentication (OAuth2):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.PlatformConsumptionsApi(api_client)
    id = 56 # int | 

    try:
        # Delete Platform Consumption by ID
        await api_instance.delete_platform_consumption_by_id(id)
    except Exception as e:
        print("Exception when calling PlatformConsumptionsApi->delete_platform_consumption_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Done |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_platform_consumption**
> PageWithLimits get_my_platform_consumption(applies_to, include_subscription=include_subscription, include_limit=include_limit)

Get the Platform Consumption

Get the Platform Consumption for the authenticated user.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.page_with_limits import PageWithLimits
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.PlatformConsumptionsApi(api_client)
    applies_to = 'applies_to_example' # str | 
    include_subscription = True # bool |  (optional)
    include_limit = True # bool |  (optional)

    try:
        # Get the Platform Consumption
        api_response = await api_instance.get_my_platform_consumption(applies_to, include_subscription=include_subscription, include_limit=include_limit)
        print("The response of PlatformConsumptionsApi->get_my_platform_consumption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformConsumptionsApi->get_my_platform_consumption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applies_to** | **str**|  | 
 **include_subscription** | **bool**|  | [optional] 
 **include_limit** | **bool**|  | [optional] 

### Return type

[**PageWithLimits**](PageWithLimits.md)

### Authorization

[OAuth2](../README.md#OAuth2), [ApiKey](../README.md#ApiKey)

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

