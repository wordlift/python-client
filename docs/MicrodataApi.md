# wordlift_client.MicrodataApi

All URIs are relative to *https://api.wordlift.io/quality-rating*

Method | HTTP request | Description
------------- | ------------- | -------------
[**microdata_to_json_ld**](MicrodataApi.md#microdata_to_json_ld) | **GET** /microdata-to-jsonld | Microdata to JSON-LD


# **microdata_to_json_ld**
> Dict[str, object] microdata_to_json_ld(u)

Microdata to JSON-LD

Provided a URL, converts any microdata found on that URL to JSON-LD.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
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
    api_instance = wordlift_client.MicrodataApi(api_client)
    u = 'u_example' # str | The web page URL

    try:
        # Microdata to JSON-LD
        api_response = await api_instance.microdata_to_json_ld(u)
        print("The response of MicrodataApi->microdata_to_json_ld:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrodataApi->microdata_to_json_ld: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **u** | **str**| The web page URL | 

### Return type

**Dict[str, object]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

