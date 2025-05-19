# wordlift_client.ImageToTextApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_to_text_api_image2_text_v1_post**](ImageToTextApi.md#image_to_text_api_image2_text_v1_post) | **POST** /image-2-text-v1 | Convert Image to Text


# **image_to_text_api_image2_text_v1_post**
> ImageToTextResponse image_to_text_api_image2_text_v1_post(image_to_text_request)

Convert Image to Text

Process an image and generate descriptive text based on its content.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.image_to_text_request import ImageToTextRequest
from wordlift_client.models.image_to_text_response import ImageToTextResponse
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
    api_instance = wordlift_client.ImageToTextApi(api_client)
    image_to_text_request = wordlift_client.ImageToTextRequest() # ImageToTextRequest | 

    try:
        # Convert Image to Text
        api_response = await api_instance.image_to_text_api_image2_text_v1_post(image_to_text_request)
        print("The response of ImageToTextApi->image_to_text_api_image2_text_v1_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageToTextApi->image_to_text_api_image2_text_v1_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_to_text_request** | [**ImageToTextRequest**](ImageToTextRequest.md)|  | 

### Return type

[**ImageToTextResponse**](ImageToTextResponse.md)

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

