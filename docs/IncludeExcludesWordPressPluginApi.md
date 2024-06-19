# wordlift_client.IncludeExcludesWordPressPluginApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_include_excludes**](IncludeExcludesWordPressPluginApi.md#list_include_excludes) | **GET** /accounts/me/include-excludes | List
[**update_include_excludes**](IncludeExcludesWordPressPluginApi.md#update_include_excludes) | **PUT** /accounts/me/include-excludes | Update


# **list_include_excludes**
> List[IncludeExclude] list_include_excludes(account)

List

List the include and exclude configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import wordlift_client
from wordlift_client.models.account import Account
from wordlift_client.models.include_exclude import IncludeExclude
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.IncludeExcludesWordPressPluginApi(api_client)
    account = wordlift_client.Account() # Account | 

    try:
        # List
        api_response = await api_instance.list_include_excludes(account)
        print("The response of IncludeExcludesWordPressPluginApi->list_include_excludes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncludeExcludesWordPressPluginApi->list_include_excludes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account**](.md)|  | 

### Return type

[**List[IncludeExclude]**](IncludeExclude.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_include_excludes**
> List[IncludeExclude] update_include_excludes(account, include_exclude_request)

Update

Update the include and exclude configurations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import wordlift_client
from wordlift_client.models.account import Account
from wordlift_client.models.include_exclude import IncludeExclude
from wordlift_client.models.include_exclude_request import IncludeExcludeRequest
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.IncludeExcludesWordPressPluginApi(api_client)
    account = wordlift_client.Account() # Account | 
    include_exclude_request = [wordlift_client.IncludeExcludeRequest()] # List[IncludeExcludeRequest] | 

    try:
        # Update
        api_response = await api_instance.update_include_excludes(account, include_exclude_request)
        print("The response of IncludeExcludesWordPressPluginApi->update_include_excludes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncludeExcludesWordPressPluginApi->update_include_excludes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account**](.md)|  | 
 **include_exclude_request** | [**List[IncludeExcludeRequest]**](IncludeExcludeRequest.md)|  | 

### Return type

[**List[IncludeExclude]**](IncludeExclude.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

