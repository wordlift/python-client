# wordlift_client.QueryFanOutApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ai_visibility_audit**](QueryFanOutApi.md#create_ai_visibility_audit) | **POST** /ai-visibility-audits | Create AI visibility audits for Query Fan-Out


# **create_ai_visibility_audit**
> AIVisibilityAnalysisResult create_ai_visibility_audit(analyze_content_request, authorization=authorization)

Create AI visibility audits for Query Fan-Out

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.ai_visibility_analysis_result import AIVisibilityAnalysisResult
from wordlift_client.models.analyze_content_request import AnalyzeContentRequest
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
    api_instance = wordlift_client.QueryFanOutApi(api_client)
    analyze_content_request = wordlift_client.AnalyzeContentRequest() # AnalyzeContentRequest | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Create AI visibility audits for Query Fan-Out
        api_response = await api_instance.create_ai_visibility_audit(analyze_content_request, authorization=authorization)
        print("The response of QueryFanOutApi->create_ai_visibility_audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryFanOutApi->create_ai_visibility_audit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyze_content_request** | [**AnalyzeContentRequest**](AnalyzeContentRequest.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**AIVisibilityAnalysisResult**](AIVisibilityAnalysisResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

