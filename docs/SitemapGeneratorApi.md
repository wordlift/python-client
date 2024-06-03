# wordlift-client.SitemapGeneratorApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_sitemap**](SitemapGeneratorApi.md#generate_sitemap) | **POST** /build | Generate Sitemap


# **generate_sitemap**
> GenerateSitemap200Response generate_sitemap(generate_sitemap_request)

Generate Sitemap

Generates a sitemap from a GraphQL query to WordLift KG. You must provide a valid GraphQL query as the request body. 

### Example


```python
import wordlift-client
from wordlift-client.models.generate_sitemap200_response import GenerateSitemap200Response
from wordlift-client.models.generate_sitemap_request import GenerateSitemapRequest
from wordlift-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift-client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift-client.SitemapGeneratorApi(api_client)
    generate_sitemap_request = wordlift-client.GenerateSitemapRequest() # GenerateSitemapRequest | 

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

No authorization required

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
