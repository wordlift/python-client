# wordlift_client.ClassificationsApi

All URIs are relative to *https://api.wordlift.io/quality-rating*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classify_using_post**](ClassificationsApi.md#classify_using_post) | **POST** /classification/classify | Create


# **classify_using_post**
> ClassificationResponse classify_using_post(body, lang=lang, multi_class=multi_class)

Create

Classify the text to provided categories

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.classification_request import ClassificationRequest
from wordlift_client.models.classification_response import ClassificationResponse
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
    api_instance = wordlift_client.ClassificationsApi(api_client)
    body = wordlift_client.ClassificationRequest() # ClassificationRequest | body
    lang = 'en' # str | Language code (optional) (default to 'en')
    multi_class = False # bool | When set to true the scores will be independent, each will fall between 0 and 1 (optional) (default to False)

    try:
        # Create
        api_response = await api_instance.classify_using_post(body, lang=lang, multi_class=multi_class)
        print("The response of ClassificationsApi->classify_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationsApi->classify_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClassificationRequest**](ClassificationRequest.md)| body | 
 **lang** | **str**| Language code | [optional] [default to &#39;en&#39;]
 **multi_class** | **bool**| When set to true the scores will be independent, each will fall between 0 and 1 | [optional] [default to False]

### Return type

[**ClassificationResponse**](ClassificationResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/ld+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

