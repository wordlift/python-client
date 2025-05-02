# wordlift_client.ContentEvaluationsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate_content_api_content_evaluations_post**](ContentEvaluationsApi.md#evaluate_content_api_content_evaluations_post) | **POST** /content-evaluations | Evaluate Content


# **evaluate_content_api_content_evaluations_post**
> ContentEvaluationResponse evaluate_content_api_content_evaluations_post(content_evaluation_request)

Evaluate Content

Submit text content for evaluation.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.content_evaluation_request import ContentEvaluationRequest
from wordlift_client.models.content_evaluation_response import ContentEvaluationResponse
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
    api_instance = wordlift_client.ContentEvaluationsApi(api_client)
    content_evaluation_request = wordlift_client.ContentEvaluationRequest() # ContentEvaluationRequest | 

    try:
        # Evaluate Content
        api_response = await api_instance.evaluate_content_api_content_evaluations_post(content_evaluation_request)
        print("The response of ContentEvaluationsApi->evaluate_content_api_content_evaluations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentEvaluationsApi->evaluate_content_api_content_evaluations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_evaluation_request** | [**ContentEvaluationRequest**](ContentEvaluationRequest.md)|  | 

### Return type

[**ContentEvaluationResponse**](ContentEvaluationResponse.md)

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

