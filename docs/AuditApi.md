# wordlift_client.AuditApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit_website**](AuditApi.md#audit_website) | **POST** /audit | Website Audit


# **audit_website**
> AuditResponse audit_website(audit_request)

Website Audit

Performs a comprehensive SEO and AI-readiness audit of a specified URL. The audit analyzes: - Site files (robots.txt, llms.txt, .well-known directory) - SEO fundamentals (title, description, headings) - Structured data (Schema.org, JSON-LD, Microdata) - Content structure and semantic HTML - Image accessibility - Automation readiness for AI agents - JavaScript rendering and bot accessibility - Content freshness (legacy field, status Unknown) - Internal linking (legacy field, status Unknown) - HTML semantics (legacy field, status Unknown)  Returns an overall score (0-100) and detailed recommendations for improvement. 

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.audit_request import AuditRequest
from wordlift_client.models.audit_response import AuditResponse
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
    api_instance = wordlift_client.AuditApi(api_client)
    audit_request = {"url":"https://example.com"} # AuditRequest | 

    try:
        # Website Audit
        api_response = await api_instance.audit_website(audit_request)
        print("The response of AuditApi->audit_website:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditApi->audit_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_request** | [**AuditRequest**](AuditRequest.md)|  | 

### Return type

[**AuditResponse**](AuditResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful audit response |  -  |
**400** | Bad Request - Invalid URL format or domain |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**403** | Forbidden - Bot protection detected |  -  |
**404** | Not Found - Page not found |  -  |
**422** | Validation Error - Invalid request format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

