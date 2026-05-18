# wordlift_client.InspectorApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get4**](InspectorApi.md#get4) | **GET** /inspect | Inspect


# **get4**
> InspectResponse get4(u, f, classes=classes)

Inspect

Inspect a URL to perform a variety of tasks defined by the list of applied filters.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.inspect_response import InspectResponse
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
    api_instance = wordlift_client.InspectorApi(api_client)
    u = 'https://wordlift.io' # str | The URL to inspect
    f = 'validator,content-analysis' # str | Filters to be applied on the result, if you want to apply multiple filters they should be separated by comma
    classes = ['classes_example'] # List[str] | A list of categories to be provided for classify filter. (optional)

    try:
        # Inspect
        api_response = await api_instance.get4(u, f, classes=classes)
        print("The response of InspectorApi->get4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InspectorApi->get4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **u** | **str**| The URL to inspect | 
 **f** | **str**| Filters to be applied on the result, if you want to apply multiple filters they should be separated by comma | 
 **classes** | [**List[str]**](str.md)| A list of categories to be provided for classify filter. | [optional] 

### Return type

[**InspectResponse**](InspectResponse.md)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

