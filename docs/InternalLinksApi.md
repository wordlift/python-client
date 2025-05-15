# wordlift_client.InternalLinksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_internal_link**](InternalLinksApi.md#create_internal_link) | **POST** /internal-links | Create
[**create_internal_link_suggestion**](InternalLinksApi.md#create_internal_link_suggestion) | **POST** /internal-links/suggestions | Suggest


# **create_internal_link**
> List[str] create_internal_link(internal_link_request)

Create

Create Internal Links.

### Example


```python
import wordlift_client
from wordlift_client.models.internal_link_request import InternalLinkRequest
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_internal_link_suggestion**
> List[InternalLink] create_internal_link_suggestion(internal_link_request)

Suggest

Create an Internal Links suggestion.

### Example


```python
import wordlift_client
from wordlift_client.models.internal_link import InternalLink
from wordlift_client.models.internal_link_request import InternalLinkRequest
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

