# Wordlift_client.ContentExpansionsApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_content_expansion**](ContentExpansionsApi.md#create_content_expansion) | **POST** /content-expansions | Create


# **create_content_expansion**
> ContentExpansionResponse create_content_expansion(content_expansion_request)

Create

Create a Content Expansion

### Example

* Api Key Authentication (ApiKey):

```python
import Wordlift_client
from Wordlift_client.models.content_expansion_request import ContentExpansionRequest
from Wordlift_client.models.content_expansion_response import ContentExpansionResponse
from Wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = Wordlift_client.Configuration(
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
async with Wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Wordlift_client.ContentExpansionsApi(api_client)
    content_expansion_request = Wordlift_client.ContentExpansionRequest() # ContentExpansionRequest | 

    try:
        # Create
        api_response = await api_instance.create_content_expansion(content_expansion_request)
        print("The response of ContentExpansionsApi->create_content_expansion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentExpansionsApi->create_content_expansion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_expansion_request** | [**ContentExpansionRequest**](ContentExpansionRequest.md)|  | 

### Return type

[**ContentExpansionResponse**](ContentExpansionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**500** | Uh oh, something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

