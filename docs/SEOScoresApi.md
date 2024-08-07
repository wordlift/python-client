# wordlift_client.SEOScoresApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seo_score**](SEOScoresApi.md#create_seo_score) | **POST** /score | Create


# **create_seo_score**
> CreateSEOScore200Response create_seo_score(create_seo_score_request)

Create

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.create_seo_score200_response import CreateSEOScore200Response
from wordlift_client.models.create_seo_score_request import CreateSEOScoreRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.SEOScoresApi(api_client)
    create_seo_score_request = wordlift_client.CreateSEOScoreRequest() # CreateSEOScoreRequest | body

    try:
        # Create
        api_response = await api_instance.create_seo_score(create_seo_score_request)
        print("The response of SEOScoresApi->create_seo_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SEOScoresApi->create_seo_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_seo_score_request** | [**CreateSEOScoreRequest**](CreateSEOScoreRequest.md)| body | 

### Return type

[**CreateSEOScore200Response**](CreateSEOScore200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

