# wordlift_client.PlatformConsumptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_my_platform_consumption**](PlatformConsumptionsApi.md#create_or_update_my_platform_consumption) | **PUT** /platform-limit/consumptions/me | Create or update the Platform Consumption
[**get_my_platform_consumption**](PlatformConsumptionsApi.md#get_my_platform_consumption) | **GET** /platform-limit/consumptions/me | Get the Platform Consumption


# **create_or_update_my_platform_consumption**
> PageWithLimits create_or_update_my_platform_consumption(applies_to, consumption_to_add=consumption_to_add)

Create or update the Platform Consumption

Create or update the Platform Consumption for the authenticated user.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.page_with_limits import PageWithLimits
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

[ApiKey](../README.md#ApiKey)

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

# **get_my_platform_consumption**
> PageWithLimits get_my_platform_consumption(applies_to, include_subscription=include_subscription, include_limit=include_limit)

Get the Platform Consumption

Get the Platform Consumption for the authenticated user.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.page_with_limits import PageWithLimits
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

[ApiKey](../README.md#ApiKey)

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

