# Wordlift_client.ContentGenerationRendersApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**render_template**](ContentGenerationRendersApi.md#render_template) | **POST** /content-generations/renders | Render
[**render_template_collection**](ContentGenerationRendersApi.md#render_template_collection) | **POST** /content-generations/renders-collection | Render


# **render_template**
> str render_template(render_request)

Render

[GET with body payload](https://opensource.zalando.com/restful-api-guidelines/#get-with-body) - no resources created

### Example


```python
import Wordlift_client
from Wordlift_client.models.render_request import RenderRequest
from Wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = Wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with Wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Wordlift_client.ContentGenerationRendersApi(api_client)
    render_request = Wordlift_client.RenderRequest() # RenderRequest | 

    try:
        # Render
        api_response = await api_instance.render_template(render_request)
        print("The response of ContentGenerationRendersApi->render_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationRendersApi->render_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **render_request** | [**RenderRequest**](RenderRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_template_collection**
> List[str] render_template_collection(render_request)

Render

[GET with body payload](https://opensource.zalando.com/restful-api-guidelines/#get-with-body) - no resources created

### Example


```python
import Wordlift_client
from Wordlift_client.models.render_request import RenderRequest
from Wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = Wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with Wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Wordlift_client.ContentGenerationRendersApi(api_client)
    render_request = [Wordlift_client.RenderRequest()] # List[RenderRequest] | 

    try:
        # Render
        api_response = await api_instance.render_template_collection(render_request)
        print("The response of ContentGenerationRendersApi->render_template_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationRendersApi->render_template_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **render_request** | [**List[RenderRequest]**](RenderRequest.md)|  | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

