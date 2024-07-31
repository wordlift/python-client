# wordlift_client.CustomDomainsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate**](CustomDomainsApi.md#validate) | **POST** /validations | Validate


# **validate**
> validate(domain_validation_request)

Validate

Check if the provided custom domain can be set for the account

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.domain_validation_request import DomainValidationRequest
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
    api_instance = wordlift_client.CustomDomainsApi(api_client)
    domain_validation_request = wordlift_client.DomainValidationRequest() # DomainValidationRequest | 

    try:
        # Validate
        await api_instance.validate(domain_validation_request)
    except Exception as e:
        print("Exception when calling CustomDomainsApi->validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_validation_request** | [**DomainValidationRequest**](DomainValidationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.wordlift.custom-domain-validation+json;version-1

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

