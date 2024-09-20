# wordlift_client.SitemapGeneratorApi

All URIs are relative to *https://api.wordlift.io/quality-rating*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_sitemap**](SitemapGeneratorApi.md#generate_sitemap) | **POST** /build | Generate Sitemap


# **generate_sitemap**
> GenerateSitemap200Response generate_sitemap(generate_sitemap_request)

Generate Sitemap

Generates a sitemap from a GraphQL query to WordLift KG. You must provide a valid GraphQL query as the request body. 

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.generate_sitemap200_response import GenerateSitemap200Response
from wordlift_client.models.generate_sitemap_request import GenerateSitemapRequest
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
    api_instance = wordlift_client.SitemapGeneratorApi(api_client)
    generate_sitemap_request = wordlift_client.GenerateSitemapRequest() # GenerateSitemapRequest | 

    try:
        # Generate Sitemap
        api_response = await api_instance.generate_sitemap(generate_sitemap_request)
        print("The response of SitemapGeneratorApi->generate_sitemap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitemapGeneratorApi->generate_sitemap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_sitemap_request** | [**GenerateSitemapRequest**](GenerateSitemapRequest.md)|  | 

### Return type

[**GenerateSitemap200Response**](GenerateSitemap200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

