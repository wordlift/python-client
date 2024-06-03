# wordlift_client.EntitiesApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entities**](EntitiesApi.md#create_entities) | **POST** /entities | Create
[**create_or_update_entities**](EntitiesApi.md#create_or_update_entities) | **PUT** /entities | Update (or create)
[**delete_entities**](EntitiesApi.md#delete_entities) | **DELETE** /entities | Delete
[**get_entities**](EntitiesApi.md#get_entities) | **GET** /entities | Get


# **create_entities**
> List[object] create_entities(body)

Create

Create new entities by automatically generating their id.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
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
    api_instance = wordlift_client.EntitiesApi(api_client)
    body = 'body_example' # str | 

    try:
        # Create
        api_response = await api_instance.create_entities(body)
        print("The response of EntitiesApi->create_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->create_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**List[object]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/rdf+xml, text/turtle
 - **Accept**: application/ld+json, application/rdf+xml, text/turtle

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**412** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_entities**
> create_or_update_entities(request_body)

Update (or create)

Create or update entities by using the provided ids.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
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
    api_instance = wordlift_client.EntitiesApi(api_client)
    request_body = None # List[object] | 

    try:
        # Update (or create)
        await api_instance.create_or_update_entities(request_body)
    except Exception as e:
        print("Exception when calling EntitiesApi->create_or_update_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[object]**](object.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/rdf+xml, text/turtle
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**412** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entities**
> delete_entities(id, include_children=include_children, include_referenced=include_referenced)

Delete

Delete entities with the provided ids.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
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
    api_instance = wordlift_client.EntitiesApi(api_client)
    id = ['id_example'] # List[str] | One or more ids, in the form of URLs.
    include_children = 'false' # str | Whether to delete all the entities whose ids start with the provided ids, by default false. (optional) (default to 'false')
    include_referenced = 'false' # str | Whether to delete all the referenced entities (e.g. in `schema:mentions`), by default false. (optional) (default to 'false')

    try:
        # Delete
        await api_instance.delete_entities(id, include_children=include_children, include_referenced=include_referenced)
    except Exception as e:
        print("Exception when calling EntitiesApi->delete_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| One or more ids, in the form of URLs. | 
 **include_children** | **str**| Whether to delete all the entities whose ids start with the provided ids, by default false. | [optional] [default to &#39;false&#39;]
 **include_referenced** | **str**| Whether to delete all the referenced entities (e.g. in &#x60;schema:mentions&#x60;), by default false. | [optional] [default to &#39;false&#39;]

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
**200** | Success |  -  |
**412** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entities**
> List[object] get_entities(id, include_children=include_children, include_referenced=include_referenced, include_private=include_private)

Get

Get entities with the provided ids.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
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
    api_instance = wordlift_client.EntitiesApi(api_client)
    id = ['id_example'] # List[str] | One or more ids, in the form of URLs.
    include_children = 'false' # str | Whether to return all the entities whose ids start with the provided ids, by default false. (optional) (default to 'false')
    include_referenced = 'false' # str | Whether to return all the referenced entities (e.g. in `schema:mentions`), by default false. (optional) (default to 'false')
    include_private = 'false' # str | Whether to return private properties, requires an authenticated request, by default false. (optional) (default to 'false')

    try:
        # Get
        api_response = await api_instance.get_entities(id, include_children=include_children, include_referenced=include_referenced, include_private=include_private)
        print("The response of EntitiesApi->get_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| One or more ids, in the form of URLs. | 
 **include_children** | **str**| Whether to return all the entities whose ids start with the provided ids, by default false. | [optional] [default to &#39;false&#39;]
 **include_referenced** | **str**| Whether to return all the referenced entities (e.g. in &#x60;schema:mentions&#x60;), by default false. | [optional] [default to &#39;false&#39;]
 **include_private** | **str**| Whether to return private properties, requires an authenticated request, by default false. | [optional] [default to &#39;false&#39;]

### Return type

**List[object]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/rdf+xml, text/turtle

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**412** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

