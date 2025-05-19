# wordlift_client.ContentGenerationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_content_generation**](ContentGenerationsApi.md#create_content_generation) | **POST** /content-generations | Create
[**delete_content_generation**](ContentGenerationsApi.md#delete_content_generation) | **DELETE** /content-generations/{id} | Delete
[**duplicate_content_generation**](ContentGenerationsApi.md#duplicate_content_generation) | **POST** /content-generations/{from_content_generation_id}/duplicates | Duplicate
[**get_content_generation**](ContentGenerationsApi.md#get_content_generation) | **GET** /content-generations/{id} | Get
[**list_content_generations**](ContentGenerationsApi.md#list_content_generations) | **GET** /content-generations | List
[**update_content_generation**](ContentGenerationsApi.md#update_content_generation) | **PUT** /content-generations/{id} | Update


# **create_content_generation**
> ContentGeneration create_content_generation(content_generation_request)

Create

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.content_generation import ContentGeneration
from wordlift_client.models.content_generation_request import ContentGenerationRequest
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
    api_instance = wordlift_client.ContentGenerationsApi(api_client)
    content_generation_request = wordlift_client.ContentGenerationRequest() # ContentGenerationRequest | 

    try:
        # Create
        api_response = await api_instance.create_content_generation(content_generation_request)
        print("The response of ContentGenerationsApi->create_content_generation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationsApi->create_content_generation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_request** | [**ContentGenerationRequest**](ContentGenerationRequest.md)|  | 

### Return type

[**ContentGeneration**](ContentGeneration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_generation**
> delete_content_generation(id)

Delete

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
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
    api_instance = wordlift_client.ContentGenerationsApi(api_client)
    id = 56 # int | The Content Generation id.

    try:
        # Delete
        await api_instance.delete_content_generation(id)
    except Exception as e:
        print("Exception when calling ContentGenerationsApi->delete_content_generation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Content Generation id. | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_content_generation**
> ContentGeneration duplicate_content_generation(from_content_generation_id)

Duplicate

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.content_generation import ContentGeneration
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
    api_instance = wordlift_client.ContentGenerationsApi(api_client)
    from_content_generation_id = 56 # int | The Content Generation id to duplicate from.

    try:
        # Duplicate
        api_response = await api_instance.duplicate_content_generation(from_content_generation_id)
        print("The response of ContentGenerationsApi->duplicate_content_generation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationsApi->duplicate_content_generation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_content_generation_id** | **int**| The Content Generation id to duplicate from. | 

### Return type

[**ContentGeneration**](ContentGeneration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_generation**
> ContentGeneration get_content_generation(id)

Get

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.content_generation import ContentGeneration
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
    api_instance = wordlift_client.ContentGenerationsApi(api_client)
    id = 56 # int | The Content Generation id.

    try:
        # Get
        api_response = await api_instance.get_content_generation(id)
        print("The response of ContentGenerationsApi->get_content_generation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationsApi->get_content_generation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Content Generation id. | 

### Return type

[**ContentGeneration**](ContentGeneration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_content_generations**
> PageContentGeneration list_content_generations(cursor=cursor, limit=limit, deleted=deleted)

List

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.page_content_generation import PageContentGeneration
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
    api_instance = wordlift_client.ContentGenerationsApi(api_client)
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)
    deleted = True # bool | Filter for the deleted flag (optional)

    try:
        # List
        api_response = await api_instance.list_content_generations(cursor=cursor, limit=limit, deleted=deleted)
        print("The response of ContentGenerationsApi->list_content_generations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationsApi->list_content_generations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]
 **deleted** | **bool**| Filter for the deleted flag | [optional] 

### Return type

[**PageContentGeneration**](PageContentGeneration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_content_generation**
> ContentGeneration update_content_generation(id, content_generation_request)

Update

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.content_generation import ContentGeneration
from wordlift_client.models.content_generation_request import ContentGenerationRequest
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
    api_instance = wordlift_client.ContentGenerationsApi(api_client)
    id = 56 # int | The Content Generation id.
    content_generation_request = wordlift_client.ContentGenerationRequest() # ContentGenerationRequest | 

    try:
        # Update
        api_response = await api_instance.update_content_generation(id, content_generation_request)
        print("The response of ContentGenerationsApi->update_content_generation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationsApi->update_content_generation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Content Generation id. | 
 **content_generation_request** | [**ContentGenerationRequest**](ContentGenerationRequest.md)|  | 

### Return type

[**ContentGeneration**](ContentGeneration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

