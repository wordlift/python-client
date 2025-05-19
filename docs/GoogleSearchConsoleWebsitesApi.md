# wordlift_client.GoogleSearchConsoleWebsitesApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gsc_sites**](GoogleSearchConsoleWebsitesApi.md#get_gsc_sites) | **GET** /google-search-console/sites | Get Google Search Console sites


# **get_gsc_sites**
> List[Website] get_gsc_sites(related_site_url=related_site_url)

Get Google Search Console sites

List all of sites from the authenticated google search console in account.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.website import Website
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
    api_instance = wordlift_client.GoogleSearchConsoleWebsitesApi(api_client)
    related_site_url = 'related_site_url_example' # str | Filters the list to include only site URLs that are equal to or related to the given site URL, including its parent or base URLs. (optional)

    try:
        # Get Google Search Console sites
        api_response = await api_instance.get_gsc_sites(related_site_url=related_site_url)
        print("The response of GoogleSearchConsoleWebsitesApi->get_gsc_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleSearchConsoleWebsitesApi->get_gsc_sites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **related_site_url** | **str**| Filters the list to include only site URLs that are equal to or related to the given site URL, including its parent or base URLs. | [optional] 

### Return type

[**List[Website]**](Website.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of GSC sites |  -  |
**401** | Unauthorized |  -  |
**412** | When the account is not connected to any Google Search Console |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

