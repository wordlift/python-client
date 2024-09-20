# wordlift_client.InternalLinksApi

All URIs are relative to *https://api.wordlift.io/quality-rating*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_internal_link**](InternalLinksApi.md#create_internal_link) | **POST** /internal-links | Create
[**create_internal_link_suggestion**](InternalLinksApi.md#create_internal_link_suggestion) | **POST** /internal-links/suggestions | Suggest


# **create_internal_link**
> List[str] create_internal_link(internal_link_request)

Create

Create Internal Links.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.internal_link_request import InternalLinkRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/quality-rating
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/quality-rating"
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
    api_instance = wordlift_client.InternalLinksApi(api_client)
    internal_link_request = wordlift_client.InternalLinkRequest() # InternalLinkRequest | 

    try:
        # Create
        api_response = await api_instance.create_internal_link(internal_link_request)
        print("The response of InternalLinksApi->create_internal_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalLinksApi->create_internal_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_link_request** | [**InternalLinkRequest**](InternalLinkRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_internal_link_suggestion**
> List[InternalLink] create_internal_link_suggestion(internal_link_request)

Suggest

Create an Internal Links suggestion.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.internal_link import InternalLink
from wordlift_client.models.internal_link_request import InternalLinkRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/quality-rating
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/quality-rating"
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
    api_instance = wordlift_client.InternalLinksApi(api_client)
    internal_link_request = wordlift_client.InternalLinkRequest() # InternalLinkRequest | 

    try:
        # Suggest
        api_response = await api_instance.create_internal_link_suggestion(internal_link_request)
        print("The response of InternalLinksApi->create_internal_link_suggestion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalLinksApi->create_internal_link_suggestion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_link_request** | [**InternalLinkRequest**](InternalLinkRequest.md)|  | 

### Return type

[**List[InternalLink]**](InternalLink.md)

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

